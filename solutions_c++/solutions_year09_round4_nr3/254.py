#include<iostream>
#include<stdio.h>
#include<string.h>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
using namespace std;

const long maxn=501;
const long maxk=100;

long pri[maxn][maxk],n,t,m;
long g[maxn][maxn];
long head[maxn],next[maxn*maxn],node[maxn*maxn],tt;
long w[maxn],vis[maxn];

void init()
{
	scanf("%d%d",&n,&m);
	fo(i,1,n)
		fo(j,1,m) scanf("%d",&pri[i][j]);
}
void add(long x, long y)
{
	node[++tt]=y, next[tt]=head[x], head[x]=tt;
}
void make()
{
	memset(g,0,sizeof(g));
	long pd;
	fo(i,1,n)
		fo(j,1,n) {
		    pd=1;
		    fo(l,1,m)  
				if (pri[i][l]>=pri[j][l]) {pd=0; break;}
			if (pd) g[i][j]=1;
	    }
	/*fo(l,1,n)
	   fo(i,1,n) if (i!=l)
		  fo(j,1,n) if (j!=l && j!=i)
		     g[i][j]=g[i][j] | (g[i][l] & g[l][j]);*/
	memset(head,0,sizeof(head)), tt=0;
	fo(i,1,n)
		fo(j,1,n) 
		    if (g[i][j]) add(i,j+n);
}
long find(long x)
{
	for (long i=head[x]; i; i=next[i])
		if (!vis[node[i]]) {
		    vis[node[i]]=1;
			if (!w[node[i]] || find(w[node[i]])) {
				w[node[i]]=x;
				return 1;
			}
	    }
	return 0;
}
void solve()
{
	memset(w,0,sizeof(w));
	long ans=0;
	fo(i,1,n) {
		memset(vis,0,sizeof(vis));
		if (find(i)) ++ans;
	}
	printf("%d\n",n-ans);
}
int main()
{
	freopen("CL.in","r",stdin);
	freopen("CL.out","w",stdout);
	scanf("%d",&t);
	fo(l,1,t) {
		init();
		make();
		printf("Case #%d: ",l);
		solve();
	}
	return 0;
}
