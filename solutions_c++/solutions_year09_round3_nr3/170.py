#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<memory>
#define fo(i,u,d) for (long i=(u); i<=(d) ;++i)
using namespace std;

const long maxn=10005;
const long inf=1000000000;

long pos[maxn],n,m,t;
long f[maxn][maxn];

void init()
{
	scanf("%d%d",&n,&m);
	fo(i,1,m) scanf("%d",&pos[i]);
	sort(pos+1,pos+m+1);
}
long solve(long x, long y)
{
	long now, num=inf;
	fo(i,1,m) {
		if (pos[i]>=x && pos[i]<=y) {
			now=0;
			if (pos[i]>x) {
				if (f[x][pos[i]-1]==-1) solve(x,pos[i]-1); 
				now+=f[x][pos[i]-1];
			}
		    now+=pos[i]-x;
			if (pos[i]<y) {
				if (f[pos[i]+1][y]==-1) solve(pos[i]+1,y);
				now+=f[pos[i]+1][y]; 
			}
			now+=y-pos[i];
			if (now<num) num=now;
		}
	}
	if (num==inf) num=0;
	f[x][y]=num;
	return num;
}
int main()
{
	freopen("CL.in","r",stdin);
	freopen("CL.out","w",stdout);
	scanf("%d",&t);
	fo(l,1,t) {
		init();
		memset(f,255,sizeof(f));
		printf("Case #%d: %d\n",l,solve(1,n));
	}
	return 0;
}
