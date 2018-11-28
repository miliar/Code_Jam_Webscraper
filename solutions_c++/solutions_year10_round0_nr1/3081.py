#include <stdio.h>

long long getClaps(int n) {
	long long result = 1;
	
	for (int i = 0; i < n; i++)
		result *= 2;
	
	return result - 1;
}

int main(int argc, char * argv[]) {

	int cases;
	long long n, k;
    long long reqClaps;
	
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		scanf("%lld %lld", &n, &k);
		reqClaps = getClaps(n);
		if ((k % (reqClaps + 1)) == reqClaps) {
			printf("Case #%d: ON\n", i+1);
		}
		else {
			printf("Case #%d: OFF\n", i+1);
		}
	}
	
	return 0;
	
}
