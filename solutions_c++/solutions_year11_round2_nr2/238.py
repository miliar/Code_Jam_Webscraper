#include <cstdio>
#include <vector>

using namespace std;

const int MAXN = 210;
const long long MAXV = 10000000000000LL;

int n, d;
long long sol;
pair <int, int> points[MAXN];

int works(long long t) {
	long long ant = points[0].first - t;

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < points[i].second; ++j) {
			if (i == 0 && j == 0)
				continue;

			ant = max(ant+d, points[i].first-t);
			if (ant > points[i].first + t)
				return 0;
		}

	return 1;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int t = 1; t <= tests; ++t) {
		scanf("%d %d", &n, &d);
		d *= 2;
		for (int i = 0; i < n; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			points[i] = make_pair(x*2, y);
		}


		long long front = 0, middle, back = MAXV;
		while (front <= back) {
			middle = (front+back) / 2;

			if (works(middle)) {
				sol = middle;
				back = middle-1;
			} else {
				front = middle+1;
			}
		}

		printf("Case #%d: %lf\n", t, (double) sol/2);
	}

	return 0;
}
