#include <stdio.h>

int T, n;
long long a[1000];

long long gcd(long long x, long long y) {
	long long r;
	while (x) { 
		r = y % x; 
		y = x; 
		x = r; 
	}
	return y; 
}

int main()
{
	int cs, i;
	long long j, g;
	scanf("%d", &T);
	for (cs = 1; cs <= T; cs++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%lld", &a[i]);
		}

		g = 0;
		for(i = 0; i < n; i++) {
			j = a[i] - a[(i + 1) % n];
			if (j < 0) j = -j;
			if (g == 0) g = j;
			else g = gcd(g, j);
		}

		printf("Case #%d: %lld\n", cs, (-a[0] % g + g) % g);
	}	
	return 0;
}
