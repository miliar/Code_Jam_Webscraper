#include <cstdio>
#include <string>

const int maxn = 3000;

int ans[maxn];
int e[maxn][maxn], best[maxn];
int n, m, casen;

void init()
{
     memset(best, 0, sizeof(best));
     scanf("%d%d", &n, &m);
     memset(e, 0, sizeof(e));
     int x, y;
     for (int i(1); i <= m; ++i)
     {
         int t;
         scanf("%d", &t);
         for (int j(1); j <= t; ++j)
         {
             scanf("%d%d", &x, &y);
             if (y == 1) best[i] = x;
             else        e[i][++e[i][0]] = x;
         }
     }
}

void work()
{
     memset(ans, 0, sizeof(ans));
     for (int i(1); i <= n + 1; ++i)
     {
         int ok = true;
         for (int j(1); j <= m; ++j)
         {
             int change = true;
             if (best[j] != 0 && ans[best[j]] == 1) change = false;
             else {
                  for (int l(1); l <= e[j][0]; ++l) if (ans[e[j][l]] == 0) {
                      change = false;  break;
                  }
             }
             if (change) {
                if (best[j] == 0) {
                   printf(" IMPOSSIBLE\n");  return;
                }
                else ans[best[j]] = 1;
                ok = false;
             }
         }
         if (ok) {
            for (int j(1); j <= n; ++j) printf(" %d", ans[j]);
            printf("\n");
            return;
         }
     }
     printf(" IMPOSSIBLE\n");
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.ans", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d:", i);
        work();
    }
    return 0;
}
