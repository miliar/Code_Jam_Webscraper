#include <stdio.h>

int main(){
	long k, n;
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		scanf("%ld%ld", &n, &k);
		n = (1<<n);
		k %= n;
		//printf("n = %ld | k = %ld", n, k);
		printf("Case #%d: %s\n", i, k == n - 1? "ON": "OFF");
	}
}