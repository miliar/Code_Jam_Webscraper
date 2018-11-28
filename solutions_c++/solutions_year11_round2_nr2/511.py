#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int h = 222;

int T, n, D;
pii a[h];

bool g(double m) {
	double e[h];
	double pr = -1000000000.;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < a[i].second; j++)
			if (a[i].first < pr + D) {
				if (pr + D - a[i].first > m)
					return 0;
				pr += D;
			} else {
				pr = max(pr + D, a[i].first - m);
			}
	return 1;
}

double sol(double l, double r) {
	double m;
	for (int t = 0; t < 200; t++) {
		m = (l + r) / 2.;
		if (g(m))
			r = m;
		else
			l = m;
	}
	return m;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d%d", &n, &D);
		for (int i = 0; i < n; i++)
			scanf("%d%d", &a[i].first, &a[i].second);
		printf("Case #%d: %.8lf\n", t+1, sol(0., 1000000000.));
	}
	return 0;
}