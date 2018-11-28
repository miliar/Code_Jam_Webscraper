#include <cstdio>

const int maxn = 111;
const int maxk = 30;

int nt, n, k;
int a[maxn][maxk], cu[maxn], nu, nv, ma[maxn];
bool u[maxn], c[maxn][maxn], cc[maxn][maxn];

int dfs( int v )
{
  u[v] = true;
  for (int i = 0; i < n; i++)
    if (cc[v][i] && (ma[i] == -1 || !u[ma[i]] && dfs(ma[i]) == 1))
    {
      ma[i] = v;
      return 1;
    }
  return 0;
}

int main()
{
  scanf("%d", &nt);
  for (int tt = 1; tt <= nt; tt++)
  {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++)
      for (int j = 0; j < k; j++)
        scanf("%d", &a[i][j]);
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
      {
        c[i][j] = false;
        for (int l = 0; l < k; l++)
          if (a[i][l] == a[j][l])
            c[i][j] = true;
        for (int l = 1; l < k; l++)
          if ((a[i][l] > a[j][l]) != (a[i][l - 1] > a[j][l - 1]))
            c[i][j] = true;
      }
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        cc[i][j] = false;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        if (!c[i][j] && a[i][0] < a[j][0])
          cc[i][j] = true;
    for (int i = 0; i < n; i++)
      ma[i] = -1;
    int ans = n;
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
        u[j] = false;
      ans -= dfs(i);
    }
    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
