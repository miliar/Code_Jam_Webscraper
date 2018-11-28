#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

int s,n,p,z[101],ans;

void dfs(int now,int rest,int sum)
{
	if (now>n) 
	{
		if (rest) return;
		ans=max(ans,sum);
		return;
	}
	if (n-now+1<rest) return;
	if (n-now+1+sum<=ans) return;
	if (z[now]==0)
	{
		if (z[now]>=p) dfs(now+1,rest,sum+1);
		else dfs(now+1,rest,sum);
		return;
	}
	if (z[now]==1)
	{
		if (z[now]>=p) dfs(now+1,rest,sum+1);
		else dfs(now+1,rest,sum);
		return;
	}
	int div=z[now] / 3;
	if (z[now] % 3==0)
	{
		if (div>=p) dfs(now+1,rest,sum+1);
		else dfs(now+1,rest,sum);
		if (div+1>=p && rest>0) dfs(now+1,rest-1,sum+1);
		else dfs(now+1,rest-1,sum);
	}
	else
	{
		if (z[now] % 3==1)
		{
			if (div+1>=p) dfs(now+1,rest,sum+1);
			else dfs(now+1,rest,sum);
			if (div+1>=p && rest>0) dfs(now+1,rest-1,sum+1);
			else dfs(now+1,rest-1,sum);
		}
		else
		{
			if (div+1>=p) dfs(now+1,rest,sum+1);
			else dfs(now+1,rest,sum);
			if (div+2>=p && rest) dfs(now+1,rest-1,sum+1);
			else dfs(now+1,rest-1,sum);
		}
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int a=1;a<=t;a++)
	{
		scanf("%d%d%d",&n,&s,&p);
		for (int b=1;b<=n;b++)
			scanf("%d",&z[b]);
		ans=0;
		dfs(1,s,0);
		printf("Case #%d: %d\n",a,ans);
	}
	return 0;
}
