#include"stdio.h"
#include"stdlib.h"
#include"math.h"
int t,T,i,j,k,n,arr[20],dp[2500000],prev[2500000];
int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        dp[0]=t;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&arr[i]);
            for(j=2000000;j>=0;j--)
                if(dp[j]==t)
                {
                    if(dp[j+arr[i]]==t)
                    {
                        printf("Case #%d:\n",t);
                        for(k=j+arr[i];k;k=prev[k]) printf("%d ",k-prev[k]); printf("\n");
                        printf("%d ",arr[i]);
                        for(k=j;k;k=prev[k]) printf("%d ",k-prev[k]); printf("\n");
                        break;                        
                    }
                    else
                    {
                        dp[j+arr[i]]=t;
                        prev[j+arr[i]]=j;
                    }
                }
            if(j>=0) break;
        }
        if(i<=n) for(i++;i<=n;i++) scanf("%d",&j);
        else printf("Case #%d:\nImpossible\n",t);
    }
    //scanf(" ");
}
