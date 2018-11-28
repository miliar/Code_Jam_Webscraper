#include <stdio.h>
#include <string.h>

int n;
char s[502], w[21] = " welcome to code jam";
int d[502][20];

int main() {
	int i, j, k;
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d\n", &n);
	for (i = 1; i <= n; i++) {
		gets(s + 1);
		memset(d, 0, sizeof(d));
		d[0][0] = 1;
		for (j = 1; s[j] != (char) NULL; j++) {
			d[j][0] = 1;
			for (k = 1; k <= 19; k++) {
				d[j][k] = d[j - 1][k];
				if (s[j] == w[k])
					d[j][k] += d[j - 1][k - 1];
				if (d[j][k] >= 10000)
					d[j][k] -= 10000;
			}
		}
		printf("Case #%d: %04d\n", i, d[j - 1][19]);
	}
	return 0;
}