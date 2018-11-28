#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const double PI = 3.1415926535897932384626433832795;

int N;
double f, R, t, r, g;

void read_data () {
	cin >> f >> R >> t >> r >> g;
}

double get_area (double x1, double y1, double x2, double y2, double r) {
	if (x1 >= x2 || y1 >= y2) return 0.0;
	if (x1*x1 + y1*y1 >= r*r) return 0.0;
	if (x2*x2 + y2*y2 <= r*r) return (x2-x1)*(y2-y1);

	double tx1 = -1.0, tx2 = -1.0;
	if (y2 <= r && x1 < sqrt (r*r-y2*y2) && x2 > sqrt (r*r-y2*y2)) tx1 = sqrt (r*r-y2*y2);
	if (y1 <= r && x1 < sqrt (r*r-y1*y1) && x2 > sqrt (r*r-y1*y1)) tx2 = sqrt (r*r-y1*y1);

	double ty1 = -1.0, ty2 = -1.0;
	if (x2 <= r && y1 < sqrt (r*r-x2*x2) && y2 > sqrt (r*r-x2*x2)) ty1 = sqrt (r*r-x2*x2);
	if (x1 <= r && y1 < sqrt (r*r-x1*x1) && y2 > sqrt (r*r-x1*x1)) ty2 = sqrt (r*r-x1*x1);

	double area = 0.0;
	if (tx1 >= 0.0) { area += (tx1-x1)*(y2-y1); x1 = tx1; }
	if (tx2 >= 0.0) { x2 = tx2; }

	if (ty1 >= 0.0) { area += (ty1-y1)*(x2-x1); y1 = ty1; }
	if (ty2 >= 0.0) { y2 = ty2; }

	double angle = atan2 (y2, x1) - atan2 (y1, x2);
	area += (r*r*angle - x1*(y2-y1) - y1*(x2-x1)) * 0.5;

	return area;
}

void solve () {
	double safe_area = 0.0;

	for (int i = 0; (2*i+1)*r+g*i <= R; ++i)
		for (int j = 0; (2*j+1)*r+g*j <= R; ++j) {
			safe_area += get_area ((2*j+1)*r+g*j+f, (2*i+1)*r+g*i+f, (2*j+1)*r+g*(j+1)-f, (2*i+1)*r+g*(i+1)-f, R-t-f);
		}

	cout << setiosflags (ios::fixed) << setprecision (6) << 1.0 - 4.0*safe_area / (PI*R*R) << endl;
}

int main () {
	cin >> N;

	for (int t = 0; t < N; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
