#include <stdio.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int n,k,x=0;
		scanf("%d ",&n);
		for (int i=1; i<=n; ++i) {
			scanf("%d",&k);
			if (k!=i)
				x++;
		}
		printf("Case #%d: %lf\n",c,(double)x);
	}
	return 0;
}
