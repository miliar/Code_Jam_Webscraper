#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);
const int max_n = 128;

struct Point {
  int x, y;
};

int W, L, U, G;
Point l[max_n], u[max_n];
vector<int> X;
vector<Real> ans;
int T, I;
Real length[max_n * 2];

void input() {
  scanf("%d %d %d %d\n", &W, &L, &U, &G);
  for (int i = 0; i < L; ++i)
    scanf("%d %d", &l[i].x, &l[i].y);
  for (int i = 0; i < U; ++i)
    scanf("%d %d", &u[i].x, &u[i].y);
}

Real get_y(int x1, int y1, int x2, int y2, int x) {
  assert(x >= x1 && x <= x2);
  if (x == x1)
    return y1;
  if (x == x2)
    return y2;
  return y1 + (Real)(y2 - y1) * (x - x1) / (x2 - x1);
}

Real get_length(int i, int j, int x) {
  return get_y(u[j].x, u[j].y, u[j + 1].x, u[j + 1].y, x) -
    get_y(l[i].x, l[i].y, l[i + 1].x, l[i + 1].y, x);
}

Real get_x(Real x1, Real len1, Real x2, Real len2, Real area, Real &res) {
  // cerr << x1 << ' ' << len1 << ' ' << x2 << ' ' << len2 << ' ' << area << endl;
  Real low = x1, high = x2;
  while (true) {
    // cerr << low << ' ' << high << endl;
    Real x = (low + high) / 2;
    Real len = len1 + (len2 - len1) * (x - x1) / (x2 - x1);
    Real cur = (len1 + len) * (x - x1) / 2;
    if (abs(cur - area) <= o) {
      res = len;
      return x;
    }
    if (cur > area)
      high = x;
    else
      low = x;
  }
}

void solve() {
  
  X.clear();
  for (int i = 0; i < L; ++i)
    X.push_back(l[i].x);
  for (int i = 0; i < U; ++i)
    X.push_back(u[i].x);
  sort(X.begin(), X.end());
  X.resize(unique(X.begin(), X.end()) - X.begin());

  int i = 0, j = 0;
  for (size_t k = 0; k < X.size(); ++k) {
    while (X[k] > l[i + 1].x)
      ++i;
    while (X[k] > u[j + 1].x)
      ++j;
    length[k] = get_length(i, j, X[k]);
    // cerr << "len = " << length[k] << endl;
  }

  Real tot = 0;
  for (size_t k = 0; k + 1 < X.size(); ++k) {
    tot += (length[k] + length[k + 1]) * (X[k + 1] - X[k]) / 2;
  }
  Real unit = tot / G;
  Real x = X[0], len = length[0];
  size_t k = 0;
  ans.clear();
  for (int t = 0; t + 1 < G; ++t) {
    Real cur = 0;
    while (cur < unit - o) {
      assert(k < X.size());
      Real whole = (length[k] + len) * (X[k] - x) / 2;
      if (cur + whole >= unit - o) {
        x = get_x(x, len, X[k], length[k], unit - cur, len);
        cur = unit;
        continue;
      } else {
        x = X[k];
        len = length[k];
        cur += whole;
        ++k;
      }
    }
    ans.push_back(x);
  }
}

void output() {
  printf("Case #%d:\n", I + 1);
  for (size_t i = 0; i < ans.size(); ++i)
    printf("%.8Lf\n", ans[i]);
}

int main() {
  scanf("%d", &T);
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

