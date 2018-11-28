#include <cstdio>

int main () {
	int T, N, I;
	int r;

	scanf("%i", &T);
	for (int t = 1; t <= T; ++t) {
		r = 0;
		scanf("%i", &N);
		for (int n = 1; n <= N; ++n) {
			scanf("%i", &I);
			if (I != n) {
				++r;
			}
		}
		printf("Case #%i: %i.000000\n", t, r);
	}
	return 0;
}

