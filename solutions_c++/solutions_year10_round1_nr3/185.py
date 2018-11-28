#include <cstdio>
#include <algorithm>

bool wins(int a, int b) {
	if (a < b) {
		std::swap(a, b);
	}
	if (b == 0) {
		return true;
	}
	if (!wins(a % b, b)) {
		return true;
	}
	return a >= 2 * b;
}

int main() {
	freopen("game.in", "r", stdin);
	freopen("game.out", "w", stdout);
	int t = 0;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ti++) {
		int a1, a2, b1, b2;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		long long res = 0;
		for (int a = a1; a <= a2; a++) {
			for (int b = b1; b <= b2; b++) {
				res += wins(a, b);
			}
		}
		printf("Case #%d: %lld\n", ti + 1, res);
	}
	return 0;
}
