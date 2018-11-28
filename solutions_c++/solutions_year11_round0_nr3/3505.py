#include <stdio.h>

int cs, ct, n;
int x, y, min;

int main()
{
	int i, k;
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d", &n);
		min = 0x7fffffff;
		x = y = 0;
		for (i = 0; i < n; i++) {
			scanf("%d", &k);
			x ^= k;
			y += k;
			if (k < min) min = k;
		}
		printf("Case #%d: ", cs);
		if (x == 0) printf("%d\n", y - min);
		else printf("NO\n");
	}
	return 0;
}
