#include <cstdio>
#include <cstring>
#define oo 1000000005
#define CheckOut(x,y) (x<1||x>N||y<1||y>M)
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
int g[105][105],g0[105][105],tot,N,M;
inline void Dfs(int hx,int hy)
{
	if (g[hx][hy])
		return;
	int h=oo,x=0,y=0;
	for (int k=0;k<4;++k)
	{
		int x1=hx+dx[k],y1=hy+dy[k];
		if (CheckOut(x1,y1))
			continue;
		if (g0[x1][y1]<h)
			h=g0[x1][y1],x=x1,y=y1;
	}
	if (h>=g0[hx][hy])
		g[hx][hy]=++tot;
	else 
	{
		Dfs(x,y);
		g[hx][hy]=g[x][y];
	}
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int Tests;scanf("%d",&Tests);
	for (int T=1;T<=Tests;++T)
	{
		tot=0;
		memset(g,0,sizeof(g));
		printf("Case #%d:\n",T);
		scanf("%d%d",&N,&M);
		int i,j;
		for (i=1;i<=N;++i)
		for (j=1;j<=M;++j)
			scanf("%d",&g0[i][j]);
		for (i=1;i<=N;++i)
		for (j=1;j<=M;++j)
		if (!g[i][j])
			Dfs(i,j);
		for (i=1;i<=N;++i,puts(""))
		for (j=1;j<=M;++j)
		if (j!=M)
			printf("%c ",g[i][j]+96);
		else 
			printf("%c",g[i][j]+96);
	}
	return 0;
}
