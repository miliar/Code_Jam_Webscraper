#include <cstdio>

int main(void) {
	int T, N, C;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs) {
		int minC = 1 << 29, sumC = 0, xorC = 0;
		scanf("%d", &N);
		while (N--) {
			scanf("%d", &C);
			if (minC > C) minC = C;
			sumC += C;
			xorC ^= C;
		}
		printf("Case #%d: ", cs);
		if (xorC) puts("NO");
		else printf("%d\n", sumC-minC);
	}
	return 0;
}
