#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
using namespace std;

static const double pi = acos(-1);

double dist(double x, double y) {
	return sqrt(x*x + y*y);
}

double prob(double f, double R, double t, double r, double g) {
	double total = pi * R * R;
	r += f;
	t += f;
	g -= 2*f;
	if (g <= 0) g = 0;
	R -= t;
	double RR = R * R;
	double inner = pi * RR;
	double empty = 0;
	
	double side = g;
	double SS = side * side;
	double inc = side + 2 * r;
	for (double x = r; x < R; x += inc) {
		for (double y = r; dist(x, y) < R; y += inc) {
			double x2 = x + side;
			double y2 = y + side;
			
			if (dist(x2, y2) <= R) {
				empty += SS;
			} else {
				if (dist(x2, y) > R) {
					x2 = sqrt((R - y)*(R + y));
				}
				if (dist(x, y2) > R) {
					y2 = sqrt((R - x)*(R + x));
				}
				
				double x1 = sqrt((R - y2) * (R + y2));
				double y1 = sqrt((R - x2) * (R + x2));
				
				double bigger = (x1 - x) * (y2 - y);
				double smaller = (x2 - x1) * (y1 - y);
				
				double angle = acos((x1 * x2 + y1 * y2) / RR);
				double sector = angle / (2 * pi) * inner;

				double width = x2 - x1;
				double height = y2 - y1;
				
				double triangle = width * height / 2;
				
				double halfBaseSquared = (width * width + height * height) / 4;
				double halfBase = sqrt(halfBaseSquared);
				double segment = sqrt(RR - halfBaseSquared) * halfBase;
				double arc = sector - segment;
				
				empty += bigger + smaller + triangle + arc;
			}
		}
	}
	
	return 1 - (4 * empty / total);
}

int main (int argc, char const *argv[])
{
	int nCases;
	cin >> nCases;
	for (int n = 1; n <= nCases; n++) {
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
		
		cout << "Case #" << n << ": "
		     << fixed << setprecision(6) << prob(f, R, t, r, g) << endl;
	}
	
	return 0;
}