#include <cstdio>

int main(int argc, char **argv) {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int N, K;
		scanf("%d%d", &N, &K);
		N = 1 << N;
		if ((K%N) == (N-1)) {
			printf("Case #%d: ON\n", i);
		} else {
			printf("Case #%d: OFF\n", i);
		}
	}
}
