#include <stdio.h>
#include <string.h>

void process() {
	long long n;
	int pd, pg;
	int d;
	scanf("%I64d %d %d", &n, &pd, &pg);
	for (d = 1; d <= 100; ++d) {
		if ((d * pd) % 100 == 0) break;
	}
	if (d > n) {
		printf("Broken\n");
		return;
	}
	if (pg == 100 && pd != 100) {
		printf("Broken\n");
		return;
	}
	if (pg == 0 && pd != 0) {
		printf("Broken\n");
		return;
	}
	printf("Possible\n");
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t = 1; t <= cas; ++t) {
		printf("Case #%d: ", t);
		process();
	}
	return 0;
}
