#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

#define NV 55
#define NM 10000
#define CLR(arr,v) memset(arr,v,sizeof(arr))

int h[NV],num[NM],nex[NM],vis[NM],H[NV],Num[NM],Nex[NM],Vis[NM],pos;
bool vist[NV];

void clear()
{
	pos = 0;
	CLR(h,-1);
	CLR(H,-1);
}

void add(int u,int v)
{
	num[pos] = v;
	nex[pos] = h[u];
	h[u] = pos;

	Num[pos] = u;
	Nex[pos] = H[v];
	H[v] = pos++;
}

bool Dfs2(int); 
bool Dfs1(int x)
{
	if(Dfs2(x)) return true;
	vist[x] = true;
	for(int i = h[x];i != -1;i = nex[i])
	{
		vis[i] = true;
		if(Dfs1(num[i])) return true;
		vis[i] = false;
	}
	return false;
}

bool Dfs2(int x)
{
	if(vist[x]) return true;
	for(int i = H[x];i != -1;i = Nex[i])
	{
		if(!vis[i])
		{
			if(Dfs2(Num[i])) return true;
		}
	}
	return false;
}

int main()
{
	int T,k = 1;
	scanf("%d",&T);
	while(T--)
	{
		clear();
		int n,t,e;
		scanf("%d",&n);
		for(int i = 1;i <= n;++i)
		{
			scanf("%d",&t);
			for(int j = 0;j < t;++j)
			{
				scanf("%d",&e);
				add(e,i);
			}
		}
		bool flag = false;
		for(int i = 1;i <= n;++i)
		{
			CLR(vis,0);
	        CLR(Vis,0);
	        CLR(vist,0);
			if(Dfs1(i)) 
			{
				flag = true;
				break;
			}
		}
		printf("Case #%d: ",k++);
		printf(flag ?"Yes\n":"No\n");
	}
}