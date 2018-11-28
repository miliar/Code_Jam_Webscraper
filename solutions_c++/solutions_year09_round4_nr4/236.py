#include<iostream>
#include<math.h>
using namespace std;

long c,n;
double x[10],y[10],r[10];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	long h;
	double j,k,l;
	scanf("%ld",&c);
	for(h=1;h<=c;h++){
		scanf("%ld",&n);
		if(n==1){
			scanf("%lf%lf%lf",&x[0],&y[0],&r[0]);
			printf("Case #%ld: %.6lf\n",h,r[0]);
		}else if(n==2){
			scanf("%lf%lf%lf",&x[0],&y[0],&r[0]);
			scanf("%lf%lf%lf",&x[1],&y[1],&r[1]);
			printf("Case #%ld: %.6lf\n",h,r[0]>r[1]?r[0]:r[1]);
		}else{
			scanf("%lf%lf%lf",&x[0],&y[0],&r[0]);
			scanf("%lf%lf%lf",&x[1],&y[1],&r[1]);
			scanf("%lf%lf%lf",&x[2],&y[2],&r[2]);
			j=(sqrt((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]))+r[0]+r[1])/2;
			k=j>r[2]?j:r[2];
			j=(sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]))+r[0]+r[2])/2;
			l=j>r[1]?j:r[1];
			if(k>l)k=l;
			j=(sqrt((x[1]-x[2])*(x[1]-x[2])+(y[1]-y[2])*(y[1]-y[2]))+r[1]+r[2])/2;
			l=j>r[0]?j:r[0];
			if(k>l)k=l;
			printf("Case #%ld: %.6lf\n",h,k);
		}
	}
	return 0;
}