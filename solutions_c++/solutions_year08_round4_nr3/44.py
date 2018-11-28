#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
#include <cstring>

using namespace std;
static const double EPS = 1e-8;
typedef long long ll;

struct SHIP
{
	double x, y, z, p;

	double power(double xx, double yy, double zz)
	{
		return (abs(x - xx) + abs(y - yy) + abs(z - zz)) / p;
	}
};

int main() {
	int T;
	cin >> T;

	for (int testCase = 1; testCase <= T; ++testCase){
		int N;
		cin >> N;
		SHIP ships[1024];
		for (int i = 0; i < N; ++i){
			cin >> ships[i].x >> ships[i].y >> ships[i].z >> ships[i].p;
		}

		double delta = 1e6;

		double x = 0, y = 0, z = 0;
		while (delta > 1e-8){
			double nextX, nextY, nextZ;
			double minValue = 1e10;

			for (int dx = -1; dx <= 1; ++dx){
				const double xx = x + delta * dx;

				for (int dy = -1; dy <= 1; ++dy){
					const double yy = y + delta * dy;

					for (int dz = -1; dz <= 1; ++dz){
						const double zz = z + delta * dz;

						double maxPower = 0;
						for (int i = 0; i < N; ++i){
							const double power = ships[i].power(xx, yy, zz);
							maxPower = max(maxPower, power);
						}

						if (minValue > maxPower){
							minValue = maxPower;
							nextX = xx;
							nextY = yy;
							nextZ = zz;
						}
					}
				}
			}

			x = nextX;
			y = nextY;
			z = nextZ;
			delta *= sqrt(0.5);
		}

		double maxPower = 0;
		for (int i = 0; i < N; ++i){
			const double power = ships[i].power(x, y, z);
			maxPower = max(maxPower, power);
		}

		printf("Case #%d: %.20lf\n", testCase, maxPower);
	}
}
