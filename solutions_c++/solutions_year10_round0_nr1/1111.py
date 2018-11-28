#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", i);
		if ((k % (1<<n)) == ((1<<n) - 1)) {
			printf("ON");
		} else {
			printf("OFF");
		}
		printf("\n");
	}
}
