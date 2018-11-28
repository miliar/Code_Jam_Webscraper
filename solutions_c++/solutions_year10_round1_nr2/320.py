#include<algorithm>
#include<cstdio>
using namespace std;
const int L=110;
const int inf=1000000000;
using namespace std;
int t,D,I,M,N,input[L],dp[L][256];

void init()
{
	for(int i=0;i<256;i++)
	{
		dp[1][i]=abs(input[1]-i);
		if( M && (input[1]!=i) )
            dp[1][i]=min(dp[1][i],((abs(input[1]-i)-1)/M+1)*I);

		dp[1][i]=min(dp[1][i],D+I);
	}
}
main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	
    int i,j,k,T,ans;
	
    scanf("%d",&T);
	while(T--)
	{
		t++;
		scanf("%d %d %d %d",&D,&I,&M,&N);
		for(i=1;i<=N;i++)
            scanf("%d",&input[i]);       
        
        init();
		for(i=2;i<=N;i++)
		{
			for(j=0;j<256;j++)
			{
				dp[i][j]=inf;
				dp[i][j]=min(dp[i][j],dp[i-1][j]+D);
				
                for(k=0;k<256;k++)
				{
					if(j!=k)
					{
						if(M)
							dp[i][j]=min(dp[i][j],dp[i-1][k]+(abs(j-k)-1)/M*I+min(abs(input[i]-j),D+I));
					}
					else 
					{
                        dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(input[i]-j));
                    }
				}
			}
		}
		
        ans=inf;
		for(i=0;i<256;i++)
			ans=min(ans,dp[N][i]);

		printf("Case #%d: %d\n",t,ans);
	}
}
