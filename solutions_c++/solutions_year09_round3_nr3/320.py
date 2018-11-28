#include<iostream>
#include<string>
#include<cmath>
#include<sstream>
using namespace std;

int p[10010];
int re[200];
int dp[1<<10];
int flag[200];
int n,m;
int rel(int ind)
{
	int sum=0;
	int a=re[ind];
	int i,j;
	for(i=a-1;i>0;i--)
	{
		for(j=0;j<m;j++)
			if(flag[j]==1&&re[j]==i)
				break;
		if(j>=m)
			sum++;
		else
			break;
	}
	for(i=a+1;i<=n;i++)
	{
		for(j=0;j<m;j++)
			if(flag[j]==1&&re[j]==i)
				break;
		if(j>=m)
			sum++;
		else
			break;
	}
	return sum;
}
void solve()
{
	memset(dp,0,sizeof(dp));
	int i,j,k;
	for(i=0;i<(1<<m);i++)
	{
		memset(flag,0,sizeof(flag));
		for(j=0;j<m;j++)
			if((i&(1<<j))>0)
				break;
		if(j>=m)
			continue;
		for(j=0;j<m;j++)
			if((i&(1<<j))>0)
				flag[j]=1;
		for(j=0;j<m;j++)
		{
			if(flag[j]==1)
			{
				flag[j]=0;
				if(dp[i]==0||(dp[i]>rel(j)+dp[i-(1<<j)]))
					dp[i]=rel(j)+dp[i-(1<<j)];
				flag[j]=1;
			}
		}
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int cas=1;
	int t,i,j,k;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas);
		cas++;
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
			scanf("%d",&re[i]);
		memset(p,0,sizeof(p));
		solve();
		printf("%d\n",dp[(1<<m)-1]);
	}
	return 0;
}
