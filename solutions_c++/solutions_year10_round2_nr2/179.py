#include <cstdio>
#include <algorithm>
using namespace std;

#define CODE B-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXN 55

int solve() {
	int n, k, b, t;
	int x[MAXN];
	int v[MAXN];
	scanf("%d%d%d%d", &n, &k, &b, &t);
	for (int i = 0; i < n; ++i)
		scanf("%d", &x[i]);
	for (int i = 0; i < n; ++i)
		scanf("%d", &v[i]);
	if (k == 0)
		return 0;
	bool dinner[MAXN];
	int swaps = 0;
	int tdinner = 0;
	for (int i = n-1; i >= 0; --i) {
		dinner[i] = false;
		if (x[i] + v[i] * t < b)
			continue;
		for (int j = i + 1; j < n; ++j) {
			if (v[i] <= v[j])
				continue;
			if (!dinner[j])
				swaps += 1;
		}
		dinner[i] = true;
		tdinner += 1;
		if (tdinner >= k)
			return swaps;
	}
	return -1;
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		int r = solve();
		if (r < 0)
			printf("Case #%d: IMPOSSIBLE\n", i);
		else
			printf("Case #%d: %d\n", i, r);
	}
	return 0;
}
