#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 1000 + 10;
int b[MAXN], e[MAXN], w[MAXN];
pair<int, int> a[MAXN];

int main() {
	int nCase;
	scanf("%d", &nCase);

	for (int re = 1; re <= nCase; ++re) {
		int s, r, x, T, n, left;
		scanf("%d%d%d%d%d", &x, &s, &r, &T, &n);
		left = x;

		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &b[i], &e[i], &w[i]);
			a[i] = make_pair(w[i], e[i] - b[i]);
			left -= e[i] - b[i];
		}

		a[n] = make_pair(0, left);
		n++;

		sort(a, a + n);

		double ans = 0;
		double t = T;

		for (int i = 0; i < n; ++i) {
			if (t <= 0) {
				ans += a[i].second * 1.0 / (a[i].first + s);
				continue;
			}
			double tt = a[i].second * 1.0 / (a[i].first + r);
			if (tt <= t) {
				t -= tt;
				ans += tt;
			} else {
				double rest = a[i].second - (a[i].first + r) * t;
				ans += t;
				ans += rest / (a[i].first + s);
				t = 0;
			}
		}
		printf("Case #%d: %.15lf\n", re, ans);
	}

	return 0;
}
