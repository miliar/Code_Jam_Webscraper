#include <cstdio>
#include <cstring>

const int maxn = 1100;
const int num[] = {0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};

bool g[maxn][maxn];
char s[maxn];
int a[maxn];
int e[maxn][maxn];
int S[maxn];
int k[maxn], t;
int f[maxn][maxn];
int m, n, Test,ans;
int pre[maxn][maxn];

void check(int i)
{
     if (i > n) {
        int tmp = 0;
        for (int j(1); j <= n; ++j) tmp = tmp * 2 + a[j];
        
        k[++t] = tmp;
        return;
     }
     a[i] = 0;  check(i + 1);
     if (i == 1 || a[i - 1] == 0) {
        a[i] = 1;  check(i + 1);
     }
}



bool check(int kk, int q)
{
     for (int i(1); i <= n; ++i) if ((k[q] | num[n - i + 1]) == k[q] && !g[kk][i]) return false;
     return true;
}

void work()
{
     for (int i(1); i <= t; ++i)
     {
         S[i] = 0;
         for (int j(1); j <= n; ++j) if ((k[i] | num[j]) == k[i]) ++S[i];
     }
     memset(f, 0, sizeof(f));
     for (int i(1); i <= t; ++i) if (check(m, i)) f[m][i] = S[i]; else f[m][i] = -1;
     for (int i(m - 1); i >= 1; --i)
     {
         for (int j(1); j <= t; ++j)
         {
             if (!check(i, j)) {f[i][j] = -1; continue;}
             f[i][j] = -1;
             for (int l(1); l <= e[j][0]; ++l)
             {
                 int v = e[j][l];
                 if (f[i + 1][v] != -1 && S[j] + f[i + 1][v] > f[i][j]) {
                    f[i][j] = S[j] + f[i + 1][v];  pre[i][j] = v;
                 }
             }
         }
     }
     ans = 0;
     for (int i(1); i <= t; ++i) 
        if (f[1][i] > ans) ans = f[1][i];
}

int main()
{
    freopen("C-small.txt", "r", stdin);
    freopen("C.ans", "w", stdout);
    scanf("%d", &Test);
    for (int i(1); i <= Test; ++i)
    {
       scanf("%d%d", &m, &n);
     memset(g, 0, sizeof(g));
     for (int i(1); i <= m; ++i)
     {
         scanf("%s", &s);
         for (int j(1); j <= n; ++j) if (s[j - 1] == '.') g[i][j] = true;
     }
     t = 0;
     check(1);
     memset(e, 0, sizeof(e));
     for (int i(1); i <= t; ++i)
     {
         for (int j(1); j <= t; ++j)
         {
             bool ok = true;
             for (int l(1); l <= n; ++l) if ((k[i] | num[n - l + 1]) == k[i]) {
                 if (l > 1 && (k[j] | num[n - (l - 1) + 1]) == k[j]) {ok = false;  break;}
                 if (l < n && (k[j] | num[n - (l + 1) + 1]) == k[j]) {ok = false;  break;}
             }
             if (ok) e[i][++e[i][0]] = j;
         }
     }
        work();
        printf("Case #%d: %d\n", i,ans);
    }
    return 0;
}
