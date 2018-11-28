#include <stdio.h>

int N, K, T;

char *state[] = {"OFF", "ON"};

int main() {
	scanf("%d ", &T);
	for (int t = 1; t <= T; ++ t) {
		scanf("%d %d ", &N, &K);
		int two_nth = 1 << N;
		int s = (int) (K % two_nth == two_nth - 1);
		printf("Case #%d: %s\n", t, state[s]);
	}
	return 0;
}

