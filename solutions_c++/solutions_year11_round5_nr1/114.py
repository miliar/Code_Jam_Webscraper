#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Illegular Cakes

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int W, L, U, G;
		cin >> W >> L >> U >> G;
		vector <int> x;
		vector <int> lx(L);
		vector <int> ly(L);
		for (int i = 0; i < L; i++) {
			cin >> lx[i] >> ly[i];
			x.push_back(lx[i]);
		}
		vector <int> ux(U);
		vector <int> uy(U);
		for (int i = 0; i < U; i++) {
			cin >> ux[i] >> uy[i];
			x.push_back(ux[i]);
		}
		sort(x.begin(), x.end());
		vector <double> y;
		for (int i = 0; i < x.size(); i++) {
			double cy = 0;
			for (int j = 0; j < L - 1; j++) {
				if (x[i] >= lx[j] && x[i] <= lx[j + 1]) {
					cy -= ly[j];
					if (lx[j + 1] - lx[j] > 0) {
						cy -= (double)(ly[j + 1] - ly[j]) * (x[i] - lx[j]) / (lx[j + 1] - lx[j]);
					}
					break;
				}
			}
			for (int j = 0; j < U - 1; j++) {
				if (x[i] >= ux[j] && x[i] <= ux[j + 1]) {
					cy += uy[j];
					if (ux[j + 1] - ux[j] > 0) {
						cy += (double)(uy[j + 1] - uy[j]) * (x[i] - ux[j]) / (ux[j + 1] - ux[j]);
					}
					break;
				}
			}
			y.push_back(cy);
		}
		double area = 0;
		for (int i = 0; i < x.size() - 1; i++) {
			area += (y[i] + y[i + 1]) * (x[i + 1] - x[i]);
		}
		cout << "Case #" << caseno << ":" << setprecision(9) << endl;
		for (int g = 1; g < G; g++) {
			double a = 0;
			double target = area * g / G;
			for (int i = 0; i < x.size() - 1; i++) {
				double add = (y[i] + y[i + 1]) * (x[i + 1] - x[i]);
				if (a + add >= target) {
					double dx = x[i + 1] - x[i];
					double dy = y[i + 1] - y[i];
					if (dy != 0) {
						double tx = (sqrt(y[i] * y[i] + dy * (target - a) / dx) - y[i]) / (dy / dx);
						cout << (x[i] + tx) << endl;
					} else {
						double tx = (target - a) / y[i] / 2;
						cout << (x[i] + tx) << endl;
					}
					break;
				}
				a += add;
			}
		}
	}

	return 0;
}
