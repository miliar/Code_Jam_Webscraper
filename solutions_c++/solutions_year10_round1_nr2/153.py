#include <stdio.h>
#include <algorithm>

const int maxn = 110;
const int maxnum = 256;
int a[maxn];
int b[maxn][maxnum + 10];

int tc, D, I, m, n;

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf ("%d%d%d%d", &D, &I, &m, &n);
    for (int i = 1; i <= n; i++)
    {
      scanf ("%d", &a[i]);
    }
    for (int i = 0; i < maxnum; i++)
      b[0][i] = 0;
    for (int i = 1; i <= n; i++)
    {
      for (int j = 0; j < maxnum; j++)
      {
        b[i][j] = b[i - 1][j] + D;  // delete
        for (int k = 0; k < maxnum; k++)
        {
          int cost = abs (a[i] - j) + b[i - 1][k];
          //printf ("%d\n", cost);
          if (abs (j - k) > m)
          {
            if (m == 0)
              continue;
            int cnti = (abs (j - k) - 1) / m;
            cost += cnti * I;
          }
          if (cost < b[i][j])
            b[i][j] = cost;
        }
        //if (i == 2 && j == 50)
        //printf ("%d %d: %d\n", i, j, b[i][j]);
      }
    }
    int ans = b[n][0];
    for (int i = 1; i < maxnum; i++)
      if (ans > b[n][i])
        ans = b[n][i];
    printf ("Case #%d: %d\n", tt, ans);
  }
}
