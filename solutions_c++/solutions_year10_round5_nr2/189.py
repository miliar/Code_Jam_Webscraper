#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#define pp 1000000001
using namespace std;
long long dp[10001];
int a[101];
int i,j,k,n,m;
int main()
{
    int q;
    int cas;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("bbb3.out","w",stdout);
    scanf("%d",&cas);
    long long l;
    for (q=1;q<=cas;q++)
    {
        scanf("%lld%d",&l,&n);
        for (i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        for (i=1;i<=10000;i++)
        dp[i]=100001;
        dp[0]=0;
        for (i=1;i<=10000;i++)
        {
            for (j=1;j<=n;j++)
            if (i>=a[j])
            dp[i]=min(dp[i],dp[i-a[j]]+1);
        }
        long long xxoo=(long long )pp*pp;
        bool flag=false;
        for (i=1;i<=10000;i++)
        {
            if (dp[l%i]<=l%i&&dp[i]<=i)
            {flag=true;xxoo=min(xxoo,dp[l%i]+l/i*dp[i]);}
        }
        if (!flag)
            printf("Case #%d: IMPOSSIBLE\n",q);
            else
        printf("Case #%d: %lld\n",q,xxoo);
    }
}
            
            
