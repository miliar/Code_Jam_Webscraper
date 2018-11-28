// gcj A
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
const int MAX=100+10;

int N;
int dp[MAX][MAX][MAX];
int abs(int a) {return a>0?a:-a;}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		scanf("%d",&N);
		memset(dp,-1,sizeof(dp));
		dp[0][1][1]=0;
		for(int i=1;i<=N;i++)
		{
			char ch;
			int dd;
			scanf(" %c%d",&ch,&dd);
			if(ch=='O')
			{
				for(int j=1;j<=100;j++)
				{
					for(int k=1;k<=100;k++)
					{
						if(dp[i-1][j][k]!=-1)
						{
							int L=abs(j-dd)+1;
							int ti=dp[i-1][j][k]+abs(j-dd)+1;
							for(int x=max(1,k-L);x<=min(100,k+L);x++) if(dp[i][dd][x]==-1||dp[i][dd][x]>ti) dp[i][dd][x]=ti;
						}
					}
				}
			}
			else
			{
				for(int j=1;j<=100;j++)
				{
					for(int k=1;k<=100;k++)
					{
						if(dp[i-1][j][k]!=-1)
						{
							int L=abs(k-dd)+1;
							int ti=dp[i-1][j][k]+abs(k-dd)+1;
							for(int x=max(1,j-L);x<=min(100,j+L);x++) if(dp[i][x][dd]==-1||dp[i][x][dd]>ti) dp[i][x][dd]=ti;
						}
					}
				}
			}
		}
		
		int ans=0x1fffffff;
		for(int i=1;i<=100;i++)
		{
			for(int j=1;j<=100;j++)
			{
				if(dp[N][i][j]!=-1) ans=min(ans,dp[N][i][j]);
			}
		}
		printf("Case #%d: %d\n",++CN,ans);
	}
	
	return 0;
}
