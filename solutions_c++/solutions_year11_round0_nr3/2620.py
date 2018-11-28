#include <cstdio>

int T, N;

int main() {
	int c, sum, xorsum, min_c;

	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d", &N);
		sum = xorsum = 0;
		min_c = 1234567;
		for(int j = 0; j < N; j++) {
			scanf("%d", &c);
			sum += c;
			xorsum ^= c;
			min_c = c < min_c ? c : min_c;
		}
		if(xorsum) {
			printf("Case #%d: NO\n", i+1);
		} else {
			printf("Case #%d: %d\n", i+1, sum - min_c);
		}
	}
	return 0;
}
