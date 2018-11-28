#include <stdio.h>
#include <string.h>

void process() {
	int n;
	int cur;
	double res;
	scanf("%d", &n);
	res = 0.0;
	for (int i = 1; i <= n; ++i) {
		scanf("%d", &cur);
		if (i != cur) {
			res += 1.0;
		}
	}
	printf("%0.6lf", res);
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
