#include <iostream>
#include <algorithm>
using namespace std;

int d, c;
int v[30], p[30];

bool judge(double time) {

	if (time < 0)	return false;

	double west = -10000000;

	for (int i = 0; i < c; ++i) {
		if (p[i] - west > time) {
			if (time * 2 / d + 1 < v[i]) {
				return false;
			}
			else {
				west = p[i] - time + (v[i] - 1) * d;
			}
		} else {
			if ((p[i] - west + time) / d  < v[i] ){
				return false;
			}
			else {
				west = west + v[i] * d;
			}
		}
	}

	return true;
}

int main() {
	int t;
	double result;

	freopen("BBB.in", "r", stdin);
	freopen("out2.txt", "w", stdout);

	scanf ("%d", &t);

	for (int ii = 1; ii <= t; ++ii) {
		int num = 0;
		scanf ("%d%d", &c, &d);

		for (int i = 0; i < c; ++i) {
			scanf ("%d%d", &p[i], &v[i]); 
			num += v[i];
		}

		int mid;
		int left = 0, right = num * d;

		while (left < right) {
			mid = (left + right) >> 1;

			if (judge((double)mid)) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}

		result = right;
		if (judge(right - 0.5)) {
			result = right - 0.5;
		}

		printf("Case #%d: %.6lf\n", ii, result);
	}
}