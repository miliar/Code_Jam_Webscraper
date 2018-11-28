#include <stdio.h>

bool solve(const int N, int K) {
	int states = 1 << N;
	K %= states;
	for (int i = 0; i < N; ++i) {
		if (!(K & 1)) {
			return false;
		}	
		K >>= 1;
	}
	return true;
}

void print(int i, bool res) {
	printf("Case #%d: %s\n", i, (res ? "ON" : "OFF"));
}

int main(void) {
	int T = 0;
	
	freopen("a-small.in",  "rt", stdin);
	freopen("a-small.out", "wt", stdout);

	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		int N = 0;
		int K = 0;
		scanf("%d%d", &N, &K);
		print(i + 1, solve(N, K));
	}

	return 0;
}
