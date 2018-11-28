#include <iostream>
using namespace std;
int D,I,M,N;
int dp[110][260];
int num[110];
int main()
{
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
	    scanf("%d %d %d %d",&D,&I,&M,&N);
	    for(int i=1;i<=N;i++)
	    {
	        scanf("%d",&num[i]);
        }
        int ans;
        for(int i=0;i<=255;i++)
        {
            dp[0][i]=0;
        }
        for(int i=1;i<=N;i++)
        {
            int now=num[i];
            for(int j=0;j<=255;j++)
            {
                dp[i][j]=dp[i-1][j]+D;
            }
            for(int j=0;j<=255;j++)
            {
                for(int end=0;end<=255;end++)
                {
                    int cha=abs(end-j);
                    if(M>0)
                    {
                        int ig;
                        if(cha>M)
                            ig=(cha-1)/M;
                        else
                            ig=0;
                    dp[i][end]=min(dp[i][end],dp[i-1][j]+(abs(now-end)+I*ig));
                    }
                    else if(end==j)
                    {
                        dp[i][end]=min(dp[i][end],dp[i-1][j]+abs(now-end));
                    }
                }
            }
        }
        ans=100000000;
        for(int i=0;i<=255;i++)
        {
            ans=min(ans,dp[N][i]);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
