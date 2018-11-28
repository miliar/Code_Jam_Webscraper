#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		int n;
		int sum = 0, x = 0, min = 1e7;
		scanf("%d", &n);
		while (n--) {
			int v;
			scanf("%d", &v);
			sum += v;
			x ^= v;
			if (min > v)
				min = v;
		}
		if (x)
			printf("Case #%d: NO\n", Ti);
		else
			printf("Case #%d: %d\n", Ti, sum - min);
	}
}
