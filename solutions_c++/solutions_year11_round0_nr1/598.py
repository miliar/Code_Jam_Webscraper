#include <stdio.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int n;
		int lo=1;
		int lb=1;
		int to=0;
		int tb=0;
		scanf("%d ",&n);
// 		printf("%d\n",n);
		for (int i=0; i<n; ++i) {
			char c;
			int k;
			scanf("%c %d ", &c, &k);
// 			printf("%c %d\n",c,k);
			if (c=='O') {
				to = MAX(tb, to + ABS(lo - k)) + 1;
				lo = k;
			} else {
				tb = MAX(to, tb + ABS(lb - k)) + 1;
				lb = k;
			}
// 			printf("> o %d/%d | b %d/%d\n", to, lo, tb, lb);
		}
		int x = to > tb ? to : tb;
		printf("Case #%d: %d\n",c,x);
	}
	return 0;
}
