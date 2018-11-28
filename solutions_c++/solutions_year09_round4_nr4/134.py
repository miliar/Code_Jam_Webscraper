#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int X[50], Y[50], R[50];
int N;

double sqr(int x) {
	return x * x;
}

double dist(int x1, int y1, int x2, int y2) {
	return sqrt(sqr(x1 - x2) + sqr(y1 - y2));
}

void init() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d%d%d", &X[i], &Y[i], &R[i]);
	}
}

void solve() {
	if (N == 1) printf("%d\n", R[0]);
	else if (N == 2) printf("%d\n", max(R[0], R[1]));
	else if (N == 3) {
		double ans = 1e10;

		for (int i = 0; i < 3; i++) {
			int i2 = (i + 1) % 3;
			int i3 = (i + 2) % 3;
			
			if (R[i2] < R[i3]) swap(i2, i3);

			double cur = (max(dist(X[i2], Y[i2], X[i3], Y[i3]) + R[i3], double(R[i2])) + R[i2]) / 2;
			cur = max(cur, double(R[i]));

			ans = min(cur, ans);
		}
			
		printf("%lf\n", ans);
	}
}

int main() {
	freopen("p4a.in", "r", stdin);
	freopen("p4a.out", "w", stdout);

	int Case; scanf("%d", &Case);
	for (int i = 0; i < Case; i++) {
		init();
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}

