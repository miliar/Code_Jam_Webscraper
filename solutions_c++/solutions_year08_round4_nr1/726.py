#include<iostream>
using namespace std;
int dp[10001][2];
struct node
{
	bool ff;
	bool ch;
}nn[10001];
int main()
{
	int n,m,i,flag=1;
	bool v;
	cin>>n;
	while(n--)
	{
		cin>>m>>v;
		for(i=1;i<=(m-1)/2;i++)cin>>nn[i].ff>>nn[i].ch;
		for(;i<=m;i++)cin>>nn[i].ff;
		for(i=m;i>=1;i--)
		{
			if(i>(m-1)/2)
			{
				if(nn[i].ff)
				{
					dp[i][0]=100000000;
					dp[i][1]=0;
				}
				else
				{
					dp[i][0]=0;
					dp[i][1]=100000000;
				}
			}
			else
			{
				if(nn[i].ff)
				{
					int min=100000000;
					if(dp[i<<1][0]+dp[(i<<1)+1][0]<min)min=dp[i<<1][0]+dp[(i<<1)+1][0];
					if(dp[i<<1][0]+dp[(i<<1)+1][1]<min)min=dp[i<<1][0]+dp[(i<<1)+1][1];
					if(dp[i<<1][1]+dp[(i<<1)+1][0]<min)min=dp[i<<1][1]+dp[(i<<1)+1][0];
					dp[i][0]=min;
					min=100000000;
					if(dp[i<<1][1]+dp[(i<<1)+1][1]<min)min=dp[i<<1][1]+dp[(i<<1)+1][1];
					if(nn[i].ch)
					{
						if(dp[i<<1][0]+dp[(i<<1)+1][1]+1<min)min=dp[i<<1][0]+dp[(i<<1)+1][1]+1;
						if(dp[i<<1][1]+dp[(i<<1)+1][0]+1<min)min=dp[i<<1][1]+dp[(i<<1)+1][0]+1;
					}
					dp[i][1]=min;
				}
				else
				{
					int min=100000000;
					if(dp[i<<1][1]+dp[(i<<1)+1][1]<min)min=dp[i<<1][1]+dp[(i<<1)+1][1];
					if(dp[i<<1][0]+dp[(i<<1)+1][1]<min)min=dp[i<<1][0]+dp[(i<<1)+1][1];
					if(dp[i<<1][1]+dp[(i<<1)+1][0]<min)min=dp[i<<1][1]+dp[(i<<1)+1][0];
					dp[i][1]=min;
					min=100000000;
					if(dp[i<<1][0]+dp[(i<<1)+1][0]<min)min=dp[i<<1][0]+dp[(i<<1)+1][0];
					if(nn[i].ch)
					{
						if(dp[i<<1][0]+dp[(i<<1)+1][1]+1<min)min=dp[i<<1][0]+dp[(i<<1)+1][1]+1;
						if(dp[i<<1][1]+dp[(i<<1)+1][0]+1<min)min=dp[i<<1][1]+dp[(i<<1)+1][0]+1;
					}
					dp[i][0]=min;
				}
			}
		}
		cout<<"Case #"<<flag++<<": ";
		if(dp[1][v]<100000000)cout<<dp[1][v]<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}