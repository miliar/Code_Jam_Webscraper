#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#define _clr(a,b) (memset((a),(b),sizeof((a))));
#define print(cas) printf("Case #%d: ",(cas)++); 
#define inf 1<<25;
using namespace std;

int n,flag;
int vis[1005];
int src[1005],len;
vector<int >map[1005];
queue<int >q;

void init()
{
	_clr(vis,0);
	while(!q.empty())q.pop();
}

void bfs(int s)
{
	int temp,i;
	vis[s]=1;
	q.push(s);
	while(!q.empty()&&!flag)
	{
		temp=q.front();
		q.pop();
		for(i=0;i<map[temp].size();i++)
		{	
			if(!vis[map[temp][i]]){vis[map[temp][i]]=1;q.push(map[temp][i]);}
			else 
			{
				flag=1;
				break;
			}
		}
	}
}

int main()
{
	int cas=1,txt,i,x,y,j;
	freopen("1.in","r",stdin);
	freopen("3.txt","w",stdout);
	scanf("%d",&txt);
	while(txt--)
	{
		flag=0;
		len=0;
		for(i=0;i<1005;i++)map[i].clear();
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&x);
			if(!x)src[len++]=i;
			for(j=0;j<x;j++)
			{
				scanf("%d",&y);
				map[y].push_back(i);
			}
		}
		for(i=0;i<len&&!flag;i++)
		{
			init();
			bfs(src[i]);
		}
		print(cas);
		if(flag)puts("Yes");
		else puts("No");
	}
	return 0;
}

