#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char words[6000][50];

int main()
{
	int n, d, l, i, j, k;
	int list[6000], nlist;
	char pattern[1000], *p;
	bool ok[30];
	scanf("%d%d%d", &l, &d, &n);
	for (i = 0; i < d; i++) {
		scanf("%s", words[i]);
	}
	for (i = 0; i < n; i++) {
		scanf("%s", pattern);
		for (j = 0; j < d; j++) {
			list[j] = j;
		}
		nlist = d;
		p = pattern;
		for (j = 0; j < l; j++) {
			memset(ok, 0, sizeof(ok));
			if (*p == '(') {
				p++;
				while (*p != ')') {
					ok[*p - 'a'] = true;
					p++;
				}
				p++;
			} else {
				ok[*p - 'a'] = true;
				p++;
			}
			for (k = nlist - 1; k >= 0; k--) {
				//printf("%s %d %d\n", words[list[k]], j, ok[words[list[k]][j] - 'a']);
				if (!ok[words[list[k]][j] - 'a']) {
					list[k] = list[--nlist];
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, nlist);
	}
	return 0;
}
