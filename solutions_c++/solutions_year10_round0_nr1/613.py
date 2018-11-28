// snapper.cpp --  Sat May 08 2010
#include <stdio.h>
int main(void) {
	int t;
	scanf(" %d", &t);
	for(int c = 1; c <= t; ++c) {
		unsigned n, k;
		scanf(" %u %u", &n, &k);
		// Below I use Dr. Evil's magic formula for printf!
		printf("Case #%d: O%s\n", c, (k+1)%(1u << n) == 0 ? "N" : "FF");
	}
	return 0;
}
