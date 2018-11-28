#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

struct point{
	double x, y, z;
	point(){}
	point(double a, double b, double c){
		x=a; y=b; z=c;
	}
};

point operator-(const point &a, const point &b){
	return point(a.x-b.x, a.y-b.y, a.z-b.z);
}

double operator*(const point &a, const point &b){
	return a.x*b.x+a.y*b.y+a.z*b.z;
}

int main(){
	int d, n;
	double px, py, pz, vx, vy, vz;
	double dist;
	double t;
	point x0, x1, x2;
	int apx, apy, apz, avx, avy, avz;
	scanf("%d", &d);
	for(int i=1; i<=d; i++){
		scanf("%d", &n);
		px=0; py=0; pz=0; vx=0; vy=0; vz=0;
		for(int j=0; j<n; j++){
			scanf("%d %d %d %d %d %d", &apx, &apy, &apz, &avx, &avy, &avz);
			px+=apx;
			py+=apy;
			pz+=apz;
			vx+=avx;
			vy+=avy;
			vz+=avz;
		}
		px/=(double)n;
		py/=(double)n;
		pz/=(double)n;
		x0.x=0; x0.y=0; x0.z=0;
		x1.x=px; x1.y=py; x1.z=pz;
		if(vx==0 && vy==0 && vz==0){
			printf("Case #%d: %.08lf %.08lf\n", i, sqrt(x1*x1), (double)0);
			continue;
		}
		vx/=(double)n;
		vy/=(double)n;
		vz/=(double)n;	
		x2.x=px+vx; x2.y=py+vy; x2.z=pz+vz;
		
		t=-((x1-x0)*(x2-x1))/((x2-x1)*(x2-x1));
		if(t<=0){
			t=0;
		} 
		dist=((x1.x-x0.x)+((x2.x-x1.x)*t))*((x1.x-x0.x)+((x2.x-x1.x)*t))+((x1.y-x0.y)+((x2.y-x1.y)*t))*((x1.y-x0.y)+((x2.y-x1.y)*t))+((x1.z-x0.z)+((x2.z-x1.z)*t))*((x1.z-x0.z)+((x2.z-x1.z)*t));
		if(dist<0) dist=0;
		dist=sqrt(dist);
		printf("Case #%d: %.08lf %.08lf\n", i, dist, t);

	}
	
	return 0;
}





