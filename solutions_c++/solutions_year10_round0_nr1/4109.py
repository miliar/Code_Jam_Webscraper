#include <stdio.h>

int main (void) {

	unsigned int N, K, T;
	unsigned int n;
	
	
	scanf("%d", &T);
	
	for ( int i=0;i<T;i++) {
		scanf("%d %d", &N, &K);
		n = 1<<N;
		K = K%n;
//		printf("N=%d K=%d n=%d \n", N, K, n);
		if (n == K+1)
			printf("Case #%d: ON\n", i+1);
		else
			printf("Case #%d: OFF\n", i+1);
	}
	
	return 0;
}
