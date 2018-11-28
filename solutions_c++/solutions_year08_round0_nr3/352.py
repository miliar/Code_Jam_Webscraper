#include <iostream>
#include <math.h>
using namespace std;

#define D(a,b) (sqrt((a)*(a) + (b)*(b)))
#define pi 3.1415926535897932384626433832795

double seg(double r, double l) {
	l = 0.5 * l;
	double res = asin(l/r)*r*r;
	res -= sqrt(r*r - l*l) * l;
	return res;
}

int main() {
	int N, nn = 0;
	cin >> N;
	double f, R, t, r, g, prob;
	double rad;
	while(nn < N) {
		cin >> f >> R >> t >> r >> g;
		rad = R - t - f;
		r += f;
		g -= (f+f);
		if(g < 0 || rad < 0) {
			prob = 1.0;
			goto A;
		}
		double x1 = r, y1 = r, x2, y2, x3, y3, x4, y4, area = 0;
		while(x1 < rad) {
			y1 = r;
			while(D(x1, y1) < (rad + 1e-9)) {
				x2 = x1 + g; y2 = y1;
				x3 = x1; y3 = y1 + g;
				x4 = x1 + g; y4 = y1 + g;
				double xrem , yrem, xrem1, yrem1;
				if(D(x4, y4) < (rad + 1e-9))
					area += g*g;
				else if(D(x3,y3) < (rad + 1e-9) && D(x2,y2) < (rad + 1e-9)) {
					xrem = g - sqrt(rad*rad - y3*y3) + x3;
					yrem = g - sqrt(rad*rad - x2*x2) + y2;
					area += g*g - xrem*yrem*0.5 + seg(rad, D(xrem, yrem));
				}
				else if(D(x3,y3) < (rad + 1e-9)) {
					xrem = sqrt(rad*rad - y1*y1) - x1;
					xrem1 = sqrt(rad*rad - y3*y3) - x3;
					area += 0.5 * g * (xrem + xrem1) + seg(rad, D(g,(xrem-xrem1)));
				}
				else if(D(x2,y2) < (rad + 1e-9)) {
					yrem = sqrt(rad*rad - x1*x1) - y1;
					yrem1 = sqrt(rad*rad - x2*x2) - y2;
					area += 0.5 * g * (yrem + yrem1) + seg(rad, D(g,(yrem-yrem1)));
				}
				else {
					xrem = sqrt(rad*rad - y1*y1) - x1;
					yrem = sqrt(rad*rad - x1*x1) - y1;
					area += xrem*yrem*0.5 + seg(rad, D(xrem, yrem));
				}
				y1 += g + r + r;
			}
			x1 += g + r + r;
		}
		prob = 1.0 - ((4 * area) / (pi*R*R));
A:;
		cout << "Case #" << ++nn << ": ";
		printf("%1.6f\n", prob);
	}
	return 0;
}
