#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 1000010
#define eps 1e-10
int xlen[maxn*2],mark[maxn];
struct Nodes{
	int l,r,w;
}p[maxn];
int n,S,R,cnt;
double T;
int m;
int t,cas;
int len;
bool cmp(Nodes aa,Nodes bb)
{
	return aa.w<bb.w;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k,kk;
	double ans,nowv,tcos;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d%d%d%lf%d",&len,&S,&R,&T,&n);
		memset(mark,0,sizeof(mark));
		m=0;
		for(i=1;i<=n;i++){
			scanf("%d%d%d",&j,&k,&kk);
			xlen[++m]=j;
			xlen[++m]=k;
			mark[j]=kk;
		}
		xlen[++m]=0;
		xlen[++m]=len;
		sort(xlen+1,xlen+m+1);
		m=unique(xlen+1,xlen+m+1)-xlen-1;
		/*for(i=1;i<=m;i++){
			printf("%d %d\n",i,xlen[i]);
		}*/
		cnt=0;
		for(i=1;i<m;i++){
			cnt++;
			p[cnt].l=xlen[i];
			p[cnt].r=xlen[i+1];
			p[cnt].w=mark[xlen[i]];
		}
		sort(p+1,p+cnt+1,cmp);
		ans=0;
		for(i=1;i<=cnt;i++){
			//printf("%d %d %d\n",p[i].l,p[i].r,p[i].w);
			if(T>eps){
				nowv=R+p[i].w;
				tcos=(p[i].r-p[i].l)/nowv;
				if(tcos<=T){
					T-=tcos;
					ans+=tcos;
				}else{
					ans+=T+(p[i].r-p[i].l-nowv*T)/(S+p[i].w);
					T=-1;
				}
			}else ans+=(p[i].r-p[i].l)*1.0/(S+p[i].w);
		}
		printf("Case #%d: %.8f\n",cas,ans);
	}
	return 0;
}
