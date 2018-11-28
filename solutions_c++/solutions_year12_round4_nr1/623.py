#include <stdio.h>
#include <iostream>
using namespace std;

#define MAXN (10000+10)

int t, n, d[MAXN], l[MAXN], s, f[MAXN];

void doit()
{
    int tmp, i, k, now = 1, lg = d[1]+d[1];

    for (int i = 1;i <= n;++i) f[i] = 0;
    f[1] = d[1]*2; k = 2;
    for (int i = 1;i < n;++i)
    {
        while (k <= n && f[i] >= d[k])
        {
            f[k] = d[k] + min(l[k],d[k]-d[i]);
            ++k;
        }
    }
    for (int i = 1;i <= n;++i)
        if (f[i] >= s)
        {
                printf("YES\n");
                return;
        }
    printf("NO\n");
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    for (int w = 1;w <= t;++w)
    {
        scanf("%d",&n);
        for (int i = 1;i <= n;++i) scanf("%d%d",&d[i],&l[i]);
        scanf("%d",&s);
        printf("Case #%d: ",w);
        doit();
    }
}
