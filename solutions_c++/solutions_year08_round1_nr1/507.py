#include <iostream>
using namespace std;
#define  maxn 810
long long lx[maxn],ly[maxn];
int nx,ny,cx[maxn],cy[maxn];
long long g[maxn][maxn];
bool sx[maxn],sy[maxn];
long long x[maxn],y[maxn];

bool path(int u)
{ 
	sx[u]=1;
	for(int v=1;v<=ny;v++) 
		if(g[u][v]==lx[u]+ly[v]&&!sy[v])
		{
			sy[v]=true;
			if(!cy[v]||path(cy[v]))
			{ 
				cx[u]=v; cy[v]=u; 
				return true; 
			}
		} 
		return false;
}
void KuhnMunkres()
{ 
	int i,j,u;long long min;

	memset(lx,0,sizeof(lx));
	memset(ly,0,sizeof(ly));
	memset(cx,0,sizeof(cx)); 
	memset(cy,0,sizeof(cy));
	for(i=1;i<=nx;i++) 
		for(j=1;j<=ny;j++)
			if(lx[i]<g[i][j]) lx[i]=g[i][j];
	for(u=1;u<=nx;u++)
		if(!cx[u])
		{ 
			memset(sx,0,sizeof(sx)); 
			memset(sy,0,sizeof(sy));
			while(!path(u))
			{ 
				min=0x3fffffff;
				for(i=1;i<=nx;i++)
					if(sx[i])for(j =1;j<=ny;j++)
						if (!sy[j])
							if(lx[i]+ly[j]-g[i][j]<min)min=lx[i]+ly[j]-g[i][j];
				for(i=1;i<=nx;i++)
					if(sx[i])lx[i]-=min,sx[i]=false; 

				for(j=1;j<=ny;++j)
					if(sy[j])ly[j]+=min,sy[j]=false; 
			}
		}
}
int main()
{
	int i,k,l,n,ncase; cin>>ncase;
	for(l=1;l<=ncase;l++)
	{
		cin>>n;
		for(i=1;i<=n;i++)cin>>x[i];
		for(i=1;i<=n;i++)cin>>y[i];
		for(i=1;i<=n;i++)
			for(k=1;k<=n;k++)g[i][k]=-x[i]*y[k];

		nx=ny=n;KuhnMunkres();
		long long answer=0;
		for(i=1;i<=n;i++)answer+=lx[i]+ly[i];

		cout<<"Case #"<<l<<": "<<-answer<<endl;
	}
	return 0;
}


