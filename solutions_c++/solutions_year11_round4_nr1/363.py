#include <cstdio>
#include <algorithm>

using namespace std;

struct ty{
	double x,y,s,len;
};

double len,walk,run,runtime,x[1000000*2],y[1000000*2];
int tr,n;
ty p[1000000*2];

bool cmp(const ty &a,const ty &b){
	return a.s<b.s;
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%lf%lf%lf%lf%d",&len,&walk,&run,&runtime,&n);
		int tot=0;
		p[tot].x=p[tot].y=p[tot].s=0;
		for (int i=0;i<n;i++){
			tot++;
			scanf("%lf%lf%lf",&p[tot].x,&p[tot].y,&p[tot].s);
			x[i]=p[tot].x,y[i]=p[tot].y;
			if (x[i]>y[i-1]){
				tot++;
				p[tot].x=y[i-1];
				p[tot].y=x[i];
				p[tot].s=0;
			}
		}
		tot++;
		p[tot].x=y[n-1],p[tot].y=len,p[tot].s=0;
		tot++;
		sort(p,p+tot,cmp);
		for (int i=0;i<tot;i++)
			p[i].len=p[i].y-p[i].x;
		double ans=0;
		int j;
		for (int i=0;i<tot;i++){
			if (ans+p[i].len/(p[i].s+run)<=runtime)
				ans+=p[i].len/(p[i].s+run);
			else{
				ans+=(runtime-ans)+(p[i].len-(p[i].s+run)*(runtime-ans))/(walk+p[i].s);
			}
			if (ans>=runtime){
				j=i+1;
				break;
			}
		}
		for (int i=j;i<tot;i++)
			ans+=p[i].len/(walk+p[i].s);
		printf("Case #%d: %.7f\n",test+1,ans);
	}
	
	return 0;
}
