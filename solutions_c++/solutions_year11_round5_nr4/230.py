#include <stdio.h>
#include <math.h>

int cs, ct;
int n, m, qs;
int a[100], p[100];
long long num, sq;

int main()
{
	int i, j, k;
	char s[100];
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%s", s);
		qs = 0;
		for (i = 0; s[i]; i++) {
			if (s[i] == '1') a[i] = 1;
			if (s[i] == '0') a[i] = 0;
			if (s[i] == '?') p[qs++] = i;
		}
		n = i;
		m = 1 << qs;
		for (i = 0; i < m; i++) {
			k = i;
			for (j = 0; j < qs; j++) {
				a[p[j]] = k & 1;
				k >>= 1;
			}
			num = 0;
			for (j = 0; j < n; j++)
				num = num * 2 + a[j];
			sq = sqrt(num);
			if (sq * sq == num || (sq + 1) * (sq + 1) == num || (sq - 1) * (sq - 1) == num) break;
		}

		printf("Case #%d: ", cs);
		for (i = 0; i < n; i++)
			printf("%d", a[i]);
		printf("\n");
	}	
	return 0;
}
