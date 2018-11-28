#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int t, n;
int main() {

	scanf("%d\n", &t);
	int test = 0;
	while(test++<t) {
		scanf("%d\n", &n);
		int alcen = 0, r = 0, e, min = INT_MAX, total = 0;
		while(alcen++<n) {
			scanf("%d\n", &e);
			r ^= e;
			if(e < min)
				min = e;
			total += e;
		}
		if(r)
			printf("Case #%d: NO\n", test);
		else
			printf("Case #%d: %d\n", test, total-min);
	}
}
