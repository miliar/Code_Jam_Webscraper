#include <cstdio>
#include <algorithm>
#define MAXINT 1000005
#define MAX 1005

using namespace std;

int main() {
	int t, z, s, xs, n, m, k, c[MAX], i;

	scanf("%d", &t);
	for (z=1; z<=t; z++) {
		scanf("%d", &n);
		s = xs = 0;
		m = MAXINT;
		for (i=1; i<=n; i++) {
			scanf("%d", &c[i]);
			xs ^= c[i];
			s += c[i];
			m = min(m, c[i]);
		}

		if (xs) printf("Case #%d: NO\n", z);
		else printf("Case #%d: %d\n", z, s - m);

	}
	return 0;
}

