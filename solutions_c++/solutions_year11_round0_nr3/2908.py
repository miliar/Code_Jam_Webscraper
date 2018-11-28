#include <cstdio>

int main() {
	int numCases;
	scanf("%d", &numCases);
	for (int i = 1; i <= numCases; i++) {
		int n;
		scanf("%d", &n);
		int min = 1 << 29;
		int xored = 0;
		int total = 0;
		for (int j = 0; j < n; j++) {
			int temp;
			scanf("%d", &temp);
			xored ^= temp;
			if (min > temp) {
				min = temp;
			}
			total += temp;
		}
		printf("Case #%d: ", i);
		if (xored == 0) {
			printf("%d\n", total - min);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
