#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=1000+10;
int n,g[maxn][maxn],list[maxn];
bool mark[maxn],ans;
void init()
{
	scanf("%d",&n);
	for (int i=0;i<n;i++)
		g[i][0]=0;
	int k,x;
	for (int i=0;i<n;i++)
		for (scanf("%d",&k);k;k--)
		{
			scanf("%d",&x);
			g[i][++g[i][0]]=x-1;
		}
}
bool bfs(int s)
{
	int t=1;
	list[0]=s;
	for (int i=0;i<n;i++)
		mark[i]=true;
	mark[s]=false;
	int u,v;
	for (int h=0;h<t;h++)
	{
		u=list[h];
		for (int i=1;i<=g[u][0];i++)
		{
			v=g[u][i];
			if (mark[v])
			{
				mark[v]=false;
				list[t++]=v;
			}
			else
				return true;
		}
	}
	return false;
}
void solve()
{
	ans=false;
	for (int i=0;i<n;i++)
		if (bfs(i))
		{
			ans=true;
			break;
		}
}
void out(int t)
{
	printf("Case #%d: ",t);
	if (ans)
		printf("Yes\n");
	else
		printf("No\n");
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		init();
		solve();
		out(i);
	}
	return 0;
}
