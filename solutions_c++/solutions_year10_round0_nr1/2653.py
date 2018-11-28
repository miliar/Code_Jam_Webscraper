#include <stdio.h>

int T; // test cases
int N; // Snapper devices
int K; // times I have snapped my fingers

int main() {
	int powerOf2;

	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d %d", &N, &K);

		powerOf2 = 1;
		for (int j = 1; j <= N; j++) {
			powerOf2 *= 2;
		}

		printf("Case #%d: ", i);
		if ((K % powerOf2) == (powerOf2 - 1)) {
			printf("ON");
		}
		else {
			printf("OFF");
		}
		printf("\n");
	}
	return 0;
}

// I'm on 2136 place
