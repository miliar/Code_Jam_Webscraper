#include<stdio.h>
#include<memory.h>

long long dp[1010],tot;
int n1,i1,i,m,n,z,x,y,b[1010],j,a[1010];

int main()
{
    
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d %d %d %d %d",&n,&m,&x,&y,&z);
        for(i=0;i<m;i++)
        {
            scanf("%d",&b[i]);
        }    
        for(i=0;i<n;i++)
        {
            a[i]=b[i%m];
            b[i%m]=((long long)x*b[i%m]+(long long)y*(i+1))%z;
        }
        memset(dp,0,sizeof(dp));
        for(i=0;i<n;i++)
        {
            dp[i]=1;
            for(j=0;j<i;j++)
                if(a[i]>a[j])
                    dp[i]=(dp[i]+dp[j])%1000000007;
        }
        tot=0;
        for(i=0;i<n;i++)
        {
            tot=(tot+dp[i])%1000000007;
        }
        printf("Case #%d: %I64d\n",i1,tot);
    }    
    return 0;
}
