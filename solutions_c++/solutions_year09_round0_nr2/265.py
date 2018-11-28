#include <iostream>
using namespace std;

const int maxn = 201, maxm = maxn * maxn;
const int w[2][4] = {{-1, 0, 0, 1}, {0, -1, 1, 0}};
int next[maxm << 1], g[maxm], p[maxm << 1], d[maxm], a[maxn][maxn];
int b[maxn][maxn], f[maxm][2];
int n, m, tot, task, tt, no;
char c, s[maxn][maxn];

inline void add(int s, int t)
{
       p[++tot] = t; next[tot] = g[s]; g[s] = tot;
       p[++tot] = s; next[tot] = g[t]; g[t] = tot;
}

void dfs(int x)
{
     s[f[x][0]][f[x][1]] = c; d[x] = 5;
     int i = g[x];
     while (i) {
           if (d[p[i]] < 5) dfs(p[i]);
           i = next[i];
     }
}

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    scanf("%d\n", &task); tt = 0;
    int i, j, k, x, y, t1, t2;
    while (task--) {
          scanf("%d%d\n", &n, &m); no = 0; c = 'a';
          memset(d, 0, sizeof(d));
          memset(p, 0, sizeof(p));
          memset(s, 0, sizeof(s));
          for (i = 1; i <= n; ++i)
              for (j = 1; j <= m; ++j) {
                  scanf("%d", &a[i][j]); b[i][j] = ++no;
                  f[no][0] = i; f[no][1] = j;
              }
          for (i = 1; i <= n; ++i)
              for (j = 1; j <= m; ++j) {
                  t1 = i; t2 = j;
                  for (k = 0; k < 4; ++k) {
                      x = i + w[0][k];
                      y = j + w[1][k];
                      if (x > 0 && x <= n && y > 0 && y <= m)
                         if (a[x][y] < a[t1][t2])
                            {t1 = x; t2 = y;}
                  }
                  if (b[t1][t2] != b[i][j]) add(b[i][j], b[t1][t2]);
              }
          for (i = 1; i <= n; ++i)
              for (j = 1; j <= m; ++j)
                  if (!d[b[i][j]]) {dfs(b[i][j]); ++c;}
          printf("Case #%d:\n", ++tt);
          for (i = 1; i <= n; ++i) {
              for (j = 1; j < m; ++j)
                  printf("%c ", s[i][j]);
              printf("%c\n", s[i][m]);
          }
    }
    return 0;
}
