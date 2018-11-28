#include <stdio.h>
#include <string.h>
long long g[1100], d[1100], t[1100];
int main() {
	int ca, cases = 0;
	int i, j;
	long long tot, count, r, k, n;
	scanf("%d",&ca);
	while (ca--) {
		printf("Case #%d: ",++cases);
		scanf("%I64d%I64d%I64d", &r, &k, &n);
		tot = 0;
		for (i=0;i<n;++i) {
			scanf("%I64d", &g[i]);
			tot += g[i];
		}
		if ( tot <= k) {
			printf("%I64d\n", r * tot);
			continue;
		}
		
		memset(d, 0, sizeof(d));
		memset(t, 0, sizeof(t));
		count = j = 0;
		while (!t[j]) {
			tot = 0;
			t[j] = ++count;
			for (i = j; g[i] + tot <= k;i = (i+1)%n) {
				tot += g[i];
			}
			d[count] = d[count-1] + tot;
			j = i;
		}
		
		if (r <= count) {
			printf("%I64d\n", d[r]);
		} else {
			printf("%I64d\n", d[count] + ((r-count) / (count - t[j] + 1)) * (d[count] - d[t[j]-1]) 
				+  d[t[j] - 1 + ((r-count) % (count - t[j] + 1))] - d[t[j]-1] );
		}
	}
	return 0;
}