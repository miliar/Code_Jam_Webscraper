#include <stdio.h>
#include <algorithm>
using namespace std;
typedef long long LL;
long long d[10010],l[10010],dp[10010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%I64d%I64d",&d[i],&l[i]);
        LL D;
        scanf("%I64d",&D);
        dp[0]=2*d[0];
        for (int i=1;i<n;i++)
        {
            dp[i]=-1;
            for (int j=0;j<i;j++)
            {
                if (dp[j]>=d[i])
                {
                    LL dis=min(l[i],d[i]-d[j]);
                    dp[i]=max(dp[i],d[i]+dis);
                }
            }
        }
        bool ok=false;
        for (int i=0;i<n;i++)
            if (dp[i]>=D) ok=true;
        if (ok) printf("Case #%d: YES\n",ii);
        else printf("Case #%d: NO\n",ii);
    }
    return 0;
}
