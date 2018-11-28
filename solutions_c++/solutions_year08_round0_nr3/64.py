#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <algorithm>

using namespace std;

double dist(double x1, double y1, double x2, double y2){
	double dx = x1-x2, dy = y1-y2;
	return sqrt(dx*dx + dy*dy);
}

double juring(double s, double R){
	double a = s/2, b = sqrt(R*R - a*a);
	double angle = fabs(2*atan2(a,b));
	return R*R*angle/2 - a*b;
}

bool intersectR(double x1, double y1, double x2, double y2, double R, double &x, double &y){
	if (x1 > x2 || y1 > y2) swap(x1,x2), swap(y1,y2);
	double r1 = dist(0,0, x1,y1), r2 = dist(0,0, x2,y2);
	if (r1 <= R && R <= r2){
		if (y1==y2){
			y = y1;
			x = R*R - y*y;
			assert(x>=0);
			x = sqrt(x);
			return true;
		} else {
			x = x1;
			y = R*R - x*x;
			assert(y>=0);
			y = sqrt(y);
			return true;
		}
	}
	return false;
}

double calc(double x1, double y1, double s, double R){
	if (s <= 0) return 0;
	double x2 = x1+s, y2 = y1;
	double x3 = x1+s, y3 = y1-s;
	double x4 = x1, y4 = y1-s;
	double ix1,iy1, ix2,iy2;

	if (dist(0,0,x1,y1) >= R && dist(0,0,x2,y2) >= R && dist(0,0,x3,y3) >= R && dist(0,0,x4,y4) >= R) return 0;
	bool ok1 = intersectR(x1,y1, x2,y2, R, ix1,iy1) || intersectR(x1,y1, x4,y4, R, ix1,iy1);
	bool ok2 = intersectR(x3,y3, x4,y4, R, ix2,iy2) || intersectR(x3,y3, x2,y2, R, ix2,iy2);
	assert(ok1 == ok2);
	if (ok1){
		double a = ix1-x1, b = iy2-y4, c = ix2-ix1, d = iy1-iy2;
		return a*s + b*s - a*b + (c*d)/2 + juring(dist(ix1,iy1, ix2,iy2), R);
	}
	return s*s;
}

int main(){
	double f,R,t,r,g;
	int nTC;

	scanf("%d",&nTC);
	for (int TC=1; TC<=nTC; TC++){
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		double area = M_PI * R * R, s = 2*r+g, no_hit = 0;
		int n = int(ceil(R/s)+1.001);
		for (int i=0; i<=n; i++)
			for (int j=1; j<=n; j++){
				double x = i*s + r + f;
				double y = j*s - r - f;
				double nS = g-f-f;
				double nR = R-t-f;
				no_hit += calc(x,y,nS,nR);
			}
		printf("Case #%d: %.6lf\n",TC,(area-4*no_hit)/area);
	}
}
