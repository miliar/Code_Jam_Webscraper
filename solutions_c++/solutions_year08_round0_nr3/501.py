#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const double divide = 1e+7;

double height(double x, double R, double g, double r)
{
	double check = fabs(x) - int(fabs(x) / (2 * r + g)) * (2 * r + g);
	if(check < r || r+g < check) return 0;
	double T = sqrt(R * R - x * x);
	int n = 0;
	while(1) {
//cerr << T << ':' << x << ':' << R << ':' << g << ':' << r << ':' << n << endl;
		if(T <= (2*n+1)*r + n*g) return 2*n*g;
		if(T <= (2*n+1)*r+(n+1)*g) return 2*T-2*(2*n+1)*r;
		++n;
	}
}

double integral(double R, double g, double r)
{
	double step = 2*R/divide;
	double sx = -R, ex = -R + step;
	double sum = 0;
	while(ex < R) {
//cerr << sx << ':' << ex << endl;
//		sum += (height(sx, R, g, r) + height(ex, R, g, r)) * step / 2;
		sum += (height(sx, R, g, r) + 4 * height((sx+ex)/2, R, g, r) + height(ex, R, g, r)) * step / 6;
		sx = ex;
		ex += step;
	}
//	if(R-ex > 0.000000000001) sum += height(ex, R, g, r) * (R-ex) / 2;
	if(R-ex > 0.000000000001) sum += (height(ex, R, g, r)+4*height(R-(R-ex)/2, R, g, r)) * (R-ex) / 6;
	return sum;
}

int main(void)
{
	int n;
	double f, R, t, r, g;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		double res = 1.0;
		cin >> f >> R >> t >> r >> g;
		if(2 * f < g) {
			res = ((M_PI * R * R) - integral(R - t - f, g - 2 * f, r + f)) / (M_PI * R * R);
		}
		cout << "Case #" << nn+1 << ": " << fixed << setprecision(6) << res << endl;
	}
	return 0;
}
