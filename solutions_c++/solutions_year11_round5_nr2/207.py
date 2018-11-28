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
const int m = 16384;

int n;
int b[m], bkp[m];
int T, I, ans;

void input() {
  scanf("%d", &n);
  memset(b, 0, sizeof b);
  for (int i = 0; i < n; ++i) {
    int x;
    scanf("%d", &x);
    b[x]++;
  }
}

bool can(int len) {
  memcpy(bkp, b, sizeof b);
  for (int x = 0; x < m; ++x) {
    while (b[x] > 0) {
      // cerr << "x = " << x << endl;
      b[x]--;
      int y = x + 1, cur = 1;
      while (true) {
        if (b[y] == 0) {
          if (cur < len) {
            memcpy(b, bkp, sizeof b);
            return false;
          }
          break;
        }
        assert(b[y] > 0);
        if (b[y] > b[y - 1]) {
          b[y]--;
          cur++;
          y++;
          continue;
        }
        if (cur >= len)
          break;
        b[y]--;
        cur++;
        y++;
      }
      // cerr << x << ' ' << y << endl;
    }
  }
  memcpy(b, bkp, sizeof b);
  return true;
}

void solve() {
  if (n == 0) {
    ans = 0;
    return;
  }
#if 0
  bool ret = can(2);
  cout << "ret = " << ret << endl;
  ans = 2;
#endif
#if 1
  int low = 1, high = n;
  while (low < high) {
    int mid = (low + high + 1) / 2;
    if (can(mid))
      low = mid;
    else
      high = mid - 1;
  }
  assert(low == high);
  ans = low;
#endif
}

void output() {
  printf("Case #%d: %d\n", I + 1, ans);
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

