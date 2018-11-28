#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


long double pi = acos((long double)0.0)*2;
long double ffint(long double a, long double b, long double x) {
	return x/2*sqrt(a*a-x*x)+a*a/2*asin(x/a)-b*x;
}

long double fint(long double a, long double b, long double c1, long double c2) {
	// int { sqrt(a*a - x*x) - b }
	//=x/2*sqrt(a*a-x*x)+a*a/2*asin(x/a)-b*x
	return fabs(ffint(a,b,c2)-ffint(a,b,c1));
}

void main() {
	ifstream inp("c.in");
	ofstream out("c.out");
	int cases;
	inp >> cases;
	for (int id=1; id<=cases; id++) {
		long double f, R, t, r, g, P = 1;
		inp >> f >> R >> t >> r >> g;
		if (g > 2*f && R-t > f) {
			P = 0;
			for (int i = 0; ; i++) {
				long double a = i * (g + 2*r) + r;
				if (a >= R - t - 2*f) break;
				for (int j = 0; ; j++) {
					long double b = j * (g + 2*r) + r;
					if (b >= R - t - 2*f) break;
					long double t1 = sqrt((R-t-f)*(R-t-f) - (b+f)*(b+f));
					if (t1 > a + g - f) t1 = a + g - f; // x <= t1
					long double t2 = a + f;
					if (R-t>=b+g) {
						long double t3 = sqrt((R-t-f)*(R-t-f)-(b+g-f)*(b+g-f));
						if (t3 > t1) t3 = t1;
						if (t3 > t2) {
							P += (t3-t2)*(g-2*f);
							t2 = t3;
						}
					}
					// x : t2 -> t1
					// y: sqrt((R-t-f)^2-x^2)
					if (t1 > t2) {
						P += fint(R-t-f, b+f, t2, t1);
					}
				}
			}
			long double whole = pi*(R)*(R)/4;
			P = (whole - P) / whole;
		}
		out << "Case #" << id << ": " << P << endl;
	}
}
