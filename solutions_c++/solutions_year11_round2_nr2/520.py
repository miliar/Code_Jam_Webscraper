#include <cstdio>
#include <algorithm>

using namespace std;

int points[1000000];
int N, D;

bool process(double l) {
	double last = -1e20;
	for (int i = 0; i < N; i++) {
		double pos = points[i];

		double left = pos - l;
		double right = pos + l;

		last = last + D;

		if (right < last - 1e-10) return false;
		last = max(last, left);
	}

	return true;
}

void solve() {
	N = 0;

	int C; scanf("%d%d", &C, &D);
	for (int i = 0; i < C; i++) {
		int pos, count; scanf("%d%d", &pos, &count);
		for (int j = 0; j < count; j++)
			points[N++] = pos;
	}

	sort(points, points + N);

	double left = 0, right = 1e20;
	while (right - left > 1e-8) {
		double mid = (right + left) / 2;
		if (process(mid)) right = mid;
		else left = mid;
	}

	printf("%.8lf\n", left);
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
