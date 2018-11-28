#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <set>
#include <queue>
#include <assert.h>
using namespace std;
#define N 3000
#define M 3000
bool used[M];
int right[M];
vector<int> belong[N];
int deg[M];
bool malt[N];
bool visited[N];
bool sat[M];
bool check(int n,int m)
{
	memset(sat,false,sizeof(bool)*m);
	for(int i=0;i<n;i++)
	{
		if(malt[i])continue;
		for(int j=0;j<belong[i].size();j++)
			sat[belong[i][j]]=true;
	}
	for(int i=0;i<m;i++)
		if(right[i]!=-1&&malt[right[i]])
			sat[i]=true;
	for(int i=0;i<m;i++)
		if(!sat[i])return false;
	return true;
}
int main()
{
	int t,n,m,ca=1;
	for(scanf("%d",&t);t--;)
	{
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)belong[i].clear();
		for(int i=0;i<m;i++)
		{
			right[i]=-1;
			deg[i]=0;
			int d;
			scanf("%d",&d);
			for(int j=0;j<d;j++)
			{
				int w,m;
				scanf("%d %d",&w,&m);
				w--;
				if(m==1)right[i]=w;
				else deg[i]++,belong[w].push_back(i);
			}
		}
		memset(malt,false,sizeof(bool)*n);
		memset(used,false,sizeof(bool)*m);
		memset(visited,false,sizeof(bool)*n);
		queue<int> qq;
		for(int i=0;i<m;i++)
			if(deg[i]==0&&!visited[right[i]])
				qq.push(right[i]),assert(right[i]!=-1),malt[right[i]]=true,
					visited[right[i]]=used[i]=true;
		bool f=true;
		while(qq.size())
		{
			int v=qq.front();qq.pop();
			for(int i=0;i<belong[v].size();i++)
			{
				int u=belong[v][i];
				assert(u>=0&&u<m);
				assert(!used[u]);
				if(used[u])continue;
				deg[u]--;
				assert(deg[u]>=0);
				if(deg[u]==0)
				{
					if(right[u]==-1)
					{
						f=false;
						goto end;
					}
					if(!malt[right[u]])
					{
						qq.push(right[u]);
						malt[right[u]]=true;
						used[u]=true;
					}
				}
			}
		}
end:
		printf("Case #%d:",ca++);
		if(!f)
		{
			puts(" IMPOSSIBLE");
			continue;
		}
		check(n,m);
		for(int j=0;j<n;j++)
			printf(" %d",malt[j]?1:0);
		puts("");
	}
	return 0;
}
