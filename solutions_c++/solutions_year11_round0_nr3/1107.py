#include <stdio.h>
#include <string.h>

void process() {
	int n;
	int sum, min, cur, bs;
	scanf("%d", &n);
	sum = bs = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &cur);
		if (i == 0) min = cur;
		else if (cur < min) min = cur;
		sum += cur;
		bs ^= cur;
	}
	if (bs == 0) printf("%d", sum - min);
	else printf("NO");
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		printf("Case #%d: ", i);
		process();
		printf("\n");
	}
	return 0;
}
