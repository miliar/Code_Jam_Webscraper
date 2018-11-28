#include <cstdio>

int main() {
	int ntests;
	int n;

	scanf("%d", &ntests);
	for (int test = 1; test <= ntests; test++) {
		scanf("%d", &n);
		
		int res = n;
		
		for (int i = 1; i <= n; i++) {
			int c;
			scanf("%d", &c);

			if (c == i) {
				res--;
			}
		}
		
		printf("Case #%d: %d.000000\n", test, res);
	}
	return 0;
}

