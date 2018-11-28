#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
const int maxn = 20000;
const int maxx = 1000000000;

int f[maxn][2];
bool g[maxn][2];
int a[maxn], b[maxn];
int n, v, casen;

void init()
{
     scanf("%d%d", &n, &v);
     for (int i(1); i <= n; ++i)
     {
         if (2 * i <= n) scanf("%d%d", &a[i], &b[i]);
         else            scanf("%d", &a[i]);
     }
}

int check(int i, int k)
{
    g[i][k] = true;
    if (2 * i > n) {
       if (a[i] == k) return 0;
       else           return maxx;
    }
    int ans = maxx;
    int p = 0;
    if (a[i] == 0 && b[i] == 1) p = 1;
    else                        p = 0;
    if (a[i] == 1 || (a[i] == 0 && b[i] == 1)) {
       if (k == 1) {
          if (!g[2 * i][k]) f[2 * i][k] = check(2 * i, k);
          if (!g[2 * i + 1][k]) f[2 * i + 1][k] = check(2 * i + 1, k);
          ans = min(ans, f[2 * i][k] + f[2 * i + 1][k] + p);
       }
       else {
            if (!g[2 * i][0]) f[2 * i][0] = check(2 * i, 0);
            if (!g[2 * i + 1][0]) f[2 * i + 1][0] = check(2 * i + 1, 0);
            if (!g[2 * i][1]) f[2 * i][1] = check(2 * i, 1);
            if (!g[2 * i + 1][1]) f[2 * i + 1][1] = check(2 * i + 1, 1);
            ans = min(ans, f[2 * i][0] + f[2 * i + 1][0] + p);
            ans = min(ans, f[2 * i][1] + f[2 * i + 1][0] + p);
            ans = min(ans, f[2 * i][0] + f[2 * i + 1][1] + p);
       }
    }
    if (a[i] == 1 && b[i] == 1) p = 1;
    else                        p = 0;
    if (a[i] == 0 || (a[i] == 1 && b[i] == 1)) {
       if (k == 0) {
          if (!g[2 * i][0]) f[2 * i][0] = check(2 * i, 0);
          if (!g[2 * i + 1][0]) f[2 * i + 1][0] = check(2 * i + 1, 0);
          ans = min(ans, f[2 * i][k] + f[2 * i + 1][k] + p);
       }
       else {
            if (!g[2 * i][0]) f[2 * i][0] = check(2 * i, 0);
            if (!g[2 * i + 1][0]) f[2 * i + 1][0] = check(2 * i + 1, 0);
            if (!g[2 * i][1]) f[2 * i][1] = check(2 * i, 1);
            if (!g[2 * i + 1][1]) f[2 * i + 1][1] = check(2 * i + 1, 1);
            ans = min(ans, f[2 * i][1] + f[2 * i + 1][1] + p);
            ans = min(ans, f[2 * i][1] + f[2 * i + 1][0] + p);
            ans = min(ans, f[2 * i][0] + f[2 * i + 1][1] + p);
       }
       
    }
    return ans;
}

void work()
{
     memset(f, 0, sizeof(f));
     memset(g, 0, sizeof(g));
     f[1][v] = check(1, v);
     if (f[1][v] == maxx) printf("IMPOSSIBLE\n");
     else                 printf("%d\n", f[1][v]);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
