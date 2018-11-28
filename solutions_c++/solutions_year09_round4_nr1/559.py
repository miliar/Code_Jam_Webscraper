#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int n, minrow[50];

int main()
{
	int cas, cases, i, j;
	char buf[100];
	scanf("%d", &cases);
	for (cas = 1; cas <= cases; cas++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", buf);
			for (j = n - 1; j >= 0; j--) {
				if (buf[j] != '0') break;
			}
			if (j < 0) j = 0;
			minrow[i] = j;
		}
		int c = 0;
		for (i = 0; i < n; i++) {
			for (j = i; j < n; j++) {
				if (minrow[j] <= i) break;
			}
			while (j > i) {
				c++;
				int k = minrow[j];
				minrow[j] = minrow[j - 1];
				minrow[j - 1] = k;
				j--;
			}
		}
		printf("Case #%d: %d\n", cas, c);
	}
	return 0;
}
