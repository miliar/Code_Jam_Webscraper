#include <cstdio>

int main() {
	int numCases;
	scanf("%d", &numCases);
	for (int i = 0; i < numCases; i++) {
		int a;
		scanf("%d", &a);
		int ans = a;
		for (int j = 1; j <= a; j++) {
			int temp;
			scanf("%d", &temp);
			if (temp == j) {
				ans--;
			}
		}
		printf("Case #%d: %lf\n", i + 1, (double)ans);
	}

	return 0;
}
