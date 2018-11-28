#include <cstdio>
#include <memory>
#define oo 10005
struct Tnode
{
	bool flag;
	int f[2],work;
}	f[oo];
int N,Test,Case;
int v;

inline void renew(int& a,int x,int y,int delta)
{
	if (x<0 || y<0) return;
	if (a<0) a=x+y+delta;
	else a<?=x+y+delta;
}

inline void DP(int u)
{
	if (u>(N>>1))
	{
		f[u].f[f[u].work]=0;
		return;
	}
	
	DP(u<<1);
	DP((u<<1)+1);

	if (f[u].work)
	{
		renew(f[u].f[1],f[u<<1].f[1],f[(u<<1)+1].f[1],0);
		if (f[u].flag) renew(f[u].f[1],f[u<<1].f[1],f[(u<<1)+1].f[0],1);
		if (f[u].flag) renew(f[u].f[1],f[u<<1].f[0],f[(u<<1)+1].f[1],1);
		
		renew(f[u].f[0],f[u<<1].f[1],f[(u<<1)+1].f[0],0);
		renew(f[u].f[0],f[u<<1].f[0],f[(u<<1)+1].f[1],0);
		renew(f[u].f[0],f[u<<1].f[0],f[(u<<1)+1].f[0],0);
	}
	else{
		renew(f[u].f[1],f[u<<1].f[1],f[(u<<1)+1].f[1],0);
		renew(f[u].f[1],f[u<<1].f[1],f[(u<<1)+1].f[0],0);
		renew(f[u].f[1],f[u<<1].f[0],f[(u<<1)+1].f[1],0);
		
		renew(f[u].f[0],f[u<<1].f[0],f[(u<<1)+1].f[0],0);
		if (f[u].flag) renew(f[u].f[0],f[u<<1].f[1],f[(u<<1)+1].f[0],1);
		if (f[u].flag) renew(f[u].f[0],f[u<<1].f[0],f[(u<<1)+1].f[1],1);
	}
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	
	for (scanf("%d",&Test);Test--;Test)
	{
		scanf("%d%d",&N,&v);
		memset(f,-1,sizeof f);
		for (int i=1;i<=N;++i)
		{
			int tmp;
			scanf("%d",&f[i].work);
			if (i<=(N>>1))
			{
				scanf("%d",&tmp);
				f[i].flag=tmp==1;
			}
			else f[i].flag=false;
		}
		
		DP(1);
		if (f[1].f[v]<0) printf("Case #%d: IMPOSSIBLE\n",++Case);
		else printf("Case #%d: %d\n",++Case,f[1].f[v]);
	}
	return 0;
}
