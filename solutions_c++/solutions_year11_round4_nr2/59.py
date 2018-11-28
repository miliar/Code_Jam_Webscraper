#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

char a[505][505];
int sx[505][505];
int sy[505][505];
int s[505][505];

int main(void)
{
//   freopen("B-small-attempt0.in", "r", stdin);
//   freopen("B-small-attempt0.out", "w", stdout);
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);

   scanf("%d", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      int r, c, d;
      scanf("%d%d%d", &r, &c, &d);

      for (int i=0; i<r; i++) {
        scanf("%s", a[i]);
      }
      for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
          a[i][j] -= '0';
          s [i+1][j+1] = s [i+1][j] + s [i][j+1] - s [i][j] + 1 * a[i][j];
          sx[i+1][j+1] = sx[i+1][j] + sx[i][j+1] - sx[i][j] + j * a[i][j];
          sy[i+1][j+1] = sy[i+1][j] + sy[i][j+1] - sy[i][j] + i * a[i][j];
        }
      }

      int ans=0;
      for (int i=min(r, c); i>=3 && !ans; i--) {
        for (int x = 0; x+i <= r; x++)
          for (int y = 0; y+i <= c; y++) {
            int SX = sx[x+i][y+i] - sx[x][y+i] - sx[x+i][y] + sx[x][y]
                     - (y + i - 1) * (a[x+i-1][y+i-1] + a[x][y+i-1])
                     - (y)         * (a[x+i-1][y] + a[x][y]);
            int SY = sy[x+i][y+i] - sy[x][y+i] - sy[x+i][y] + sy[x][y]
                     - (x + i - 1) * (a[x+i-1][y+i-1] + a[x+i-1][y])
                     - (x)         * (a[x][y+i-1] + a[x][y]);
            int S  = s [x+i][y+i] - s [x][y+i] - s [x+i][y] + s [x][y]
                     - (1)         * (a[x+i-1][y+i-1] + a[x][y+i-1])
                     - (1)         * (a[x+i-1][y] + a[x][y]);

            if (SX * 2 == (y + y + i - 1) * S && SY * 2 == (x + x + i - 1) * S) {
              ans = i;
            }
          }
      }

      if (ans)
        printf ("%d\n", ans);
      else 
        puts ("IMPOSSIBLE");
   }
   return 0;
}
