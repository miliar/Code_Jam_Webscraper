#include <cstdio>
#include <cstring>

const int maxn = 101;

int x[maxn],v[maxn];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        int n,k,b,t;
        scanf("%d%d%d%d",&n,&k,&b,&t);
        for (int i = 1; i <= n; ++i)
            scanf("%d",&x[i]);
        for (int i = 1; i <= n; ++i)
            scanf("%d",&v[i]);
        int ans = 0,m = 0;
        for (int i = n; i > 0; --i)
        {
            if (b - x[i] <= t * v[i])
                m++;
            else
            {
                ans += k - m;
            }
            if (m == k)
                break;
        }
        if (k == 0)
            ans = 0;
        if (m < k)
            printf("Case #%d: IMPOSSIBLE\n",T);
        else printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
