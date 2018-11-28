#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cmath>
#include <complex>
#include <vector>
#include <algorithm>
using namespace std;

typedef complex<double> point;

const double EPS = 1e-12;

inline bool getCenter(point c1, double r1, point c2, double r2, point c3, double r3, point& out) {
	out = (c1+c2+c3)/3.0;
	for (int i = 0; i < 100; i++) {
		double t;
		if ((t = abs(out - c1)) > r1 + EPS) {
			out = c1 + (out-c1)/t*r1;
		} else if ((t = abs(out - c2)) > r2 + EPS) {
			out = c2 + (out-c2)/t*r2;
		} else if ((t = abs(out - c3)) > r3 + EPS) {
			out = c3 + (out-c3)/t*r3;
		} else {
			return true;
		}
	}
	return false;
}

int main(int argc, char* argv[]) {
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int numTestCases;
	scanf("%d", &numTestCases);
	for (int testCase = 1; testCase <= numTestCases; testCase++) {
		int n;
		scanf("%d", &n);
		vector<point> centers;
		vector<double> radii;
		for (int i = 0; i < n; i++) {
			int x, y, r;
			scanf("%d%d%d", &x, &y, &r);
			centers.push_back(point(x, y));
			radii.push_back(r);
		}
		vector< vector< vector<int> > > mask(n, vector< vector<int> >(n, vector<int>(n, 0)));
		vector< vector< vector<double> > > rad(n, vector< vector<double> >(n, vector<double>(n, 0)));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					// Binsearch for radius and center.
					double left = max(radii[i], max(radii[j], radii[k]));
					double right = left + abs(centers[i]-centers[j]) + abs(centers[i]-centers[k]);
					point center = (centers[i]+centers[j]+centers[k])/3.0;
					while (right - left > 1e-7) {
						double r = (left + right)/2;
						if (getCenter(centers[i], r - radii[i], centers[j], r - radii[j], centers[k], r - radii[k], center)) {
							right = r;
						} else {
							left = r;
						}
					}
					// Find which other points can be inside
					rad[i][j][k] = right;
					getCenter(centers[i], right - radii[i], centers[j], right - radii[j], centers[k], right - radii[k], center);
					int t = 1;
					mask[i][j][k] = 0;
					for (int l = 0; l < n; l++, t*=2) {
						if (abs(center - centers[l]) < rad[i][j][k] - radii[l] + EPS)
							mask[i][j][k] |= t;
					}
				}
			}
		}
		double res = 1e+20;
		int reqmask = (1<<n) - 1;
		for (int i1 = 0; i1 < n; i1++) {
			for (int j1 = 0; j1 < n; j1++) {
				for (int k1 = 0; k1 < n; k1++) {
					for (int i2 = 0; i2 < n; i2++) {
						for (int j2 = 0; j2 < n; j2++) {
							for (int k2 = 0; k2 < n; k2++) {
								if ((mask[i1][j1][k1] | mask[i2][j2][k2]) == reqmask) {
									res = min(res, max(rad[i1][j1][k1], rad[i2][j2][k2]));
								}
							}
						}
					}
				}
			}
		}
		printf("Case #%d: %.6lf\n", testCase, res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
