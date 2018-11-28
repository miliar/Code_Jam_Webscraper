#include <stdio.h>
#include <string.h>

int T, r, k, n;
int g[1000];
long long tot, ans;

long long a[1000];
int b[1000];

int main()
{
	int cs, i, x;
	scanf("%d", &T);
	for (cs = 1; cs <= T; cs++) {
		scanf("%d%d%d", &r, &k, &n);
		tot = 0;
		for (i = 0; i < n; i++) {
			scanf("%d", &g[i]);
			tot += g[i];
		}
		if (k >= tot) {
			ans = tot * r;
			printf("Case #%d: %lld\n", cs, ans);
			continue;
		}

		for (i = 0; i < n; i++) {
			tot = 0;
			for (x = i; ; x = (x + 1) % n) {
				if (tot + g[x] > k) break;
				tot += g[x];
			}
			a[i] = tot;
			b[i] = x;
		}

		ans = 0;
		x = 0;
		for (i = 0; i < r; i++) {
			ans += a[x];
			x = b[x];
		}
		printf("Case #%d: %lld\n", cs, ans);

	}	
	return 0;
}
