#include <stdio.h>
#include <math.h>

bool solve(int t, int n, long int k);

int main() {
	int t, n;
	long int k;

	scanf("%d", &t);
	for(int i=1; i<=t; ++i) {
		scanf("%d %ld", &n, &k);
		printf("Case #%d: ", i);
		if ( solve(t, n, k) == true ) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}
	}
	return 0;
}

bool solve(int t, int n, long int k) {
	if ( n == 1 && k == 0 ) {
		return false;
	} else if ( n == 1 && k == 1 ) {
		return true;
	}
	long int number, plugin;

	number = (long int)pow(2.0, n);
	plugin = k % number;

	if ( plugin & (number-1L) == plugin ) {
		return true;
	}
	
	return false;
}
