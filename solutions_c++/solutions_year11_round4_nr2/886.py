#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define maxn 550
#define eps 1e-8

typedef long double dbl;

int T;
int r, c, d;
int sum[maxn][maxn];
int m[maxn][maxn];

int main () {
  scanf("%d", &T);
  for (int qn = 1; qn <= T; qn++) {
    scanf("%d%d%d \n", &r, &c, &d);
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        char cc;
        scanf("%c", &cc), m[i][j] = cc, m[i][j] -= '0';
      }
      scanf(" \n");
    }
  

    int ans = 0;
    for (int x = 0; x < r; x++) {
      for (int y = 0; y < c; y++) {
        for (int rd = 1; rd <= min(r - x, c - y); rd++) {
          dbl cx = 0, cy = 0, sumd = 0;
          for (int i = x; i < x + rd; i++) {
            for (int j = y; j < y + rd; j++) {
              if (i == x && j == y) continue;
              if (i == x + rd - 1 && j == y) continue;
              if (i == x && j == y + rd - 1) continue;
              if (i == x + rd - 1 && j == y + rd - 1) continue;
              cx += i * (m[i][j] + d);
              cy += j * (m[i][j] + d);
              sumd += (m[i][j] + d);
            }
          }
          cx /= sumd;
          cy /= sumd;

          if (abs(cx - (x + x + rd - 1) / 2.0) < eps && abs(cy - (y + y + rd - 1) / 2.0) < eps) {
            ans = max(ans, rd);
          }
        }
      }
    }

    if (ans < 3) {
      printf("Case #%d: IMPOSSIBLE\n", qn);
    } else {
      printf("Case #%d: %d\n", qn, ans);
    }
  }


  return 0;
}