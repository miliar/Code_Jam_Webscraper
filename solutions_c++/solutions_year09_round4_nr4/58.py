#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "D"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

struct point {
  double x, y;
};

struct circle {
  point o;
  double r;
};

const long double eps = 1e-6;

double dist(point a, point b) {
  return hypot(a.x - b.x, a.y - b.y);
}

bool IsIn(const circle& d, const circle& c) {
  return dist(c.o, d.o) + c.r < d.r + eps;
}

bool Cover(const vector<circle>& circles, const circle& c1, const circle& c2) {
  for (int i = 0; i < circles.size(); ++i) {
    if (!IsIn(c1, circles[i]) && !IsIn(c2, circles[i])) {
      return false;
    }
  }
  return true;
}


vector<circle> GetCircles(const circle& c1, const circle& c2, double r) {
  vector<circle> result;
  double d = dist(c1.o, c2.o);
  if (r < c1.r || r < c2.r) {
    return result;
  }
  if (d > r - c1.r + r - c2.r) {
    return result;
  }
  if (r - c1.r > d + r - c2.r) {
    return result;
  }
  if (r - c2.r > d + r - c1.r) {
    return result;
  }
  double alpha = acos( (d * d + (r - c1.r) * (r - c1.r) - (r - c2.r) * (r - c2.r)) / (2 * d * (r - c1.r)));
  double beta = atan2(c2.o.y - c1.o.y, c2.o.x - c1.o.x);
  circle ans1;
  ans1.o.x = c1.o.x + (r - c1.r) * cos(beta + alpha);
  ans1.o.y = c1.o.y + (r - c1.r) * sin(beta + alpha);
  ans1.r = r;
  double d1 = dist(ans1.o, c1.o);
  double d2 = dist(ans1.o, c2.o);
  if (fabs(d1 - (r - c1.r)) > eps || fabs(d2 - (r - c2.r)) > eps) {
    abort();
  }
  result.push_back(ans1);
  circle ans2;
  ans2.o.x = c1.o.x + (r - c1.r) * cos(beta - alpha);
  ans2.o.y = c1.o.y + (r - c1.r) * sin(beta - alpha);
  ans2.r = r;
  result.push_back(ans2);
  return result;
}

bool CanFit(double r, const vector<circle>& circles) {
  vector< vector< vector<circle> > > all_circles(circles.size(), vector< vector<circle> >(circles.size()));
  for (int i1 = 0; i1 < circles.size(); ++i1) {
    circle c = circles[i1];
    c.r = r;
    all_circles[i1][i1].push_back(c);
    for (int i2 = i1 + 1; i2 < circles.size(); ++i2) {
      all_circles[i1][i2] = GetCircles(circles[i1], circles[i2], r);
    }
  }
  vector<ll> masks;
  for (int i1 = 0; i1 < circles.size(); ++i1) {
    for (int i2 = i1; i2 < circles.size(); ++i2) {
      for (int l = 0; l < all_circles[i1][i2].size(); ++l) {
        ll mask = 0;
        for (int k = 0; k < circles.size(); ++k) {
          if (IsIn(all_circles[i1][i2][l], circles[k])) {
            mask |= (ll(1) << k);
          }
        }
        masks.push_back(mask);
      }
    }
  }
  for (int i = 0; i < masks.size(); ++i) {
    if (masks[i] == ((ll(1) << circles.size()) - 1)) {
      return true;
    }
    for (int j = i + 1; j < masks.size(); ++j) {
      if ((masks[i] | masks[j]) == ((ll(1) << circles.size()) - 1)) {
        return true;
      }
    }
  }
  /*for (int i1 = 0; i1 < circles.size(); ++i1) {
    for (int i2 = i1; i2 < circles.size(); ++i2) {
      for (int k = 0; k < all_circles[i1][i2].size(); ++k) {
        for (int i3 = i1; i3 < circles.size(); ++i3) {
          for (int i4 = i3; i4 < circles.size(); ++i4) {
            for (int l = 0; l < all_circles[i3][i4].size(); ++l) {
              if (Cover(circles, all_circles[i1][i2][k], all_circles[i3][i4][l])) {
                return true;
              }
            }
          }
        }
      }
    }
  }*/
  return false;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int circle_count;
    cin >> circle_count;
    vector<circle> circles(circle_count);
    for (int i = 0; i < circle_count; ++i) {
      cin >> circles[i].o.x >> circles[i].o.y >> circles[i].r;
    }
    double rmin = 0;
    for (int i = 0; i < circles.size(); ++i) {
      rmin = max(rmin, circles[i].r);
    }
    double rmax = max(rmin, 2000.);
    while (rmax - rmin > eps && (rmax - rmin) / rmax > eps) {
      cerr << rmin << ' ' << rmax << endl;
      double r = (rmin + rmax) / 2;
      if (CanFit(r, circles)) {
        rmax = r;
      } else {
        rmin = r;
      }
    }
    printf("Case #%d: %.10lf\n", test_index + 1, rmax);
    cerr << test_index + 1 << " of " << test_count << endl;
  }
  return 0;
}
