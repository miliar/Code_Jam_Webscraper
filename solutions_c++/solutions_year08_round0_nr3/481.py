#include <iostream>
#include <string>
#include <math.h>

using namespace std;

#define rep(i, n) for (int i=0; i<(n); i++)
#define PI 3.14159265

double quad(double x) {
	return x*x;
}

double modulo2(double x, double y) {
	return quad(x) + quad(y);
}

double calc(double R, double a, double x, double y) {
	if (modulo2(x, y) >= R*R) {
		return 0;
	}
	if (modulo2(x+a, y+a) < R*R) {
		return 0;
	}
	if (modulo2(x+a, y) >= R*R) {
		// direito fora
		if (modulo2(x, y+a) >= R*R) {
			// superior fora
			double xi = sqrt(R*R - y*y);
			double yi = sqrt(R*R - x*x);
			double alfa = acos(x/R) - asin(y/R);
			assert(alfa > 0);
			return (xi-x)*(yi-y)/2 + R*R*alfa/2 - R*R*sin(alfa)/2;
		} else {
			// superior dentro
			double x1 = sqrt(R*R - quad(y+a));
			double x2 = sqrt(R*R - y*y);
			double alfa = asin((y+a)/R) - asin(y/R);
			assert(alfa > 0);
			return (x2-x + x1-x)*a/2 + R*R*alfa/2 - R*R*sin(alfa)/2;
		}
	} else {
		// direito dentro
		if (modulo2(x, y+a) >= R*R) {
			// superior fora
			double y1 = sqrt(R*R - x*x);
			double y2 = sqrt(R*R - quad(x+a));
			double alfa = acos(x/R) - acos((x+a)/R);
			assert(alfa > 0);
			return (y1-y + y2-y)*a/2 + R*R*alfa/2 - R*R*sin(alfa)/2;
		} else {
			// superior dentro
			double xi = sqrt(R*R - quad(y+a));
			double yi = sqrt(R*R - quad(x+a));
			double alfa = asin((y+a)/R) - acos((x+a)/R);
			assert(alfa > 0);
			double area = 0;
			area += a*a - (x+a-xi)*(y+a-yi)/2;
			area += R*R*alfa/2 - R*R*sin(alfa)/2;
			return area;
		}
	}
	return 0;
}

int main(void) {
	int N;
	double f, R, t, r, g;
	double p;
	double x, y;

	cout.setf(ios::fixed, ios::floatfield);
	cin >> N;
	rep(k, N) {
		cin >> f >> R >> t >> r >> g;
		//cout << f << " " << R << " " << t << " " << r << " " << g << endl;
		if (2*f >= g) p = 0;
		else {
			p = 0;
			for(x = r; x <= R-t; x += 2*r+g) {
				for(y = r; y <= R-t; y += 2*r+g) {
					if (modulo2(x, y) <= quad(R-t)) {
						if (modulo2(x+g, y+g) <= quad(R-t)) {
							p += quad(g-2*f);
						} else {
							p += calc(R-t-f, g-2*f, x+f, y+f);
						}
					}
				}
			}
			p *= 4;
			p /= (PI*R*R);
		}
		cout << "Case #" << (k+1) << ": " << (1-p) << endl;
	}

}

