#include<stdio.h>

int nCase, N;

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		int sum = 0, mn = 1000000000, xo = 0, a;
		for(scanf("%d", &N); N > 0; --N) {
			scanf("%d", &a);
			sum += a;
			xo ^= a;
			if(a < mn) mn = a;
		}
		if(xo != 0) printf("Case #%d: NO\n", cs);
		else printf("Case #%d: %d\n", cs, sum-mn);
	}
}

