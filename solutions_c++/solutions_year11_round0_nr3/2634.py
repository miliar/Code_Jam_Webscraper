#include <cstdio>

#define MAX_C 1000000

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n;
		scanf("%d", &n);
		int x = 0;
		int sum = 0;
		int min = MAX_C;
		while (n--) {
			int c;
			scanf("%d", &c);
			x ^= c;
			sum += c;
			if (c < min) min = c;
		}
		printf("Case #%d: ", i);
		if (x) printf("NO\n");
		else printf("%d\n", sum - min);
	}
	return 0;
}
