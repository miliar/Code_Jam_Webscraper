#include<iostream>
#define MAXN 101
int nx,ny,m,cx[MAXN],cy[MAXN];
bool g[MAXN][MAXN],sy[MAXN];
int path(int u)
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
int d[101][101];
int main()
{
	freopen("c-large.in","r",stdin);
	freopen("c-large.out","w",stdout);
	int css,cs,a,ct,tp,k,i,j,n,m;
	char s[100];
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		memset(g,0,sizeof(g));
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&d[i][j]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				for(k=0;k<m;k++)
					if(d[i][k]>=d[j][k])break;
				if(k==m)g[i+1][j+1]=true;
			}
		nx=ny=n;
		printf("Case #%d: %d\n",css,n-MaximumMatch());
	}
	return 0;
}
