#include <cstdio>
#include <cstdlib>

int main() {
	int TESTS;
	scanf("%d", &TESTS);
	for(int test = 1; test<=TESTS; test++) {
		int N;
		scanf("%d", &N);
		int xorr = 0;
		int min = 1000000000;
		int sum = 0;
		for(int i = 0; i<N; i++) {
			int num;
			scanf("%d", &num);
			xorr ^= num;
			sum+=num;
			if(num < min) {
				min = num;
			}
		}
		if(xorr == 0) {
			printf("Case #%d: %d\n", test, sum-min);
		} else {
			printf("Case #%d: NO\n", test);
		}
	}
	return 0;
}
