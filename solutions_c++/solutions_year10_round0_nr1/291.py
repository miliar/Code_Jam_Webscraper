#include <stdio.h>
#include <stdlib.h>

int main()
{
	int c, t, n, k, i;
	scanf("%d", &t);
	for (c = 1; c <= t; c++) {
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++) {
			if ((k & (1 << i)) == 0) break;
		}
		printf("Case #%d: %s\n", c, i == n ? "ON" : "OFF");
	}
	return 0;
}
