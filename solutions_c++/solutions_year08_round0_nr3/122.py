#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int test, tnum;

	double integral(double x1, double x2, double r)
	{
		if (x2 < x1)
			swap(x1, x2);
		double t2 = asin(x2 / r);
		double t1 = asin(x1 / r);
		return abs((r * r / 2.) *
			(
				(t2 + sin(2 * t2) / 2.) -
				(t1 + sin(2 * t1) / 2.)
			));
	}

	double sq(double x1, double x2, double y1, double y2, double r) {
		double y_x1, y_x2, x_y1, x_y2;

		y_x1 = x1 > r ? -1 : sqrt(r * r - x1 * x1);
		y_x2 = x2 > r ? -1 : sqrt(r * r - x2 * x2);
		x_y1 = y1 > r ? -1 : sqrt(r * r - y1 * y1);
		x_y2 = y2 > r ? -1 : sqrt(r * r - y2 * y2);

		if (y_x1 < y1 || y_x1 > y2)
			y_x1 = -1;
		if (y_x2 < y1 || y_x2 > y2)
			y_x2 = -1;
		if (x_y1 < x1 || x_y1 > x2)
			x_y1 = -1;
		if (x_y2 < x1 || x_y2 > x2)
			x_y2 = -1;

		if (y_x1 < 0 && y_x2 < 0 && x_y1 < 0 && x_y2 < 0) {
			if (x1 * x1 + y1 * y1 <= r * r)
				return (y2 - y1) * (x2 - x1);
			else
				return 0;
		}

		if (y_x1 > -0.5 && x_y1 > -0.5) {
			return integral(x1, x_y1, r) - y1 * (x_y1 - x1);
		}

		if (y_x1 > -0.5 && y_x2 > -0.5) {
			return integral(x1, x2, r) - y1 * (x2 - x1);
		}

		if (x_y2 > -0.5 && y_x2 > -0.5) {
			return (y2 - y1) * (x_y2 - x1) +
				integral(x_y2, x2, r) - y1 * (x2 - x_y2);
		}

		if (x_y2 > -0.5 && x_y1 > -0.5) {
			return (y2 - y1) * (x_y2 - x1) +
				integral(x_y2, x_y1, r) - y1 * (x_y1 - x_y2);
		}

		return 0;

	}


	double f, R, t, r, g;
	double result;

	void readdata()
	{
		fin >> f >> R >> t >> r >> g;
	}

	void outputdata()
	{
		fout.setf(ios::fixed | ios::showpoint);
		fout.precision(6);
		fout << "Case #" << (test + 1) << ": " << result << endl;
	}

	void run()
	{
		double s_total = 2 * acos(0.) * R * R;
		double s_alive = 0;
		if (g > 2 * f) {
			double rad = R - t;
			for (double y1 = r; y1 < rad; y1 += g + 2 * r) {
				double y2 = y1 + g;
				for (double x1 = r; x1 < rad; x1 += g + 2 * r) {
					double x2 = x1 + g;
					s_alive += sq(x1 + f, x2 - f, y1 + f, y2 - f, rad - f);
				}
			}
			s_alive *= 4;
		}
		result = 1 - s_alive / s_total;
	}

	
int main()
{
    fin >> tnum;
	for (test = 0; test < tnum; test++) {
		readdata();
		run();
		outputdata();
	}
	return 0;
}
