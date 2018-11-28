#include<iostream>
using namespace std;
__int64 dp[105][105];

int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
//	freopen("c.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	int ca=1;
	while(zu--)
	{
		int i,j,w,h,r;
		cin>>h>>w>>r;
		memset(dp,-1,sizeof(dp));
		for(i=0;i<r;i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			dp[x][y] = 0;
		}
		for(i=1;i<=w-1;i++)
			dp[h][i] = 0;
		if(dp[h][w]==-1)
			dp[h][w] = 1;
		for(i=1;i<=w-2;i++)
			if(dp[h-1][i]==-1)
				dp[h-1][i] = dp[h][i+2];
		for(;i<=w;i++)
			dp[h-1][i] = 0;
		for(i=h-2;i>=1;i--)
		{
			for(j=1;j<=w-2;j++)
				if(dp[i][j])
					dp[i][j] = (dp[i+1][j+2]+dp[i+2][j+1])%10007;
			if(dp[i][j])
				dp[i][j] = dp[i+2][j+1];
			dp[i][w] = 0;
		}
	/*	for(i=1;i<=h;i++)
		{
			for(j=1;j<=w;j++)
				cout<<dp[i][j]<<' ';
			cout<<endl;
		}*/
		printf("Case #%d: %I64d\n",ca++,dp[1][1]%10007);
	}
}
