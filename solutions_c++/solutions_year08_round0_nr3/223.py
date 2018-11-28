#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int test;

double f, R, t, r, g;
const double pi = acos(-1.);

double SQR(double x) {
	return x*x;
}

double square(double x1, double y1, double x2, double y2, double x3, double y3) {
	return fabs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2;
}

double find(double x, double y) {
	double r1 = R - t - f;
	x += f; y += f;
	double s = g - 2*f;
	if (r1 <= 0 || s <= 0) return 0;
	if (SQR(x) + SQR(y) > SQR(r1)) return 0;
	if (SQR(x + s) + SQR(y + s) <= SQR(r1)) return s*s;
	double res = 0;
	
	vector<double> xx;
	vector<double> yy;
	
	xx.push_back(x); yy.push_back(y);
	
	double x1, y1;
	double x2, y2;

	if (SQR(x) + SQR(y + s) < SQR(r1)) {
		xx.push_back(x); yy.push_back(y + s);
		y1 = y + s; x1 = sqrt(fabs(SQR(r1) - SQR(y1)));
		xx.push_back(x1); yy.push_back(y1);
	} else {
		x1 = x; y1 = sqrt(fabs(SQR(r1) -  SQR(x1)));
		xx.push_back(x1); yy.push_back(y1);
	}
	
	if (SQR(x + s) + SQR(y) < SQR(r1)) {
		x2 = x+s; y2 = sqrt( fabs( SQR(r1) - SQR(x2)) );
		xx.push_back(x2); yy.push_back(y2);
		xx.push_back(x + s); yy.push_back(y);
	} else {
		y2 = y; x2 = sqrt( fabs( SQR(r1) - SQR(y2) ) );
		xx.push_back(x2); yy.push_back(y2);
	}
	
	for (int i = 2; i < xx.size(); i++) {
		res += square(xx[0], yy[0], xx[i-1], yy[i-1], xx[i], yy[i]);
	}
	
	double L = hypot(x2 - x1, y2 - y1);
	double al = asin(L / 2. / r1); al *= 2;

	res += r1*r1*(al - sin(al)) / 2;

	return res;
}

void solve() {
	double res = 0;
	
	cin >> f >> R >> t >> r >> g;

	for (int i = 0; i < 1100; i++) {
		for (int j = 0; j < 1100; j++) {
			double x = r + (g + 2*r)*i;
			double y = r + (g + 2*r)*j;
			res += find(x, y);
		}
	}
	
	double S = pi*R*R/4;

	res = res / S;
	res = 1 - res;

	cout << "Case #" << test << ": ";
	printf("%.6lf\n", res);
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int N;
	cin >> N;
	for (test = 1; test <= N; test++)
		solve();
	fclose(stdin);
	fclose(stdout);
	return 0;
}