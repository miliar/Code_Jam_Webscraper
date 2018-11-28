#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>

using std::min;

void dfs( int **g, int *c, int *t, int &tn, int u, int n )
{
  c[u] = 1;
  for (int i = 0; i < n; i++)
    if (g[u][i] && !c[i])
      dfs(g, c, t, tn, i, n);
  t[--tn] = u;
}

int main()
{
  int testN;
  scanf("%d", &testN);
  for (int test = 1; test <= testN; test++)
  {
    int n, k;
    scanf("%d%d", &n, &k);
    int **price = new int*[n];
    int **go = new int*[n];
    for (int i = 0; i < n; i++)
    {
      price[i] = new int[k], go[i] = new int[n];
      for (int j = 0; j < k; j++)
        scanf("%d", &price[i][j]);
    }
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
      {
        go[i][j] = 1;
        for (int t = 0; t < k; t++)
          if (price[i][t] >= price[j][t])
            go[i][j] = 0, t = k;
      }
    int *c = new int[n], *t = new int[n], tn = n;
    memset(c, 0, sizeof(c[0]) * n);
    for (int i = 0; i < n; i++)
      if (c[i] == 0)
        dfs(go, c, t, tn, i, n);
    int **d = new int*[n + 1];
    for (int i = 0; i <= n; i++)
    {
      d[i] = new int[1 << n];
      memset(d[i], 0x7f, sizeof(d[i][0]) * (1 << n));
    }
    d[0][0] = 0;
    for (int i = 0; i < n; i++)
      for (int pr = 0; pr < (1 << n); pr++)
      {
        d[i + 1][pr | (1 << i)] = min(d[i + 1][pr | (1 << i)], d[i][pr] + 1);
        for (int j = 0; j < i; j++)
        {
          if (!go[t[j]][t[i]] || (pr & (1 << j)) == 0)
            continue;
          d[i + 1][(pr & ~(1 << j)) | (1 << i)] = min(
          d[i + 1][(pr & ~(1 << j)) | (1 << i)], d[i][pr]);
        }
      }
    int ans = n;
    for (int i = 0; i < (1 << n); i++)
      ans = min(ans, d[n][i]);
    printf("Case #%d: %d\n", test, ans);
  }
  return 0;
}

