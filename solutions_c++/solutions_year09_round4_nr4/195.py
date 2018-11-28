#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int x[4], y[4], r[4];

double get(int i, int j, int k)
{
	double tmp = hypot((double) x[i] - x[j], (double) y[i] - y[j]);
	return max<double>((tmp + r[i] + r[j]) / 2, r[k]);
}

int main()
{
	int T, n;

	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);

	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d %d", &x[i], &y[i], &r[i]);
		}
		double res = 1e10;
		if (n == 1)
			res = r[0];
		else if (n == 2)
			res = max(r[0], r[1]);
		else {
			res = min(res, get(0, 1, 2));
			res = min(res, get(0, 2, 1));
			res = min(res, get(1, 2, 0));
		}
		printf("Case #%d: %.6lf\n", t + 1, res);
	}
	return 0;
}