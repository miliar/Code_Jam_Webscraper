#include <stdio.h>
#include <algorithm>

const int maxm = 12;

struct Node
{
  int n;
  int v[maxm];
} a[maxm][1 << maxm];

int p[maxm][1 << maxm];
int z[1 << maxm];
int m, tc;

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf ("%d", &m);
    int n = 1 << m;
    for (int i = 0; i < n; i++)
    {
      scanf ("%d", &z[i]);
    }
    int maxp = 0;
    for (int i = 0; i < m; i++)
    {
      for (int j = 0; j < (1 << (m - i - 1)); j++)
      {
        scanf ("%d", &p[i][j]);
        maxp += p[i][j];
        //printf ("p %d %d = %d\n", i, j, p[i][j]);
      }
    }
    for (int i = 0; i < (1 << (m - 1)); i++)
    {
      // printf ("i: %d\n", i);
      int tx = std::min (z[i * 2], z[i * 2 + 1]);
      a[0][i].n = tx;
      a[0][i].v[0] = p[0][i];
      if (tx > 0)
        for (int j = 1; j <= tx; j++)
          a[0][i].v[j] = 0;
      // printf ("tx: %d\n", tx);
    }
    // printf ("asdf\n");
    for (int i = 1; i <m; i++)
    {
      for (int j = 0; j < (1 << (m - i - 1)); j++)
      {
        int c1 = j * 2;
        int c2 = c1 + 1;
        for (int k = 0; k <= m; k++)
          a[i][j].v[k] = maxp;
        int n1 = a[i - 1][c1].n, n2 = a[i - 1][c2].n;
        //printf ("%d %d, c1 = %d, c2 = %d, n1 = %d n2 = %d\n", i, j, c1, c2, n1, n2);
        a[i][j].n = std:: min (n1, n2);
        for (int k = 0; k <= n1; k++)
          for (int l = 0; l <= n2; l++)
          {
            int x = a[i][j].n - std::min (n1 - k, n2 - l);
            int v = a[i - 1][c1].v[k] + a[i - 1][c2].v[l];
            // printf ("k=%d, l=%d, x=%d, v=%d\n", k, l, x, v);
            // printf ("n = %d, +1 = %d\n", a[i][j].n, a[i][j].v[x + 1]);
            if (x < a[i][j].n && v < a[i][j].v[x + 1])
            {
              // printf ("hit+1\n");
              a[i][j].v[x + 1] = v;
            }
            v += p[i][j];
            if (a[i][j].v[x] > v)
            {
              // printf ("hit\n");
              a[i][j].v[x] = v;
            }
          }
        // for (int k = 0; k <= a[i][j].n; k++)
        // {
        //   printf ("v%d=%d ", a[i][j].n - k, a[i][j].v[k]);
        // }printf("\n");
      }
    }
    int ans = a[m - 1][0].v[0];
    for (int i = 1; i <= a[m - 1][0].n; i++)
    {
      if (ans > a[m - 1][0].v[i])
        ans = a[m - 1][0].v[i];
    }
    printf ("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
