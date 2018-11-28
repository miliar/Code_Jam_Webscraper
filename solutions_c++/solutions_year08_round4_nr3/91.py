#include <iostream>
#include <iomanip>
#include <vector>
#include <limits>
#include <cmath>

using namespace std;

const double INF = numeric_limits<double>::infinity();
const double EPS = 1e-08;

struct Point
{
	double x;
	double y;
	double z;
	double p;
public:
	Point(double x, double y, double z, double p) : x(x), y(y), z(z),p(p) { }
	Point() { }
};

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int n;
		cin >> n;

		vector<Point> v(n);

		for(int i = 0; i < n; i++) {
			cin >> v[i].x >> v[i].y >> v[i].z >> v[i].p;
		}

		double x = v[0].x;
		double y = v[0].y;
		double z = v[0].z;

		double dmax = 0.0;
		double mult = 0.5;

		while(mult > EPS) {
			dmax = 0.0;

			int j = 0;

			for(int i = 0; i < n; i++) {
				double dx = v[i].x - x;
				double dy = v[i].y - y;
				double dz = v[i].z - z;
				double dist = (fabs(dx) + fabs(dy) + fabs(dz)) / v[i].p;
				if(dmax < dist) { dmax = dist; j = i; }
			}

			x += (v[j].x - x) * mult;
			y += (v[j].y - y) * mult;
			z += (v[j].z - z) * mult;

			mult *= 0.9365;
		}

		cout << "Case #" << iCase << ": "
			 << setprecision(7) << fixed << dmax << endl;
	}

	return 0;
}
