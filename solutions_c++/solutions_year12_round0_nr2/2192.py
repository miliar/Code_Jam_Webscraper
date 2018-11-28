#include<stdio.h>
#include<string.h>

int dp[105][105],p;
int score[105];

int make(int now,int rem)
{
	if(now<0)
	{
		if(!rem)
			return 0;
		else
			return -1000000;
	}
	if(dp[now][rem]!=-1)
		return dp[now][rem];

	dp[now][rem] = 0;
	int m,got;
	if(rem && score[now]>=2)
	{
		m = score[now]/3 + 1 + (score[now]%3==2);
		got = (m>=p) + make(now-1,rem-1);
		if(got > dp[now][rem])
			dp[now][rem] = got;
	}
	
	
	m = (score[now]+2)/3;
	got = (m>=p) + make(now-1,rem);
	if(got > dp[now][rem])
		dp[now][rem] = got;
		
	return dp[now][rem];
}

int main()
{
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	int t,n,s,i,cs=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
			scanf("%d",&score[i]);

		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",++cs,make(n-1,s));
	}
	return 0;
}