#include<iostream>
#include<math.h>
using namespace std;

long t,n;
double x[501],y[501],z[501],vx[501],vy[501],vz[501];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	long h,i,j,k;
	double x1,y1,z1,x2,y2,z2,a,b,x3,y3,z3;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		x1=0;x2=0;
		y1=0;y2=0;
		z1=0;z2=0;
		scanf("%ld",&n);
		for(i=1;i<=n;i++){
			scanf("%lf%lf%lf%lf%lf%lf",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
			x1+=x[i]/(n+0.0);
			y1+=y[i]/(n+0.0);
			z1+=z[i]/(n+0.0);
			x2+=vx[i]/(n+0.0);
			y2+=vy[i]/(n+0.0);
			z2+=vz[i]/(n+0.0);
		}
		if(fabs(x2)<=0.00000001 && fabs(y2)<=0.00000001 && fabs(z2)<=0.00000001){
			b=sqrt(x1*x1+y1*y1+z1*z1);
			printf("Case #%ld: %.8lf %.8lf\n",h,b,0);
			continue;
		}a=(x1*x2+y1*y2+z1*z2)/(x2*x2+y2*y2+z2*z2);
		if(a<0)a=-a;
		else{
			b=sqrt(x1*x1+y1*y1+z1*z1);
			printf("Case #%ld: %.8lf %.8lf\n",h,b,0);
			continue;
		}
		x3=x1+a*x2;
		y3=y1+a*y2;
		z3=z1+a*z2;
		b=sqrt(x3*x3+y3*y3+z3*z3);
		printf("Case #%ld: %.8lf %.8lf\n",h,b,a);
	}
	return 0;	
}