#include <stdio.h>

int main () {
	int t;
	scanf("%d", &t);
	
	for (int c = 1; c <= t; c++) {
		int n, k;
		scanf("%d %d", &n, &k);
		
		int divby = 1 << n;
		if (k % divby == divby - 1)
			printf("Case #%d: ON\n", c);
		else
			printf("Case #%d: OFF\n", c);
	}
}
