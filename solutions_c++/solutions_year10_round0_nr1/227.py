#include <cstdio>

int T, n, k;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &k);
		if (k + 1 << 32 - n) puts("OFF");
		else puts("ON");
	}
	return 0;
}
