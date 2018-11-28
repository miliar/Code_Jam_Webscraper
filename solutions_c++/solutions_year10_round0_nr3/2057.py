#include <cstdio>
#include <cstring>

int pre[1010][1010];

int main (void)
{
  int test, tests, R, k, n;
  int i, j, p;
  int mx, nmx, pos;
  long long res;
  int g[1010];
  int wh[1010];
  int hm[1010];
  freopen ("clarge.in", "rt", stdin);
  freopen ("clarge.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    memset (pre, 0, sizeof(pre));
    memset (wh, 0, sizeof(wh));
    memset (hm, 0, sizeof(hm));
    res = 0;
    scanf ("%d %d %d", &R, &k, &n);
    for (i = 0; i < n; i++)
      scanf ("%d", &g[i]);
    for (i = 0; i < n; i++)
      pre[i][i] = g[i];
    
    for (i = 0; i < n; i++)
      for (j = i+1; j < n; j++)
      {
        if (pre[i][j-1] == -1)
          pre[i][j] = -1;
        else
          pre[i][j] = pre[i][j-1] + g[j];
        if (pre[i][j] > k)
          pre[i][j] = -1;          
      }
    for (i = 1; i < n; i++)
      for (j = 0; j < i; j++)
      {
        if (j == 0)
          p = n - 1;
        else
          p = j - 1;
        if (pre[i][p] == -1)
          pre[i][j] = -1;
        else
          pre[i][j] = pre[i][p] + g[j];
        if (pre[i][j] > k)
          pre[i][j] = -1;          
      }
    for (i = 0 ; i < n; i++)
    {
      mx = -1;
      for (j = 0; j < n; j++)
        if (mx < pre[i][j])
          mx = pre[i][j], nmx = j + 1;
      if (nmx == n)
        nmx = 0;
      wh[i] = nmx;
      hm[i] = mx;
    }
    pos = 0;
    for (i = 0; i < R; i++)
    {
      res = res + hm[pos];
      pos = wh[pos];
    } 
    printf ("Case #%d: %I64d\n", test + 1, res);
  }
  return 0;
}
