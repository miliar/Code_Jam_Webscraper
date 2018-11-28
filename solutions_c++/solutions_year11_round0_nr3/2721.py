#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N;
		int C[1000];
		int min = 10000000;
		int current = 0;
		int sum = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &C[i]);
			current ^= C[i];
			if (C[i] < min) {
				min = C[i];
			}
			sum += C[i];
		}

		printf("Case #%d: ", t);
		if (current != 0) {
			printf("NO");
		} else {
			printf("%d", sum - min);
		}
		printf("\n");
	}

	return 0;
}
