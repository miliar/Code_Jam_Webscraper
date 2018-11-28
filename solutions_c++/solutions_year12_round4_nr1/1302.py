#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int maxN = 10010;
int f[maxN][maxN];
struct vine
{
       int d, l;
} a[maxN];
int T, n, d;

bool cmp(vine a, vine b)
{
     return a.d < b.d;
}


bool dfs(int u, int v)
{
     if (f[u][v] != -1) return f[u][v];
     if (u == n - 1)
     {
           f[u][v] = 1;
           return 1;
     }
     f[u][v] = 0;
     int l = min(a[u].d - a[v].d, a[u].l);
     for (int i = u + 1; i <= n; i++)
     {
         if (a[u].d + l < a[i].d) break;
         dfs(i, u);
         if (f[i][u])
         {
                     f[u][v] = 1;
                     break;
         }
     }
     return f[u][v];
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d", &n);
        a[0].d = 0;
        for (int i = 1; i <= n; i++)
            scanf("%d%d", &a[i].d, &a[i].l);
        scanf("%d", &d);
        a[n + 1].d = d;
        n += 2;
        sort(a, a + n, cmp);
        memset(f, -1, sizeof(f));
        printf("Case #%d: ", cas);
        if (dfs(1, 0)) printf("YES\n");
        else printf("NO\n");
    }
    
    
    return 0;
}
