#include <cstdio>

int main() {
	int T, N, K, n;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d%d", &N, &K);
		n = 1 << N;
		printf("Case #%d: %s\n", i+1, (K+1)%n ? "OFF" : "ON");
	}
	return 0;
}
