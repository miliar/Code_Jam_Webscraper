#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define SQR(x) ((x)*(x))

double solve() {
	int n, x[3], y[3], r[3];
	scanf("%d", &n);
	if (n > 3) return 0;
	for (int i = 0; i < n; ++i)
		scanf("%d%d%d", x+i, y+i, r+i);
	double res = 1e18;
	if (n == 1) return r[0];
	if (n == 2) return max(r[0], r[1]);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) if (i != j)
			for (int k = 0; k < n; ++k) if (i != k && j != k)
				res = min(res,
					max(r[i] + 0.0, r[j] + r[k] + sqrt(SQR(x[j]-x[k])+SQR(y[j]-y[k])+0.0)));
	return res / 2;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: %.9lf\n", i+1, solve());
	}
}