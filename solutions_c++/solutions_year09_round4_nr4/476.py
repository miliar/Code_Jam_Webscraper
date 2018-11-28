#include<stdio.h>
#include<memory.h>
#include<math.h>
#include<algorithm>
#define sqr(x) ((x)*(x))
#define max(x,y) ((x)>(y)?(x):(y))


int T,n;
double x[111],y[111],r[111];
double ans=0;

double dist(double x,double y ,double xx,double yy){
	return sqrt(sqr(x-xx)+sqr(y-yy));
}


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=0;_<T;_++){

		scanf("%d\n",&n);		
		for(int i=0;i<n;i++)
			scanf("%lf %lf %lf\n",&x[i],&y[i],&r[i]);
		ans=0;
		if(n==1) ans=r[0];else
		if(n==2){
			ans=(dist(x[1],y[1],x[0],y[0])+r[1]+r[0])/2;
			ans<?=max(r[1],r[0]);
		}else{
			ans=max ( (dist(x[1],y[1],x[0],y[0])+r[1]+r[0])/2 , r[2]);
			ans<?=max ( (dist(x[1],y[1],x[2],y[2])+r[1]+r[2])/2 , r[0]);
			ans<?=max ( (dist(x[0],y[0],x[2],y[2])+r[0]+r[2])/2 , r[1]);
		}
		printf("Case #%d: %0.7lf\n",_+1,ans);
	}
	return 0;
}
