#include <cstdio>

int main(void) {
	int n, b, k;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		scanf("%d %d", &b, &k);
		int p = 1<<b;
		printf("Case #%d: %s\n", i, (k+1)%p?"OFF":"ON");
	}
	return 0;
}