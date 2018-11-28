#include <iostream>
#include <fstream>
#include <cmath>

#define For(i,a,b) for (int i = (a); i < (b); i++)

using namespace std;

const double PI = 3.14159265358979323846;

double slice(double h, double x1, double x2, double r)
{
	if (h < 0)
		return slice(0, x1, x2, r)*2 - slice(-h, x1, x2, r);

	if (h >= r) return 0;

	double l = sqrt(r*r - h*h);

	if (x2 < x1) swap(x2, x1);

	if (x1 < -l) x1 = -l;
	if (x1 > l) x1 = l;
	if (x2 < -l) x2 = -l;
	if (x2 > l) x2 = l;

	double ret = 0.5 * (atan2(x2, sqrt(r*r-x2*x2))*r*r + x2*sqrt(r*r-x2*x2));
	ret -= 0.5 * (atan2(x1, sqrt(r*r-x1*x1))*r*r + x1*sqrt(r*r-x1*x1));
	ret -= (x2-x1)*h;

	return ret;
}

int main()
{
	ifstream fin("C.in");
	ofstream fout("C.out");

	int T;
	fin >> T;
	For (LOL, 1, T+1)
	{
		double f, R, t, r, g;
		fin >> f >> R >> t >> r >> g;

		double totarea = R*R*PI;

		double area = 0;
		if (R - t - f < -1e-7) goto output;
		if (2*f > g) goto output;

		R -= t+f;
		area = totarea - R*R*PI;

		double slots = 0;

		double x = 0;
		while (x+r+f+1e-7>-R)
			x -= g + 2*r;
		while (x-r-f-1e-7<R) {
			slots += 2*slice(0, x-r-f, x+r+f, R);
			x += g + 2*r;
		}

		area += slots*2;

		double l = 0;
		while (l+r+f+1e-7>-R)
			l -= g + 2*r;

		for (double x = l; x-2*r-2*f-1e-7 < R; x += 2*r+g)
			for (double y = l; y-2*r-2*f-1e-7 < R; y += 2*r+g) {
				area -= slice(y-r-f, x-r-f, x+r+f, R) - slice(y+r+f, x-r-f, x+r+f, R);
			}

		if (area > totarea) area = totarea;
		if (area < 0) area = 0;

		output:
		fout.precision(6);
		fout << fixed << "Case #" << LOL << ": " << area/totarea << endl;
	}

	return 0;
}