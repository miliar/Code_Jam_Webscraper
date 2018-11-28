#include <stdio.h>

int bit[32];
int i, j, T, N, K;

int main()
{
	for (i = 0; i < 32; i++) {
		bit[i] = 1<<i;
	}

	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d %d", &N, &K);
		for (j = 0; j < N; j++) {
			if (!(bit[j] & K)) {
				break;
			}
		}
		if (j < N) {
			printf("Case #%d: OFF\n", i+1);
		} else {
			printf("Case #%d: ON\n", i+1);
		}
	}
}
