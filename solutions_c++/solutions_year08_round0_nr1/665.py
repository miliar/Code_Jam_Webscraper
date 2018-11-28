#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
const int maxn = 2000;
const int maxx = 1000000;
int n, m, casen;
string a[maxn], b[maxn];
int f[maxn][maxn];
int g[maxn][maxn];
string s;

void init()
{
     scanf("%d", &n); getline(cin, s);
     for (int i(1); i <= n; ++i) getline(cin, a[i]);
     scanf("%d", &m); getline(cin, s);
     for (int i(1); i <= m; ++i) getline(cin, b[i]);
     memset(g, 0, sizeof(g));
     for (int i(1); i <= m; ++i)
         for (int j(1); j <= n; ++j) if (b[i] == a[j]) g[i][j] = 1;
     memset(f, 0, sizeof(f));
     //printf("%d %d\n", n, m);
}

void work()
{
     f[0][0] = 0;
     for (int i(1); i <= n; ++i) if (g[1][i] == 1) f[1][i] = maxx;
     for (int i(2); i <= m; ++i)
     {
         for (int j(1); j <= n; ++j)
         {
             if (g[i][j] == 1) {
                f[i][j] = maxx;  continue;
             }
             f[i][j] = f[i - 1][j];
             for (int l(1); l <= n; ++l) if (l != j) {
                 if (f[i - 1][l] + 1 < f[i][j]) f[i][j] = f[i - 1][l] + 1;
             }
         }
     }
     int ans = maxx;
     for (int i(1); i <= n; ++i) if (f[m][i] < ans) ans = f[m][i];
     printf("%d\n", ans);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        printf("Case #%d: ", i);
        init();
        work();
    }
    return 0;
}
