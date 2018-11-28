#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int C[1100];
int seq[1100];
int dp[1100][5];
int main(int argc,char* argv[])
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	
	int T;
	int n,l,h;
	int cas=1;
	scanf("%d",&T);
	while(T--)
	{
		int L,t,N;
		int lenC;
		scanf("%d%d%d%d",&L,&t,&N,&lenC);
		for(int i=0;i<lenC;i++)
			scanf("%d",&C[i]);
		int tail=0;
		for(int tt=1;tt<=N;tt++)
		{
			seq[tt]=C[tail++];
			tail%=lenC;
		}
		for(int i=0;i<=N;i++)
			for(int j=0;j<=L;j++)
				dp[i][j]=0x7fffffff;
		dp[0][0]=0;
	/*	for(int i=1;i<=N;i++)
			printf("%d ",seq[i]);
		printf("\n");
	*/	for(int i=0;i<N;i++)
		{
			for(int tt=0;tt<=L;tt++)
			{
				if(dp[i][tt]!=0x7fffffff)
				{
					dp[i+1][tt]=min(dp[i+1][tt],seq[i+1]*2+dp[i][tt]);
					if(dp[i][tt]>=t)
						dp[i+1][tt+1]=min(dp[i+1][tt+1],dp[i][tt]+seq[i+1]);
					else if(seq[i+1]*2+dp[i][tt]>=t)
					{
						dp[i+1][tt+1]=min(dp[i+1][tt+1],t+(seq[i+1]-(t-dp[i][tt])/2));
					}
				}

			}
		}
	/*	for(int tt=0;tt<=L;tt++)
		{
			for(int i=0;i<=N;i++)
				printf("%d ",dp[i][tt]);
			printf("\n");
		}*/
		int ans=dp[N][0];
		for(int i=0;i<=L;i++)
			ans=min(dp[N][i],ans);
		printf("Case #%d: %d\n",cas++,ans);
		
	}

	return 0;
}
