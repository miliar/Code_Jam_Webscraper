#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

#define EPS 0.00001
#define dist(a,b) sqrt( ((a).x - (b).x) * ((a).x - (b).x) + ((a).y - (b).y) * ((a).y - (b).y) )

struct rad {
  int r, index;
  double x, y;
};

vector<rad> radius;

int n, w, l;

bool fits(int i) {
  if (radius[i].x < 0) return false;
  if (radius[i].y < 0) return false;
  if (radius[i].x > w) return false;
  if (radius[i].y > l) return false;
  for (int j = 0; j < i; ++j) {
    if (dist(radius[j], radius[i]) < radius[j].r + radius[i].r) return false;
  }
  return true;
}

bool cmp1 (rad one, rad two) {
  return (one.r > two.r);
}
bool cmp2 (rad one, rad two) {
  return (one.index < two.index);
}

int main() {
  int t; cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    cin >> n >> w >> l;

    radius.clear();
    for (int i = 0; i < n; ++i) {
      rad in; cin >> in.r; in.index = i;
      radius.push_back(in);
    }

    sort(radius.begin(), radius.end(), cmp1);

    radius[0].x = 0.0;
    radius[0].y = 0.0;

    bool line1 = true;
    bool line2 = true;
    for (int i = 1; i < n; ++i) {
      if (line1) {
        radius[i].x = radius[i-1].x + radius[i-1].r + radius[i].r;
        radius[i].y = 0;
        if (radius[i].x > w) {
          line1 = false;
          radius[i].x = 0;
          radius[i].y = radius[0].x + radius[0].r + radius[i].r;
          if (radius[i].y > l) {
            line2 = false;
            --i; continue;
          }
        }
      } else if (line2) {
        radius[i].x = 0;
        radius[i].y = radius[i-1].y + radius[i-1].r + radius[i].r;
        if (radius[i].y > l) {
          line2 = false;
          --i; continue;
        }
      } else {

        for (int j = 0; j < i; ++j) {
          radius[i].x = radius[j].x + radius[j].r + radius[i].r;
          radius[i].y = radius[j].y - radius[j].r + radius[i].r;
          if (fits(i)) break;
          radius[i].x = radius[j].x - radius[j].r + radius[i].r;
          radius[i].y = radius[j].y + radius[j].r + radius[i].r;
          if (fits(i)) break;

          radius[i].x = radius[j].x + radius[j].r + radius[i].r;
          radius[i].y = radius[j].y;
          if (fits(i)) break;
          radius[i].x = radius[j].x;
          radius[i].y = radius[j].y + radius[j].r + radius[i].r;
          if (fits(i)) break;

          radius[i].x = radius[j].x + radius[j].r + radius[i].r;
          radius[i].y = radius[j].y + radius[j].r - radius[i].r;
          if (fits(i)) break;
          radius[i].x = radius[j].x + radius[j].r - radius[i].r;
          radius[i].y = radius[j].y + radius[j].r + radius[i].r;
          if (fits(i)) break;
        }
      }
    }

    sort(radius.begin(), radius.end(), cmp2);

    cout << "Case #" << case_num << ":";
    for (int i = 0; i < n; ++i) {
      printf(" %.04f %.04f", radius[i].x, radius[i].y);
    }
    cout << endl;

  }
  return 0;
}