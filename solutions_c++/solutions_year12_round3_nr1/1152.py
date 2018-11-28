#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;

int first[1100],next[1210000],vv[1210000];
int vis[1100],d[1100];
int is[1100][1100];

void cpy(int a,int b,int n)
{
	for(int i=1;i<=n;i++)
		is[b][i]+=is[a][i];
}
bool bfs(int n)
{
	memset(is,0,sizeof(is));
	memset(vis,0,sizeof(vis));
	int i,j,u,v,e;
	queue<int>q;
	for(i=1;i<=n;i++)
		is[i][i]=1;
	for(i=1;i<=n;i++)if(!d[i])
		vis[i]=1,q.push(i);

	while(!q.empty())
	{
		u=q.front();q.pop();
		e=first[u];

		while(e)
		{
			v=vv[e];
			cpy(u,v,n);
			d[v]--;
			if(!d[v])
				q.push(v),vis[v]=1;
			e=next[e];
		}
	}
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)if(is[i][j]>1)
			return 1;
	return 0;
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,m,i,ii=0,j,u,v,e;

	scanf("%d",&t);

	while(t--)
	{
		scanf("%d",&n);
		memset(first,0,sizeof(first));
		e=2;
		memset(d,0,sizeof(d));
		for(i=1;i<=n;i++)
		{
			int k;
			scanf("%d",&k);
			while(k--)
			{
				scanf("%d",&v);
				next[e]=first[v],vv[e]=i,first[v]=e++;
				d[i]++;
			}
		}
		bool iss=bfs(n);
		printf("Case #%d: ",++ii);
		if(iss)
			printf("Yes\n");
		else
			printf("No\n");
	}
}