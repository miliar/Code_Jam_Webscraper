#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
struct node{
	int x;
	int y;
	int t;};
node e[2000],w[4000];
int a,b,c,d,f,g,h,i,j,k,m,n,tcase,X,S,R,N;
double ans,u,T;
const int lim=2147483647;
bool cmp(node p,node q)
{   return (p.x<q.x ||((p.x==q.x) &&(p.y<q.y)) );}
bool cmp2(node p,node q)
{   return p.t<q.t;}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&tcase);
	for (f=1;f<=tcase;f++){
		printf("Case #%d: ",f);
		ans=0;
		scanf("%d%d%d%lf%d",&X,&S,&R,&T,&N);
		for (i=1;i<=N;i++)scanf("%d%d%d",&e[i].x,&e[i].y,&e[i].t);
		e[N+1].x=0;e[N+1].y=0;e[N+1].t=lim;
		e[N+2].x=X;e[N+2].y=X;e[N+2].t=lim;
		N+=2;
		sort(e+1,e+N+1,cmp);
		//for (i=1;i<=N;i++) printf("%d %d %d\n",e[i].x,e[i].y,e[i].t);
		c=0;
		for (i=2;i<=N;i++){
			if (i<N){
				c++;
				w[c].x=e[i].y-e[i].x;
				w[c].t=S+e[i].t;
				}
			if (e[i].x>e[i-1].y){
				c++;
				w[c].x=e[i].x-e[i-1].y;
				w[c].t=S;}
			}
		sort(w+1,w+c+1,cmp2);
		//for (i=1;i<=c;i++) printf("%d %d\n",w[i].x,w[i].t);
		if (R<S) T=0;
		R=R-S;
		for (i=1;i<=c;i++){
			//printf("# %.6lf %.6lf \n",ans,T);
			if (fabs(T)<1e-9){
				u=w[i].x;
				ans=ans+u/w[i].t;} else
			if (T*(R+w[i].t)>=w[i].x){
				u=w[i].x;
				ans=ans+u/(R+w[i].t);
				//printf("## %.6lf %d\n",u,R);
				T=T-u/(R+w[i].t);} else{
				u=w[i].x;
				u=u-T*(R+w[i].t);
				ans=ans+u/w[i].t+T;
				T=0;}
			}
		printf("%.7lf\n",ans);
		}
	return 0;
}
