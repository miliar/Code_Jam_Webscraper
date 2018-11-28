#include<iostream>
#define maxn 801
int cx[maxn],cy[maxn],lx[maxn],ly[maxn],nx,ny,match,g[maxn][maxn];
bool sx[maxn],sy[maxn];
int path (int u)
{ 
	sx[u]=true;
	for(int v=1;v<=ny;v++)
		if(g[u][v]==lx[u]+ly[v]&&!sy[v])
		{
			sy[v]=true;
			if(!cy[v]||path(cy[v]))
			{
				cx[u]=v;
				cy[v]=u;
				return true;
			}
		}
	return false;
}
void KuhnMunkres()
{ 
	int i,j,u,min;
	memset(lx,0,4*maxn);
	memset(ly,0,4*maxn);
	memset(cx,0,4*maxn);
	memset(cy,0,4*maxn);
	for(i=1;i<=nx;i++)
		for(j=1;j<=ny;j++)
			if(lx[i]<g[i][j])
				lx[i]=g[i][j];
	for(match=0,u=1;u<=nx;u++)
		if(!cx[u])
		{
			memset(sx,0,maxn);
			memset(sy,0,maxn);
			while(!path(u))
			{
				min=0x3fffffff;
				for(i=1;i<=nx;i++)
					if(sx[i])
						for(j=1;j<=ny;j++)
							if(!sy[j])
								if(lx[i]+ly[j]-g[i][j]<min)
									min=lx[i]+ly[j]-g[i][j];
				for (i=1;i<=nx;i++)
					if(sx[i])
					{
						lx[i]-=min;
						sx[i]=false;
					}
					for(j=1;j<=ny;j++)
						if(sy[j])
						{
							ly[j]+=min;
							sy[j]=false;
						}
			}
		}
}
int x[801],y[801];
int main()
{
	int css,cs,n,i,j,ans;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d",&x[i]);
		for(i=1;i<=n;i++)
			scanf("%d",&y[i]);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				g[i][j]=-x[i]*y[j];
		nx=ny=n;
		KuhnMunkres();
		ans=0;
		for(i=1;i<=n;i++)
			ans-=lx[i]+ly[i];
		printf("Case #%d: %d\n",css,ans);
	}
	return 0;
}
