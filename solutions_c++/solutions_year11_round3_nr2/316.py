#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int n,l,C;
		long long t;
		scanf("%d%lld%d%d",&l,&t,&n,&C);
		long long a[C];
		for (int i=0;i<C;i++)
			scanf("%lld",&a[i]);
		long long d[n];
		for (int i=0;i<n;i++)
			d[i]=a[i%C]*2;
		long long x = 0;
		int i;
		for (i=0;i<n;i++) {
			if (d[i] > t) {
				x += t;
				d[i] -= t;
				break;
			}
			t -= d[i];
			x += d[i];
		}
		if (i<n) {
			sort(&d[i],&d[n]);
			for (;i<n;i++) {
				if (i>=n-l)
					x += d[i]/2;
				else
					x += d[i];
			}
		}

		printf("Case #%d: %lld\n",c,x);
	}
	return 0;
}
