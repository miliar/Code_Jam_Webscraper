#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 210;

struct Node
{
	int p[30];
}node[N];

int n,k;

bool operator < (const Node &a,const Node &b)
{
	return a.p[0]>b.p[0];
}

int nx,ny;			//二部图两部分的顶点数
bool graph[N][N];		//二部图
bool visited[N];		//用于dfs，记录y部顶点
int match[N];			//匹配结果

int FindPath(int u)
{
	int v;
	for(v=0;v<ny;v++)
	{
		if(!visited[v] && graph[u][v])
		{
			visited[v]=1;
			if(match[v]<0 || FindPath(match[v]))
			{
				match[v]=u;
				return 1;
			}
		}
	}
	return 0;
}

int MaxMatch()
{
	int i,ans=0;
	memset(match,-1,sizeof(match));
	for(i=0;i<nx;i++)
	{
		memset(visited,0,sizeof(visited));
		ans+=FindPath(i);
	}
	return ans;
}

bool inter(int p,int q)
{
	int i;
	for(i=0;i<k;i++)
		if(node[p].p[i]<=node[q].p[i])
			return true;
	return false;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ca=1;
	int i,j;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)
			for(j=0;j<k;j++)
				scanf("%d",&node[i].p[j]);
		sort(node,node+n);
		memset(graph,0,sizeof(graph));
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				if(!inter(i,j))
					graph[i][j]=1;
		//for(i=0;i<n;i++)
		//	graph[i][i]=1;
		nx=ny=n;
		printf("Case #%d: %d\n",ca++,n-MaxMatch());
	}
	return 0;
}