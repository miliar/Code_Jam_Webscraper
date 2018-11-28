#include <cstdio>

int main() {
	int T, N, C, min, xorsum, sum;

	scanf("%i", &T);
	for (int t = 1; t <= T; ++t) {
		min = 1000001;
		xorsum = 0;
		sum = 0;
		scanf("%i", &N);
		while (N--) {
			scanf("%i", &C);
			if (min > C) {
				min = C;
			}
			xorsum ^= C;
			sum += C;
		}
		printf("Case #%i: ", t);
		if (xorsum) {
			printf("NO\n", t);
		} else {
			printf("%i\n", sum - min);
		}
	}
	return 0;
}

