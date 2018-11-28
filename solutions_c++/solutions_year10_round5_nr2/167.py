#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXN 100
#define MAXP 100000
#define INFI 1000000000
#define INFM 1000000000000000001LL
using namespace std;

int b[MAXN+1],dp[MAXP+1];
long long l,m;
int n,g;

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int i,j,c,t;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%I64d %d",&l,&n);
        scanf("%d",&b[0]);
        g=b[0];
        for(j=1;j<n;j++)
        {
            scanf("%d",&b[j]);
            g=__gcd(g,b[j]);
        }
        printf("Case #%d: ",c+1);
        if(l%g!=0)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(j=0;j<n;j++)
        {
            b[j]=b[j]/g;
        }
        l=l/g;
        sort(b,b+n);
        fill(dp,dp+MAXP+1,INFI);
        dp[0]=0;
        for(i=1;i<=MAXP;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i>=b[j])
                {
                    dp[i]=min(dp[i],dp[i-b[j]]+1);
                }
            }
        }
        m=INFM;
        for(i=0;i<=MAXP;i++)
        {
            if(dp[i]<INFI)
            {
                for(j=0;j<n;j++)
                {
                    if((l-i)%b[j]==0)
                    {
                        m=min(m,dp[i]+(l-i)/b[j]);
                    }
                }
            }
        }
        if(m<INFM)
        {
            printf("%I64d\n",m);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
