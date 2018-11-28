#include<stdio.h>
#include<string.h>

int p,inf=1<<29;

int dp[15][2000][15];

int min(int a,int b)
{
	return a<b?a:b;
}

int max(int a,int b)
{
	return a>b?a:b;
}

inline int solve()
{
	int i,j,k,u,v,cost,idx=0;
	
	for(k=p;k>=1;k--)
	{
		for(i=0;i<(1<<(k-1));i++)
		{
			scanf("%d",&cost);
			//printf("cost=%d\n",cost);
			
			for(u=0;u<=p;u++)
			if(dp[k][2*i][u]!=inf)
			for(v=0;v<=p;v++)
			if(dp[k][2*i+1][v]!=inf)
			{
				//printf("%d %d\n",);
				
				int num=max(u,v);
				
				dp[k-1][i][num]=min(dp[k-1][i][num],dp[k][2*i][u]+dp[k][2*i+1][v]);
				if(num>=1)
				dp[k-1][i][num-1]=min(dp[k-1][i][num-1],dp[k][2*i][u]+dp[k][2*i+1][v]+cost);
			}
		}
	}
	
//	for(k=p;k>=0;k--)
//	{
//		for(i=0;i<(1<<k);i++)
//		{
//			printf("(");
//			for(j=0;j<=p;j++)
//			{
//				if(dp[k][i][j]!=inf)printf("%3d,",dp[k][i][j]);
//				else                printf("inf,");
//			}
//			printf(") ");
//		}
//		puts("");
//	}
	
	return  dp[0][0][0];
	//while(1);
}

int main()
{
	//freopen("b-big.in","r",stdin);
//	freopen("b-bigout.txt","w",stdout);
	int t,tc=1;
	scanf("%d",&t);
	while(t--)
	{
		  scanf("%d",&p);
		  //printf("%d\n",p);
		  
		  int i,j,k,x;
		  
		  memset(dp,-1,sizeof(dp));
		  
		  for(i=0;i<=p;i++)
		  for(j=0;j<=p;j++)
		  for(k=0;k<(1<<p);k++)
		  {
			  dp[i][k][j]=inf;
		  }
		  
		  for(i=0;i<(1<<p);i++)
		  {
			  scanf("%d",&x);
			  dp[p][i][p-x]=0;
			  //printf("x=%d\n",x);
		  }
		  printf("Case #%d: %d\n",tc++,solve());
	}
//	while(1);
}
