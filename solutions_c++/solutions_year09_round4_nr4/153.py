#include <stdio.h>
#include <math.h>

double dis(double x,double y){
	return sqrt(x*x+y*y);
}

double max(double a,double b){
	return a>b?a:b;
}

double min(double a,double b){
	return a<b?a:b;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1; cs<=T; cs++){
		const int size=3;
		int n;
		double x[size],y[size],r[size];
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		double a;
		if(n==1){
			a=r[0];
		}else if(n==2){
			a=max(r[0],r[1]);
		}else{
			a=(dis(x[0]-x[1],y[0]-y[1])+r[0]+r[1])/2.0;
			a=min(a,(dis(x[1]-x[2],y[1]-y[2])+r[1]+r[2])/2.0);
			a=min(a,(dis(x[0]-x[2],y[0]-y[2])+r[0]+r[2])/2.0);
		}
		printf("Case #%d: %.9lf\n",cs,a); 
	}
	return 0;
}
