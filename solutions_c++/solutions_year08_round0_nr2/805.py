#include<iostream>
using namespace std;
const int MAXN=201;
int qa[101],qb[101],za[101],zb[101];
int nx,ny,m,cx[MAXN],cy[MAXN];
bool g[MAXN][MAXN],sy[MAXN];
int path (int u)
{
	for(int v=1;v<=ny;v++)
		if(g[u][v]&&sy[v]==false)
		{
			sy[v]=true;
			if(cy[v]==0||path(cy[v]))
			{
				cx[u]=v;
				cy[v]=u;
				return true;
			}
		}
	return false;
}
int MaximumMatch()
{
	int i,ret=0;
	memset(cx,0,4*MAXN);
	memset(cy,0,4*MAXN);
	for(i=1;i<=nx;i++)
		if(cx[i]==0)
		{
			memset(sy,0,MAXN);
			if(path(i))ret++;
		}
	return ret;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int n,cs,i,j,aa,bb,css,na,nb,a,b,c,d,del;
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d",&del);
		scanf("%d%d",&na,&nb);
		for(i=1;i<=na;i++)
		{
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			qa[i]=a*60+b;
			za[i]=c*60+d+del;
		}
		for(i=1;i<=nb;i++)
		{
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			qb[i]=a*60+b;
			zb[i]=c*60+d+del;
		}
		memset(g,0,MAXN*MAXN);
		for(i=1;i<=na;i++)
			for(j=1;j<=nb;j++)
			{
				if(za[i]<=qb[j])g[i][j+na]=true;
				if(zb[j]<=qa[i])g[na+j][i]=true;
			}
		nx=ny=na+nb;
		MaximumMatch();
		aa=bb=0;
		for(i=1;i<=na;i++)
			if(cy[i]==0)aa++;
		for(i=1;i<=nb;i++)
			if(cy[i+na]==0)bb++;
		printf("Case #%d: %d %d\n",css,aa,bb);
	}
	return 0;
}
