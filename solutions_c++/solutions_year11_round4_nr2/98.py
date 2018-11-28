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
const int max_n = 512;

int m, n, D;
int a[max_n][max_n];
int sx[max_n][max_n], sy[max_n][max_n], sum[max_n][max_n];
int ans;
int T, I;

inline int get(int x, int y) {
  if (x < 0 || y < 0)
    return 0;
  else
    return sum[x][y];
}

inline int getx(int x, int y) {
  if (x < 0 || y < 0)
    return 0;
  else
    return sx[x][y];
}

inline int gety(int x, int y) {
  if (x < 0 || y < 0)
    return 0;
  else
    return sy[x][y];
}

void input() {
  scanf("%d %d %d", &m, &n, &D);
  for (int x = 0; x < m; ++x) {
    for (int y = 0; y < n; ++y) {
      char ch;
      do {
        scanf("%c", &ch);
      } while (ch < '0' || ch > '9');
      a[x][y] = ch - '0';
      // fprintf(stderr, "%d", a[x][y]);
    }
    // fprintf(stderr, "\n");
  }
}

bool check(int totx, int tot, int x, int s) {
  int fz, fm;
  if (s % 2 == 0) {
    fm = 2;
    fz = x * 2 + s - 1;
  } else {
    fm = 1;
    fz = x + (s - 1) / 2;
  }
  return totx * fm == tot * fz;
}

void solve() {
  for (int x = 0; x < m; ++x) {
    for (int y = 0; y < n; ++y) {
      if (x == 0 && y == 0) {
        sx[x][y] = a[x][y] * x;
        sy[x][y] = a[x][y] * y;
        sum[x][y] = a[x][y];
      } else if (x == 0) {
        sx[x][y] = sx[x][y - 1] + a[x][y] * x;
        sy[x][y] = sy[x][y - 1] + a[x][y] * y;
        sum[x][y] = sum[x][y - 1] + a[x][y];
      } else if (y == 0) {
        sx[x][y] = sx[x - 1][y] + a[x][y] * x;
        sy[x][y] = sy[x - 1][y] + a[x][y] * y;
        sum[x][y] = sum[x - 1][y] + a[x][y];
      } else {
        sx[x][y] = sx[x - 1][y] + sx[x][y - 1] - sx[x - 1][y - 1] + a[x][y] * x;
        sy[x][y] = sy[x - 1][y] + sy[x][y - 1] - sy[x - 1][y - 1] + a[x][y] * y;
        sum[x][y] = sum[x - 1][y] + sum[x][y - 1] - sum[x - 1][y - 1] + a[x][y];
      }
    }
  }
  for (int s = min(m, n); s >= 3; --s) {
    for (int x = 0; x + s <= m; ++x) {
      for (int y = 0; y + s <= n; ++y) {
        int totx = getx(x + s - 1, y + s - 1) -
          getx(x - 1, y + s - 1) - getx(x + s - 1, y - 1) +
          getx(x - 1, y - 1);
        int toty = gety(x + s - 1, y + s - 1) -
          gety(x - 1, y + s - 1) - gety(x + s - 1, y - 1) +
          gety(x - 1, y - 1);
        int tot = get(x + s - 1, y + s - 1) -
          get(x - 1, y + s - 1) - get(x + s - 1, y - 1) +
          get(x - 1, y - 1);
        totx = totx - a[x][y] * x - a[x][y + s - 1] * x -
          a[x + s - 1][y] * (x + s - 1) - a[x + s - 1][y + s - 1] * (x + s - 1);
        toty = toty - a[x][y] * y - a[x][y + s - 1] * (y + s - 1) -
          a[x + s - 1][y] * y - a[x + s - 1][y + s - 1] * (y + s - 1);
        tot = tot - a[x][y] - a[x][y + s - 1] -
          a[x + s - 1][y] - a[x + s - 1][y + s - 1];
        if (check(totx, tot, x, s) && check(toty, tot, y, s)) {
          // fprintf(stderr, "%d %d %d\n", x, y, s);
          ans = s;
          return;
        }
      }
    }
  }
  ans = -1;
}

void output() {
  printf("Case #%d: ", I + 1);
  fprintf(stderr, "Case #%d: ", I + 1);
  if (ans == -1)
    printf("IMPOSSIBLE\n");
  else
    printf("%d\n", ans);
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

