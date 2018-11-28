#include <stdio.h>

int main()
{
	int T;
	scanf(" %d", &T);
	for (int _ = 1; _ <= T; _++) {
		int N, K;
		scanf(" %d %d", &N, &K);
		printf("Case #%d: %s\n", _, (++K % (1UL << N)) == 0 ? "ON" : "OFF");
	}
}
