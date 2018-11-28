// codejam_c.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define pi 3.14159265358979323846
#define eps 1e-8

using namespace std;

double sqr(double x){ return x*x;}
double dst(double ax, double ay, double bx, double by){
	return sqr(ax-bx)+sqr(by-ay);
}
double lx, ly, hx, hy, mx, my;
double f, R, t, r, g, binx, biny;

void bs(void){
	while ((hx - lx > eps) || (fabs(hx-lx) <= eps && eps < hy - ly)){
		//printf("(%.2lf, %.2lf) ~ (%.2lf, %.2lf)\n", lx, ly, hx, hy);
		mx = (lx+hx)/2, my = (ly+hy)/2;
		if (sqr(R-t-f) - dst(0, 0, mx, my) > -eps ){ //Inside
			lx = mx;
			ly = my;
		}else{ //Outside
			hx = mx;
			hy = my;
		}
	}
	if (lx == hx && ly == hy){
		binx = lx;
		biny = ly;
	}else{
		if (sqr(R-t-f) - dst(0, 0, lx, ly) > -eps){
			binx = lx;
			biny = ly;
		}else{
			binx = hx;
			biny = hy;
		}
	}
}

int main()
{
	int T, Case=0;
	scanf("%d", &T);
	while (T--){
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		double P = 0;
		for (int i = 1 ; (2*i-1)*r+(i-1)*g <= R-t; ++i)
			for (int j = 1; (2*j-1)*r+(j-1)*g <= R-t; ++j){
				double x = (2*i-1)*r+(i-1)*g;
				double y = (2*j-1)*r+(j-1)*g;
				if (sqr(R-t-f) - dst(0, 0, x+g, y+g) > -eps){
					P += sqr(g-2*f);
					continue;
				}
				if (dst(0, 0, x+f, y+f) - sqr(R-t-f) > eps) continue;
				double A[5][2];
				int cnt = 1;
				A[0][0] = x+f;
				A[0][1] = y+f;
				//printf("\tCentre Point (%.2lf %.2lf)\n", x+f, y+f);
				x += f, y += f;
				double sw = g - 2*f;
				//printf("\tLocated Point (%.2lf %.2lf)\n", A[p+1][0], A[p+1][1]);
				lx = x, ly = y, hx = x+sw, hy = y, bs();
				A[cnt][0] = binx, A[cnt++][1] = biny;
				//printf("%.5lf == %.5lf, %.5lf == %.5lf?\n", binx, x+sw, biny, y);
				if (fabs(binx-x-sw) <= eps && fabs(biny-y) <= eps){
					lx = x+sw, ly = y, hx = x+sw, hy = y+sw, bs();
					A[cnt][0] = binx, A[cnt++][1] = biny;
				}
				lx = x, ly = y, hx = x, hy = y+sw, bs();
				A[cnt][0] = binx, A[cnt++][1] = biny;
				//printf("%.5lf == %.5lf, %.5lf == %.5lf?\n", binx, x, biny, y+sw);
				if (fabs(binx-x) <= eps && fabs(biny-y-sw) <= eps){
					lx = x, ly = y+sw, hx = x+sw, hy = y+sw, bs();
					A[cnt][0] = binx, A[cnt++][1] = biny;
					swap(A[cnt-2][0], A[cnt-1][0]);
					swap(A[cnt-2][1], A[cnt-1][1]);
				}
				//for (int i = 0 ; i < cnt; ++i) printf("[%d]: %.6lf %.6lf\n", i+1, A[i][0], A[i][1]);
				double TP=0;
				for (int p = 0 ; p < cnt; ++p)
					TP += A[p][0] * A[(p+1)%cnt][1] - A[p][1] * A[(p+1)%cnt][0];
				TP /= 2;
				for (int p = 0 ; p < cnt; ++p)
					if (fabs(A[p][0]-A[(p+1)%cnt][0]) > eps && fabs(A[p][1]-A[(p+1)%cnt][1]) > eps){
						double cp = A[p][0] * A[(p+1)%cnt][1] - A[p][1] * A[(p+1)%cnt][0];
						double dp = A[p][0] * A[(p+1)%cnt][0] + A[p][1] * A[(p+1)%cnt][1];
						double SP = sqr(R-t-f)*atan2(cp, dp)/2-0.5*cp;
						//printf("%.10lf - %.10lf = %.10lf\n", sqr(R-t-f)*atan2(cp, dp)/2, 0.5*cp, SP);
						TP+=SP;
					}
				//printf("Add %.2lf\n", TP/2);
				P += TP;
			}
		printf("Case #%d: %.10lf\n", ++Case, 1 - 4 * P / sqr(R) / pi);
	}
	return 0;
}

