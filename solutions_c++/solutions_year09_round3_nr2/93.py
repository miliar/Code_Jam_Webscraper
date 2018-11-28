#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace std;

#ifdef WIN32
//ifstream in("B-small.in");
ifstream in("B-large.in");
#define cin in
//ofstream out("B-small.out");
ofstream out("B-large.out");
#define cout out
#endif

const double eps = 1e-8;

int main()
{
	int t, ca = 0;
	for (cin >> t; t; --t) {
		int n;
		double xyz[510][3];
		double dd[510][3];
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> xyz[i][0] >> xyz[i][1] >> xyz[i][2];
			cin >> dd[i][0] >> dd[i][1] >> dd[i][2];
		}

		double sum[3] = {0, 0, 0}, sumd[3] = {0, 0, 0};
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < 3; ++j) {
				sum[j] += xyz[i][j];
				sumd[j] += dd[i][j];
			}
		}

		double a = double(sumd[0] * sumd[0] + sumd[1] * sumd[1] + sumd[2] * sumd[2]) / n / n;
		double c = double(sum[0] * sum[0] + sum[1] * sum[1] + sum[2] * sum[2]) / n / n;
		double b = double(2 * (sum[0] * sumd[0] + sum[1] * sumd[1] + sum[2] * sumd[2])) / n / n;
		double delta = b * b - 4 * a * c;
		double res[2];
		if (fabs(a) < eps) { // if a ==0
			if (b > -eps) { // if b >= 0
				res[0] = c, res[1] = 0;
			} else { // if b < 0
				res[0] = 0, res[1] = -c/b;
			}
		} else if (delta >= 0) {
			double t1 = (-b-delta) / 2.0 / a, t2 = (-b+delta) / 2.0 / a;
			if (t1 > t2) swap(t1, t2);
			if (t1 > -eps) res[0] = 0, res[1] = t1;
			else if (t2 > -eps) res[0] = 0, res[1] = t2;
			else res[0] = c, res[1] = 0;
		} else if (-b/(2*a) > 0) {
			res[0] = -delta/(4*a), res[1] = -b/(2*a);
		} else res[0] = c, res[1] = 0;

		cout.precision(8); cout.setf(ios::fixed);
		cout << "Case #" << ++ca << ": " << sqrt(res[0]) << " " << res[1] << endl;
	}
	return 0;
}
