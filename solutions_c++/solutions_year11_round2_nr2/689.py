#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int d, c;
int pv[1000000][2];

bool inDis(double a, double b, double dis) {
	double dif;
	if (a < b) dif = b - a;
	else dif = a - b;
	if (dif < dis + 1e-12) return true;
	else return false;
}

bool canGet(double dis) {
	double last = pv[0][0] - dis;
	for (int i = 0; i < d; ++i) {
		if (last < pv[i][0] - dis) {
			last = pv[i][0] - dis;
		}
		if (!inDis(last + (pv[i][1] - 1) * c, pv[i][0], dis)) {
			return false;
		}
		last += pv[i][1] * c;
	}
	return true;
}

void process() {
	int sum = 0;
	scanf("%d%d", &d, &c);
	for (int i = 0; i < d; ++i) {
		scanf("%d%d", &pv[i][0], &pv[i][1]);
		sum += pv[i][1];
	}
	double mn = 0, mx = (sum - 1) * c, mid;
	while (mx - mn > 1e-12) {
		mid = (mx + mn) / 2.0;
		if (canGet(mid)) {
			mx = mid;
		} else {
			mn = mid;
		}
	}
	printf("%.9lf\n", mx);
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t = 1; t <= cas; ++t) {
		printf("Case #%d: ", t);
		process();
	}
	return 0;
}
