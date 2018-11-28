#include <cstdio>
#include <string>

const int maxn = 500;

int e[maxn][maxn];
bool x[maxn], y[maxn];
int Link[maxn];
int a[maxn][maxn];
int n, m, casen, T;
int t1[maxn], t2[maxn];

void init()
{
     scanf("%d", &T);
     scanf("%d%d", &n, &m);
     int h, min;
     for (int i(1); i <= n + m; ++i)
     {
         scanf("%d:%d", &h, &min);
         t1[i] = h * 60 + min;
         scanf("%d:%d", &h, &min);
         t2[i] = h * 60 + min;
     }
     memset(a, 0, sizeof(a));
     for (int i(1); i <= n; ++i)
     {
         for (int j(n + 1); j <= n + m; ++j)
         {
             if (t2[i] + T <= t1[j]) a[i][++a[i][0]] = j;
             if (t2[j] + T <= t1[i]) a[j][++a[j][0]] = i;
         }
     }
}

bool check(int u)
{
     for (int i(1); i <= a[u][0]; ++i)
     {
         int v = a[u][i];
         if (!y[v]) {
            y[v] = true;
            if (Link[v] == 0 || check(Link[v])) {
               Link[v] = u;
               return true;
            }
         }
     }
     return false;
}

void work()
{
     memset(Link, 0, sizeof(Link));
     int ans1 = 0, ans2 = 0;
     for (int i(1); i <= n + m; ++i)
     {
         memset(y, 0, sizeof(y));
         check(i);
     }
     for (int i(1); i <= n + m; ++i) if (Link[i] == 0) {
         if (i <= n) ++ans1; else ++ans2;
     }
     printf("%d %d\n", ans1, ans2);
} 

int main()
{
    freopen("B-large.in", "r", stdin);
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
