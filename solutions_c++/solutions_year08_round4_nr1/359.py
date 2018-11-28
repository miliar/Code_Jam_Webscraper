#include<stdio.h>

int val[10002],x[10002],y[10002];
int dp[10002][2];

int ans,M,V;

inline int MIN(int a,int b)
{
	if(a>b) a=b;
	if(a>100000000) a=100000000;
	return a;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T,ks,i,j,k,a,b;

	scanf("%d",&T);

	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d",&M,&V);

		for(i=1;i<=(M-1)/2;i++)
			scanf("%d%d",&x[i],&y[i]);
		for(j=1,k=(M-1)/2+1;j<=(M+1)/2;j++,k++)
		{
			scanf("%d",&val[k]);
			dp[k][val[k]]=0;
			dp[k][1-val[k]]=100000000;
		}

		for(i=(M-1)/2;i>=1;i--)
		{
			a=2*i;
			b=2*i+1;

//			if(y[i]==0) //unchangable
			{
				if(x[i]==1) //AND
				{
					dp[i][0]=MIN(dp[a][0]+dp[b][0],MIN(dp[a][0]+dp[b][1],dp[a][1]+dp[b][0]));
					dp[i][1]=dp[a][1]+dp[b][1];
				}
				else
				{
					dp[i][1]=MIN(dp[a][1]+dp[b][1],MIN(dp[a][0]+dp[b][1],dp[a][1]+dp[b][0]));
					dp[i][0]=dp[a][0]+dp[b][0];
				}
			}
//			else by changing

			if(y[i]==1)
			{
				if(x[i]==1) //make it or
				{
					dp[i][1]=MIN(MIN(dp[a][1]+dp[b][1],MIN(dp[a][0]+dp[b][1],dp[a][1]+dp[b][0]))+1,dp[i][1]);
					dp[i][0]=MIN(dp[a][0]+dp[b][0]+1,dp[i][0]);
				}
				else //make it and
				{
					dp[i][0]=MIN(dp[i][0],MIN(dp[a][0]+dp[b][0],MIN(dp[a][0]+dp[b][1],dp[a][1]+dp[b][0]))+1);
					dp[i][1]=MIN(dp[i][1],dp[a][1]+dp[b][1]+1);
				}
			}


		}

		ans=dp[1][V];

		if(ans>M) printf("Case #%d: IMPOSSIBLE\n",ks);
		else printf("Case #%d: %d\n",ks,ans);


	}

	return 0;
}