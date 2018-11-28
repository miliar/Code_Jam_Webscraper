#include <cstdio>
#include <algorithm>

using namespace std;

int c, n, t[1001];
int gcd, y;

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int i, j, k, tmp, a, b, r;
	scanf("%d", &c);
	for (i = 1; i <= c; i++) {
		scanf("%d", &n);
		for (j = 1; j <= n; j++)
			scanf("%d", &t[j]);
		sort(t + 1, t + n + 1);
		gcd = t[2] - t[1];
		for (j = 2; j < n; j++) {
			a = gcd;
			b = t[j + 1] - t[j];
			if (a < b) { tmp = a; a = b; b = tmp; }
			while (b) {
				r = a % b;
				a = b;
				b = r;
			}
			gcd = a;
		}
		y = gcd - t[1] % gcd;
		if (y == gcd) y = 0;
		printf("Case #%d: %d\n", i, y);
	}
	return 0;
}