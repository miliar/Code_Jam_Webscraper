#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int t, n, a[2000];

int gcd(int a, int b) {
	if (!a) return b;
	return gcd(b % a, a);
}

int main() {
	freopen("b.in", "r", stdin);	
	freopen("b.out", "w", stdout);
	scanf("%d", &t);
	int i, j, k, l, d;
	for (l = 1; l <= t; ++l) {
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		d = a[1] - a[0];
		for (i = 2; i < n; ++i)
			d = gcd(d, a[i] - a[i - 1]);
		j = (d - (a[0] % d)) % d;
		printf("Case #%d: %d\n", l, j);
	}
	return 0;
}
