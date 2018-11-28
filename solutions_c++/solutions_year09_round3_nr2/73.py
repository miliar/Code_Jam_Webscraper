#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>

using namespace std;

void submit() {
	freopen("D:\\Codejam\\problem\\problem\\input.in", "r", stdin);
    freopen("D:\\Codejam\\problem\\problem\\output.out", "w", stdout);
}

//code here

int N;
double pos[501][3];
double vlo[501][3];

const double eps = 1e-9;

int main() {
	submit();
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		scanf("%d", &N);
		double x=0, y=0, z=0, vx=0, vy=0, vz=0;
		for (int i=0; i<N; ++i) {
			double x0, y0, z0, vx0, vy0, vz0;
			scanf("%lf %lf %lf %lf %lf %lf", &x0, &y0, &z0, &vx0, &vy0, &vz0);
			x += x0;
			y += y0;
			z += z0;
			vx += vx0;
			vy += vy0;
			vz += vz0;
		}
		x /= N;
		y /= N;
		z /= N;
		vx /= N;
		vy /= N;
		vz /= N;

		double a = vx * vx + vy * vy + vz * vz;
		double b = 2 * vx * x + 2 * vy * y + 2 * vz * z;
		double c = x*x + y*y + z*z;

		double t = 0;
	    double d = sqrt(c);
		if (a < eps) {
			if (b < -eps) {
				t = - c / b;
				d = 0;
			}	
		}
		else {
			double cand = -b / a / 2;
			if (cand > eps) {
				t = cand;
				double d2 = a * t * t + b * t + c;
				if (d2 < 0)
					d = 0;
				else
					d = sqrt(d2);
			}
		}
		printf("Case #%d: %lf %lf\n", tid, d, t);
	}
	return 0;
}