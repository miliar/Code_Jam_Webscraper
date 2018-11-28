#include <cstdio>
#include <string>

const int maxn = 1100;
const int num[] = {0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};

int k[maxn], t;
int f[maxn][maxn];
int m, n, casen;
bool block[maxn][maxn];
char s[maxn];
int a[maxn];
int e[maxn][maxn];
int sum[maxn];


int pre[maxn][maxn];

void check(int i)
{
     if (i > n) {
        int temp = 0;
        for (int j(1); j <= n; ++j) temp = temp * 2 + a[j];
        //for (int j(1); j <= n; ++j) printf("%d", a[j]);
        //printf("\n");
        k[++t] = temp;
        return;
     }
     a[i] = 0;  check(i + 1);
     if (i == 1 || a[i - 1] == 0) {
        a[i] = 1;  check(i + 1);
     }
}

void init()
{
     scanf("%d%d", &m, &n);
     memset(block, 0, sizeof(block));
     for (int i(1); i <= m; ++i)
     {
         scanf("%s", &s);
         for (int j(1); j <= n; ++j) if (s[j - 1] == '.') block[i][j] = true;
     }
     t = 0;
     check(1);
     
     //for (int i(1); i <= t; ++i) printf("%d\n", k[i]);
     
     
     
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
     /*
     for (int i(1); i <= t; ++i)
     {
         for (int j(1); j <= e[i][0]; ++j) printf("%d ", e[i][j]);
         printf("\n");
     }
     */
     
}

bool check(int kk, int q)
{
     for (int i(1); i <= n; ++i) if ((k[q] | num[n - i + 1]) == k[q] && !block[kk][i]) return false;
     return true;
}

void work()
{
     for (int i(1); i <= t; ++i)
     {
         sum[i] = 0;
         for (int j(1); j <= n; ++j) if ((k[i] | num[j]) == k[i]) ++sum[i];
     }
     memset(f, 0, sizeof(f));
     for (int i(1); i <= t; ++i) if (check(m, i)) f[m][i] = sum[i]; else f[m][i] = -1;
     for (int i(m - 1); i >= 1; --i)
     {
         for (int j(1); j <= t; ++j)
         {
             if (!check(i, j)) {f[i][j] = -1; continue;}
             f[i][j] = -1;
             for (int l(1); l <= e[j][0]; ++l)
             {
                 int v = e[j][l];
                 if (f[i + 1][v] != -1 && sum[j] + f[i + 1][v] > f[i][j]) {
                    f[i][j] = sum[j] + f[i + 1][v];  pre[i][j] = v;
                 }
             }
         }
     }
     int ans = 0;
     for (int i(1); i <= t; ++i) if (f[1][i] > ans) ans = f[1][i];
     printf("%d\n", ans);
     
     /*
     ans = 0;
     int kk;
     for (int i(1); i <= t; ++i) if (f[1][i] > ans) {ans = f[1][i];  kk = i;}
     for (int i(1); i <= m; ++i)
     {
         int temp = k[kk];
         for (int j(1); j <= n; ++j) {a[j] = temp % 2;  temp /= 2;}
         for (int j(n); j >= 1; --j) printf("%d", a[j]);
         kk = pre[i][kk];
         printf("\n");
     }*/
}

int main()
{
    freopen("C-small.txt", "r", stdin);
    freopen("C.ans", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
