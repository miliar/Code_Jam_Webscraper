#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
using namespace std;
int n,m;
set<int> adj[100];
set<set<int> > rooms;
int color;
int colors[100];
bool vis[100];
bool verify()
{
	set<set<int> >::iterator it;
	for(it=rooms.begin();it!=rooms.end();it++)
	{
		const set<int>& t=(*it);
		memset(vis,0,sizeof(vis));
		set<int>::iterator it2;
		for(it2=t.begin();it2!=t.end();it2++)
			vis[colors[*it2]]=true;
		for(int i=0;i<color;i++)
			if(!vis[i])
				return false;
	}
	return true;
}
bool dfs(int a)
{
	if(a==n)
		return verify();
	else
	{
		for(int i=0;i<color;i++)
		{
			colors[a]=i;
			if(dfs(a+1))
				return true;
		}
	}
	return false;
}
int sol[100];
int begin[100],end[100];
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		rooms.clear();
		for(int i=0;i<100;i++)
			adj[i].clear();
		scanf("%d%d",&n,&m);
		for(int i=0;i<m;i++)
			scanf("%d",&begin[i]);
		for(int i=0;i<m;i++)
			scanf("%d",&end[i]);
		for(int i=0;i<m;i++)
		{
			int a,b;
			a=begin[i];
			b=end[i];
			a--,b--;
			adj[a].insert(b);
			adj[b].insert(a);
		}
		for(int i=0;i<n;i++)
		{
			adj[i].insert((i+1)%n);
			adj[(i+1)%n].insert(i);
		}
		for(int i=0;i<n;i++)
		{
			set<int>::iterator it2;
			for(it2=adj[i].begin();it2!=adj[i].end();it2++)
			{
				if((*it2)==((i+1)%n))
					continue;
				//printf("new room\n");
				set<int> t;
				//printf("%d\n",i);
				t.insert(i);
				int p=i,a=(*it2);
				while(a!=i)
				{
					//printf("%d\n",a);
					t.insert(a);
					set<int>::iterator it=adj[a].upper_bound(p);
					if(it==adj[a].end())
						it=adj[a].begin();
					p=a;
					a=(*it);
				}
				rooms.insert(t);
			}
		}
		for(color=1;color<=n;color++)
		{
			if(!dfs(0))
				break;
			memcpy(sol,colors,sizeof(sol));
		}
		printf("Case #%d: %d\n",tn,color-1);
		for(int i=0;i<n;i++)
		{
			if(i)
				putchar(' ');
			printf("%d",sol[i]+1);
		}
		printf("\n");
	}
}
