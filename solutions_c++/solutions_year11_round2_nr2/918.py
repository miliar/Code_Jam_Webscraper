#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define EPS 1e-9
#define MAXN 200
#define MAXM 1000000
#define INF 1e9

int n, d, x[MAXN + 5], a[MAXN + 5];
double y[MAXM + 5];

bool ok(double time) {
	int m = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < a[i]; j++)
			y[m++] = x[i];

	//	for (int i = 0; i < m; i++)
	//		cout << y[i] << ' ';
	//	cout << endl;

	y[0] -= time;
	y[m - 1] += time;
	int i, j;
	i = 1;
	j = m - 2;
	while (i <= j) {
		if (i == j) {
			double u = y[i];
			y[i] = max(y[i - 1] + d, y[i] - time);
			if (fabs(u - y[i]) > time + EPS)
				return false;
		} else {
			double u = y[i];
			double v = y[j];
			y[i] = max(y[i - 1] + d, y[i] - time);
			y[j] = min(y[j + 1] - d, y[j] + time);
			if (fabs(u - y[i]) > time + EPS)
				return false;
			if (fabs(v - y[j]) > time + EPS)
				return false;
		}
		i++;
		j--;
	}
	//	for (int i = 0; i < m; i++)
	//		cout << y[i] << ' ';
	//	cout << endl;
	for (int i = 1; i < m; i++)
		if (y[i] - y[i - 1] < d - EPS)
			return false;
	return true;
}

void solve(int test) {
	scanf("%d%d", &n, &d);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &x[i], &a[i]);

	//	if (test == 7) {
	//		cout << "----" << endl;
	//		cout << d << endl;
	//		for (int i = 0; i < n; i++)
	//			cout << x[i] << ' ' << a[i] << endl;
	//		cout << "----" << endl;
	//	}

	//	cout << ok(4) << endl;

	double low = 0;
	double high = INF;

	while (high - low >= EPS) {
		double mid = (low + high) / 2;
		if (ok(mid))
			high = mid;
		else
			low = mid;
	}

	printf("Case #%d: %.6lf\n", test, high);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	scanf("%d", &nTest);

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
