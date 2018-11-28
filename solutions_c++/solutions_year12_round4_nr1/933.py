#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair <int, int> pii;

const int h = 10010;

int tests;
pii a[h];
int d[h], n;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d%d", &a[i].first, &a[i].second);
		scanf("%d", &a[n].first);
		a[n].second = 1;
		for (int i = 0; i <= n; i++)
			d[i] = 0;
		d[0] = a[0].first;
		for (int i = 0; i < n; i++) {
			for (int j = i+1; j <= n && a[j].first <= a[i].first + d[i]; j++)
				d[j] = max(d[j], min(a[j].first - a[i].first, a[j].second));
		}
		printf("Case #%d: %s\n", test, d[n] ? "YES" : "NO");
	}
	return 0;
}