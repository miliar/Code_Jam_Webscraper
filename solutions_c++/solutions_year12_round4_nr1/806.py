#include <stdio.h>
#include <string.h>

int cs, ct;
int d[10010], l[10010];
int longest[10010];
int n;

int main()
{
	int i, j, k;
	scanf("%d", &cs);
	for (ct = 1; ct <= cs; ct++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &d[n]);
		memset(longest, -1, sizeof(longest));
		longest[0] = d[0];
		for (i = 0; i < n; i++)
		if (longest[i] >= 0) {
			for (j = i + 1; j <= n; j++)
			if (d[i] + longest[i] >= d[j]) {
				k = (l[j] < d[j] - d[i]) ? l[j] : (d[j] - d[i]);
				if (k > longest[j]) longest[j] = k;
			}
			else break;
		}
		if (longest[n] >= 0) printf("Case #%d: YES\n", ct);
		else printf("Case #%d: NO\n", ct);
	}
	return 0;
}
