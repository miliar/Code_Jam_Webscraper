#include <cstdio>

int main(void) {
	int T, n, k;
	scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", C, ((k+1)%(1<<n) ? "OFF" : "ON"));
	}

	return 0;
}
