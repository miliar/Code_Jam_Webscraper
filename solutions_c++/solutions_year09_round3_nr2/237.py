#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main(){
	int ts, k;
	double cX, cY, cZ, sX, sY, sZ;
	double min, max;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ts);
	for(int _ts=1;_ts<=ts;_ts++){
		cX = cY = cZ = sX = sY = sZ = 0.0;
		scanf("%d",&k);
		for(int i=0;i<k;i++){
			double t1,t2,t3,t4,t5,t6;
			scanf("%lf %lf %lf %lf %lf %lf",&t1,&t2,&t3,&t4,&t5,&t6);
			cX += t1;
			cY += t2;
			cZ += t3;
			sX += t4;
			sY += t5;
			sZ += t6;
		}
		min = 0.0; 
		max = 10000000;
		double fa, fb;
		double K = (double)k;
		for(int i=0;i<200;i++){
			double a = (min*2 + max) / 3.0;
			double b = (min + max*2) / 3.0;
			fa = sqrt( ((cX+a*sX)/K)*((cX+a*sX)/K) + ((cY+a*sY)/K)*((cY+a*sY)/K) +  ((cZ+a*sZ)/K)*((cZ+a*sZ)/K) );
			fb = sqrt( ((cX+b*sX)/K)*((cX+b*sX)/K) + ((cY+b*sY)/K)*((cY+b*sY)/K) +  ((cZ+b*sZ)/K)*((cZ+b*sZ)/K) );
			if(fa > fb)
				min = a;
			else
				max = b;
		}
		printf("Case #%d: %.8lf %.8lf\n",_ts,(fa+fb)/2.0,(min+max)/2.0);
	}
	return 0;
}