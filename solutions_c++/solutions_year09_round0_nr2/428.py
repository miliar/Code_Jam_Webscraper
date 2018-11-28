#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
#define fod(i,u,d) for (long i=(u); i>=(d); --i)
using namespace std;

const long maxn=201;
const long w[4][2]={-1,0, 0,-1, 0,1, 1,0};

long fa[maxn][maxn][2],lab[maxn][maxn];
long g[maxn][maxn],t,n,m,tot;

void init()
{
	scanf("%d%d",&n,&m);
	fo(i,1,n)
		fo(j,1,m) scanf("%d",&g[i][j]);
}
void make()
{
	long x,y,tx,ty,h;
	memset(fa,0,sizeof(fa));
	fo(i,1,n)
		fo(j,1,m) {
		   h=g[i][j], tx=ty=0;
		   fo(l,0,3) {
			   x=i+w[l][0], y=j+w[l][1];
			   if (x>0 && x<=n && y>0 && y<=m && g[x][y]<h) 
				   h=g[x][y], tx=x, ty=y;
		   }
		   if (tx) fa[i][j][0]=tx, fa[i][j][1]=ty;
	   }
}
long cal(long i, long j)
{
	if (!fa[i][j][0]) lab[i][j]=++tot; 
	else 
	if (lab[fa[i][j][0]][fa[i][j][1]]) 
		lab[i][j]=lab[fa[i][j][0]][fa[i][j][1]];
	else 
		lab[i][j]=cal(fa[i][j][0],fa[i][j][1]);
	return lab[i][j];
}
void solve()
{
	tot=0;
	memset(lab,0,sizeof(lab));
	fo(i,1,n)
		fo(j,1,m)
		   if (!lab[i][j]) cal(i,j);
}
void print()
{
	tot=0;
	long vis[maxn];
	memset(vis,0,sizeof(vis));
	fo(i,1,n) {
		fo(j,1,m) {
		   if (!vis[lab[i][j]]) vis[lab[i][j]]=++tot;
		   if (j>1) printf(" "); printf("%c",'a'+vis[lab[i][j]]-1);
	    }
		printf("\n");
	}
}
int main()
{
	freopen("Bl.in","r",stdin);
	freopen("Bl.out","w",stdout);
	scanf("%d",&t);
	fo(l,1,t) {
		init();
		make();
		solve();
		printf("Case #%d:\n",l);  print();
	}
	return 0;
}
