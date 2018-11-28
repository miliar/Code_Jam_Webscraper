#include <cstdio>
#include <algorithm>
using namespace std;

int solve() {
	int n, s, p, t[32] = {0}, result0 = 0, result1 = 0;
	scanf("%d%d%d", &n, &s, &p);
	for (int i = 0, tmp; i < n; ++ i) {
		scanf("%d", &tmp);
		++ t[tmp];
	}
	if (p == 0) {
		result1 = n;
	} else if (p == 1) {
		result1 = n - t[0];
	} else {
		result0 = t[3 * (p - 1) - 1] + t[3 * (p - 1)];
		for (int i = 3 * (p - 1) + 1; i <= 30; ++ i) {
			result1 += t[i];
		}
	}
	return min(result0, s) + result1;
}

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		printf("Case #%d: %d\n", t, solve());
	}
	return 0;
}
