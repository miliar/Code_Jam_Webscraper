#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 16;

double x[MAXN], y[MAXN], r[MAXN];

double go(int i, int j)
{
	double dx = x[i] - x[j];
	double dy = y[i] - y[j];
	double dd = sqrt(dx * dx + dy * dy);
	dd += r[i] + r[j];
	return dd / 2;
}

double run()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%lf %lf %lf", x + i, y + i, r + i);
	}
	if (n == 1) {
		return r[0];
	}
	if (n == 2) {
		return max(r[0], r[1]);
	}
	double minr = 1e100;
	for (int i = 0; i < 3; ++i) {
		double tt = go((i + 1) % 3, (i + 2) % 3);
		double rrr = max(r[i], tt);
		if (rrr < minr) minr = rrr;
	}
	return minr;
}

int main()
{
	freopen("Din.txt", "r", stdin);
	freopen("Dout.txt", "w", stdout);
	int c;
	scanf("%d", &c);
	for (int i = 1; i <= c; ++i) {
		printf("Case #%d: %.6lf\n", i, run());
	}
	return 0;
}