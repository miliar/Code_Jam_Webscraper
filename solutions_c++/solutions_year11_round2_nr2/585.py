#include<stdio.h>
#define MAX 10000000000000000.0
int n;
double D;
struct ee{double x,c;}a[300];
int check(double m){
	int i;
	double L=-MAX,x;
	for(i=0;i<n;i++){
		if(a[i].x+m<L)return 0;
		x=L;
		if(a[i].x-m>L)x=a[i].x-m;
		x+=D*a[i].c;
		if(x-D>a[i].x+m)return 0;
		L=x;
	}
	return 1;
}	
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,t,i;
	double L,R,m;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%lf",&n,&D);
		for(i=0;i<n;i++)scanf("%lf%lf",&a[i].x,&a[i].c);
		L=0;R=MAX;
		while(L+0.00000001<R){
			m=(L+R)/2;
			if(check(m))R=m;
			else L=m;
		}
		printf("Case #%d: %.10lf\n",t,R);
	}
}
