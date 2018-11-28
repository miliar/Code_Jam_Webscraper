#include <iostream>
#include <cmath>
#include <map>
using namespace std;
int dp[2][1024000];
int main()
{
   // printf("%d\n",1<<1);
 freopen("c1.txt","r",stdin);
   freopen("c1out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int n;
        int num[1024];
        scanf("%d",&n);
        int res=0;
        int tar=0;
        int min1=10000000;
        int sum=0;
        dp[0][0]=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&num[i]);
            min1=min(min1,num[i]);
            sum+=num[i];
            res^=num[i];
            tar|=num[i];
        }
        printf("Case #%d: ",t);
        if(res!=0)
        {
            printf("NO\n");
            continue;
        }
        int max1=0;
        int from=1,to=0;
    /*    for(int i=0;i<n;i++)
        {
            from^=1;
            to^=1;
            for(int j=0;j<=tar;j++)
            {
                if(dp[from][j]!=-1)
                {
                    if(dp[to][j^num[i]]<dp[from][j]+num[i])
                    {
                        dp[to][j^num[i]]=dp[from][j]+num[i];
                        max1=max(max1,dp[to][j^num[i]]);
                       // printf("%d %d %d %d\n",j,num[i],j^num[i],dp[j]+num[i]);
                    }
                }
            }
        }  */
        printf("%d\n",sum-min1);

    }
	return 0;
}
