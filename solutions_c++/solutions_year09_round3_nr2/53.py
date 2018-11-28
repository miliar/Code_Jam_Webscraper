#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
const double eps = 1e-9;

int main() {
	int cas, cass=0;
	for (scanf("%d", &cas); cas--; ) {
		printf("Case #%d:", ++cass);
		int n;
		scanf("%d", &n);
		double x=0, y=0, z=0, vx=0, vy=0, vz=0;
		for (int i=0; i<n; ++i) {
			int xx, yy, zz, vvx, vvy, vvz;
			scanf("%d %d %d %d %d %d", &xx, &yy, &zz, &vvx, &vvy, &vvz);
			x += xx;
			y += yy;
			z += zz;
			vx += vvx;
			vy += vvy;
			vz += vvz;
		}
		x /= n;
		y /= n;
		z /= n;
		vx /= n;
		vy /= n;
		vz /= n;
//		printf("%.2lf %.2lf %.2lf %.2lf %.2lf %.2lf\n", x, y, z, vx, vy, vz);
		double a = vx*vx + vy*vy + vz*vz;
		double b = vx*x + vy*y +vz*z;
		b *= 2;
		double c = x*x + y*y + z*z;
//		printf("%.2lf %.2lf %.2lf\n", a, b, c);
		if (fabs(a)<eps) {
			double t = -c/b;
			t = 0.0;
			double res = (x+vx*t)*(x+vx*t)+(y+vy*t)*(y+vy*t)+(z+vz*t)*(z+vz*t);
			res = sqrt(res);
			printf(" %.10lf %.10lf\n", res+eps, t+eps);
		}
		else {
			double t = -b/a/2;
			t = max(t, 0.0);
			double res = (x+vx*t)*(x+vx*t)+(y+vy*t)*(y+vy*t)+(z+vz*t)*(z+vz*t);
			double tt = 0.0;
			double tmp = (x+vx*tt)*(x+vx*tt)+(y+vy*tt)*(y+vy*tt)+(z+vz*tt)*(z+vz*tt);
			if (tmp<res-eps) {
				res = tmp;
				t = tt;
			}
			res = sqrt(res);
			printf(" %.10lf %.10lf\n", res+eps, t+eps);			
		}
			
			
	}
	return 0;
	
}
				
