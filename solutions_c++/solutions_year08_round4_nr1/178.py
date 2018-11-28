#include<iostream>
using namespace std;
int a[50000];
int dp[50000][2];
int b[50000];
int x,m,n;
const int inf=20000;
void solve(int t)
{
	if(t>x)
	{
		dp[t][a[t]]=0;
		dp[t][1-a[t]]=inf;
		return;
	}
	solve(t*2);
	solve(t*2+1);
	if(b[t])
	{
		if(a[t])
		{
			dp[t][1]=min(inf,dp[t*2][1]+dp[t*2+1][1]);
			dp[t][0]=min(inf,min(dp[t*2][0]+dp[t*2+1][1],min(dp[t*2][1]+dp[t*2+1][0],dp[t*2][0]+dp[t*2+1][0])));
			dp[t][1]=min(dp[t][1],1+min(dp[t*2][0]+dp[t*2+1][1],min(dp[t*2][1]+dp[t*2+1][0],dp[t*2][1]+dp[t*2+1][1])));
			dp[t][0]=min(dp[t][0],1+dp[t*2][0]+dp[t*2+1][0]);
		}
		else
		{
			dp[t][0]=min(inf,dp[t*2][0]+dp[t*2+1][0]);
			dp[t][1]=min(inf,min(dp[t*2][0]+dp[t*2+1][1],min(dp[t*2][1]+dp[t*2+1][0],dp[t*2][1]+dp[t*2+1][1])));
			dp[t][0]=min(dp[t][0],1+min(dp[t*2][0]+dp[t*2+1][1],min(dp[t*2][1]+dp[t*2+1][0],dp[t*2][0]+dp[t*2+1][0])));
			dp[t][1]=min(dp[t][1],1+dp[t*2][1]+dp[t*2+1][1]);
		}
	}
	else
	{
		if(a[t])
		{
			dp[t][1]=min(inf,dp[t*2][1]+dp[t*2+1][1]);
			dp[t][0]=min(inf,min(dp[t*2][0]+dp[t*2+1][1],min(dp[t*2][1]+dp[t*2+1][0],dp[t*2][0]+dp[t*2+1][0])));
		}
		else
		{
			dp[t][0]=min(inf,dp[t*2][0]+dp[t*2+1][0]);
			dp[t][1]=min(inf,min(dp[t*2][0]+dp[t*2+1][1],min(dp[t*2][1]+dp[t*2+1][0],dp[t*2][1]+dp[t*2+1][1])));
		}
	}
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	int g=1;
	while(zu--)
	{
		scanf("%d%d",&m,&n);
		x=(m-1)/2;
		memset(dp,0x3f,sizeof(dp));
		memset(b,0,sizeof(b));
		for(int i=1;i<=m;i++)
		{
			if(i<=x)
				scanf("%d%d",a+i,b+i);
			else
				scanf("%d",a+i);
		}
		solve(1);
	//	for(int i=1;i<=5;i++)	cout<<dp[i][0]<<" "<<dp[i][1]<<endl;
		if(dp[1][n]==inf)
			printf("Case #%d: IMPOSSIBLE\n",g++);
		else
			printf("Case #%d: %d\n",g++,dp[1][n]);
	}

}
