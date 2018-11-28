#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

double x[100], y[100], r[100];
bool hash[100];
int list[100];
int N, size;

int doubleCmp(double a, double b) {
	if (fabs(a - b) < 1e-6) return 0;
	return a < b ? -1 : 1;
}

double sqr(double x) {
	return x * x;
}

bool inCircle(double xt, double yt, double R) {
	for (int i = 0; i < size; i++)
		if (doubleCmp(sqrt(sqr(xt - x[list[i]]) + sqr(yt - y[list[i]])), R - r[list[i]]) > 0) return false;
	return true;
}

bool check(double R) {
	for (int i = 0; i < size; i++)
		if (doubleCmp(r[list[i]], R) > 0) return false;
	for (int i = 0; i < size; i++) if (inCircle(x[list[i]], y[list[i]], R))
		return true;
	for (int i = 0; i < size; i++)
		for (int j = i + 1; j < size; j++) {
			int p = list[i], q = list[j];
			if (doubleCmp(sqrt(sqr(x[p] - x[q]) + sqr(y[p] - y[q])), 2 * R - r[p] - r[q]) > 0) return false;
			if (doubleCmp(sqrt(sqr(x[p] - x[q]) + sqr(y[p] - y[q])), fabs(r[p] - r[q])) < 0) continue;
			double a1 = -2 * x[p] + 2 * x[q], b1 = -2 * y[p] + 2 * y[q];
			double c1 = sqr(x[p]) + sqr(y[p]) - sqr(R - r[p]) - (sqr(x[q]) + sqr(y[q]) - sqr(R - r[q]));
			double a2 = y[p] - y[q], b2 = x[q] - x[p], c2 = -a2 * x[p] - b2 * y[p];
			double xd = (-c1 * b2 + c2 * b1) / (a1 * b2 - a2 * b1);
			double yd = (-c1 * a2 + c2 * a1) / (b1 * a2 - b2 * a1);
			double a = y[p] - y[q], b = x[q] - x[p];
			double len = sqrt(sqr(a) + sqr(b));
			a /= len; b /= len;
			len = sqrt(fabs(sqr(R - r[p]) - sqr(xd - x[p]) - sqr(yd - y[p])));
			a *= len; b *= len;
			if (inCircle(xd + a, yd + b, R)) return true;
			if (inCircle(xd - a, yd - b, R)) return true;
		}
	return false;
}

double solve() {
	double Min = 0.0, Max = 1e20, Mid;
	while (Max - Min > 1e-6) {
		Mid = (Min + Max) / 2;
		if (check(Mid)) Max = Mid;
		else Min = Mid;
	}
	return Min;
}

int main() {
	int caseSize;
	scanf("%d", &caseSize);
	for (int T = 1; T <= caseSize; T++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
		if (N == 1) {
			printf("Case #%d: %lf\n", T, r[0]);
			continue;
		}
		if (N == 2) {
			printf("Case #%d: %lf\n", T, max(r[0], r[1]));
			continue;
		}
		double result = 1e30;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++) if (i != j) {
				memset(hash, false, sizeof(hash));
				for (int k = 0; k < N; k++)
					if (doubleCmp((x[k] - x[i]) * (y[j] - y[i]), (x[j] - x[i]) * (y[k] - y[i])) > 0 ||
						doubleCmp((x[k] - x[i]) * (y[j] - y[i]), (x[j] - x[i]) * (y[k] - y[i])) == 0 &&
						doubleCmp((x[k] - x[i]) * (x[j] - x[i]) + (y[j] - y[i]) * (y[k] - y[i]), 0.0) >= 0) hash[k] = true;
				size = 0;
				for (int k = 0; k < N; k++)
					if (hash[k]) list[size++] = k;
				double temp = solve();
				size = 0;
				for (int k = 0; k < N; k++)
					if (!hash[k]) list[size++] = k;
				temp = max(temp, solve());
				result = min(result, temp);
			}
		printf("Case #%d: %lf\n", T, result);
	}
	return 0;
}
