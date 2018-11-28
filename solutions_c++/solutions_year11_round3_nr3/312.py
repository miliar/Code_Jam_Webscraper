#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <limits.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

long long gcd(long long a, long long b) {
	// a <= b
	if (!a)
		return b;
	return gcd(b%a, a);
}

long long ggcd(long long a, long long b) {
	long long aa=MIN(a,b);
	long long bb=MAX(a,b);
	return gcd(aa,bb);
}

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int n;
		long long l,h;
		scanf("%d%lld%lld",&n,&l,&h);
		long long f[n];
		for (int i=0;i<n;++i)
			scanf("%lld", &f[i]);

		long long x=-1;
		if (1 >= l && 1 <= h)
			x=1;
		else {
			for (x=l; x<=h; x++) {
				int i;
				for (i=0;i<n;++i)
					if (x%f[i] && f[i]%x)
						break;
				if (i==n)
					break;
			}
			if (x>h)
				x=-1;
		}

		if (x>=0)
			printf("Case #%d: %lld\n",c,x);
		else
			printf("Case #%d: NO\n",c);
	}
	return 0;
}
