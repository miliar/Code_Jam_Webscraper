#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

typedef long double ldbl;

const ldbl EPS = 1e-9;
const ldbl PI = atan2(1, 1) * 4;

bool ldblLess(const ldbl x, const ldbl y) {
	return x + EPS <= y;
}

bool ldblEqual(const ldbl x, const ldbl y) {
	return (x < y + EPS) && (y < x + EPS);
}

ldbl cross(ldbl r, ldbl x) {
	if (!ldblLess(x, r)) return 0;
	return sqrt(r * r - x * x);
}

ldbl angle(ldbl x1, ldbl y1, ldbl x2, ldbl y2) {
	return atan2(abs(x1 * y2 - y1 * x2), abs(x1 * x2 + y1 * y2));
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		ldbl f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
		ldbl result = 0;
		if (2 * f <= g) {
			t += f;
			g -= 2 * f;
			r += f;
			R -= t;
			for (int i = 0; i < 1000; ++i) {
				for (int j = 0; j < 1000; ++j) {
					ldbl x1 = (g + 2 * r) * i + r;
					ldbl x2 = (g + 2 * r) * i + r + g;
					ldbl y1 = (g + 2 * r) * j + r;
					ldbl y2 = (g + 2 * r) * j + r + g;
					if (ldblLess(R * R, x1 * x1 + y1 * y1)) continue;
					if (!ldblLess(R * R, x2 * x2 + y2 * y2)) {
//						cout << i << " " << j << endl;
						result += g * g;
						continue;
					}
					vector<pair<ldbl, ldbl> > q;
					if (!ldblLess(R, x1)) {
						ldbl z = cross(R, x1);
						if (!ldblLess(y2, z) && !ldblLess(z, y1)) {
							q.push_back(make_pair(x1, z));
						}
					}
					if (!ldblLess(R, x2)) {
						ldbl z = cross(R, x2);
						if (!ldblLess(y2, z) && !ldblLess(z, y1)) {
							q.push_back(make_pair(x2, z));
						}
					}
					if (!ldblLess(R, y1)) {
						ldbl z = cross(R, y1);
						if (!ldblLess(x2, z) && !ldblLess(z, x1)) {
							q.push_back(make_pair(z, y1));
						}
					}
					if (!ldblLess(R, y2)) {
						ldbl z = cross(R, y2);
						if (!ldblLess(x2, z) && !ldblLess(z, x1)) {
							q.push_back(make_pair(z, y2));
						}
					}
					int n = 0;
					for (int k = 0; k < (int)q.size(); ++k) {
						bool f = !ldblEqual(q[k].first, x1) || !ldblEqual(q[k].second, y1);
						for (int l = 0; l < k; ++l) {
							if (ldblEqual(q[k].first, q[l].first) && ldblEqual(q[k].second, q[l].second)) {
								f = false;
								break;
							}
						}
						if (f) {
							q[n++] = q[k];
						}
					}
					if (n < 2) continue;
//					cout << n << " " << i << " " << j << endl;
					result += g * g;
					ldbl x0 = min(q[0].first, q[1].first);
					ldbl y0 = min(q[0].second, q[1].second);
					result -= (g - x0 + x1) * (g - y0 + y1);
					result += (R * R * angle(q[0].first, q[0].second, q[1].first, q[1].second) - abs(q[0].first * y0 - q[0].second * x0) - abs(q[1].first * y0 - q[1].second * x0)) * 0.5;
				}
			}
			R += t;
			result = result * 4 / (PI * R * R);
		}
		result = 1 - result;
		printf("Case #%d: %.6lf\n", tt + 1, (double)result);
	}
	return 0;
}
