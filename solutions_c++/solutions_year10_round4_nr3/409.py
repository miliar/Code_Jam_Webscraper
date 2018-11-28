#include <stdio.h>

const int maxn = 110;

int a[2][maxn][maxn];
int ans, n, tc;
int u, v, x1, x2, y1, y2;

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf ("%d", &n);
    for (int i = 0; i < maxn; i++)
      for (int j = 0; j < maxn; j++)
        a[0][i][j] = 0;
    int mx = 0, my = 0;
    u = 0; v = 1;
    bool live = false;
    for (int i = 0; i < n; i++)
    {
      scanf ("%d%d%d%d", &x1, &y1, &x2, &y2);
      for (int i = x1 - 1; i < x2; i++)
        for (int j = y1 - 1; j < y2; j++)
        {
          a[0][i][j] = 1;
        }
      if (x2 > mx) mx = x2;
      if (y2 > my) my = y2;
      live = true;
    }
    ans = 0;
    while (live)
    {
      live = false;
      ans++;
      for (int i = 0; i < mx; i++)
        for (int j = 0; j < my; j++)
        {
          if ((i == 0 || a[u][i - 1][j] == 0) &&
              (j == 0 || a[u][i][j - 1] == 0))
            a[v][i][j] = 0;
          else if (i > 0 && a[u][i - 1][j] == 1 &&
                   j > 0 && a[u][i][j - 1] == 1)
            a[v][i][j] = 1;
          else
            a[v][i][j] = a[u][i][j];
          if (a[v][i][j] == 1) live = true;
        }
      u = v; v = 1- u;
    }
    printf ("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
