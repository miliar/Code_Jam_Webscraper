#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 1010
#define MAXL 1000100

int n, l;
double vMin, vMax, t, v[MAXL];

void solve(int test) {
	memset(v, 0, sizeof(v));
	cin >> l >> vMin >> vMax >> t >> n;
	for (int i = 0; i < n; i++) {
		int x, y, z;
		cin >> x >> y >> z;
		for (int j = x; j < y; j++)
			v[j] = z;
	}
	sort(v, v + l);
	double ret = 0;
	for (int i = 0; i < l; i++)
		if (t > 0) {
			double v1 = v[i] + vMax;
			double v2 = v[i] + vMin;
			if (1.0 / v1 < t) {
				t -= 1.0 / v1;
				ret += 1.0 / v1;
			} else {
				ret += t + (1.0 - t * v1) / v2;
				t = 0;
			}
		} else
			ret += 1.0 / (v[i] + vMin);
	printf("Case #%d: %.9lf\n", test, ret);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;

	cin >> nTest;

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
