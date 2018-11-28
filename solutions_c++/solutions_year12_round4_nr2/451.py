#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <set>

using namespace std;

typedef long long llong;
typedef pair<int, int> pii;

inline double sqr(double x) { return x * x; }

#define RAD first
#define IND second

int n;
llong W, L;
set<pair<llong, int> > r;
bool doswap;
vector<int> x;
vector<int> y;
vector<bool> used;

void rec(llong x0, llong x1, llong y0, bool left, bool down) {
  for (set<pair<llong, int> >::reverse_iterator it = r.rbegin(); it != r.rend(); ++it) {
    int i = (*it).IND;
    if (used[i]) continue;
    int R = (*it).RAD;
    int xc = left ? x0 : x0 + R;
    int yc = down ? y0 : y0 + R;
    // printf("index = %d, R = %d, at (%d, %d) ~ ", r[i].IND, R, xc, yc);
    if (xc + R <= x1 && yc <= L) {
      // printf("ok\n");
      x[i] = xc;
      y[i] = yc;
      used[i] = true;
      r.erase(*it);
      rec(x0, xc + R, yc + R, left, false);
      rec(xc + R, x1, y0, false, down);
      return;
    } else {
      // printf("fail\n");
    }
  }
}

void solve() 
{
  cin >> n >> W >> L;
  //  r.resize(n);
  llong R;
  for (int i = 0; i < n; ++i) {
    cin >> R;
    r.insert(make_pair(R, i));
  }
  if (W < L) {
    doswap = true;
    swap(W, L);
  } else {
    doswap = false;
  }
  //  sort(r.rbegin(), r.rend());
  x.resize(n);
  y.resize(n);
  used.assign(n, false);
  R = r.rbegin()->RAD;
  rec(0, W + R + 5, 0, true, true);
  if (doswap)
    swap(x, y);
  for (int i = 0; i < n; ++i) {
    printf("%d %d ", x[i], y[i]);
    assert(used[i]);
  }
  printf("\n");
}

int main()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
