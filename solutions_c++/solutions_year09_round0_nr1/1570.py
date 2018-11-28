#include <stdio.h>
#include <string.h>

char s[5000][20], t[5000];
int mark[20][256];
int l, d, n;
int ans;

int main()
{
	int i, j, k;
	scanf("%d%d%d", &l, &d, &n);
	for (i = 0; i < d; i++)
		scanf("%s", s[i]);
	for (i = 0; i < n; i++) {
		scanf("%s", t);
		k = 0;
		memset(mark, 0, sizeof(mark));
		for (j = 0; j < l; j++) {
			if (t[k] == '(') {
				k++;
				while (t[k] != ')') {
					mark[j][t[k]] = 1;
					k++;
				}
			}
			else mark[j][t[k]] = 1;
			k++;
		}
		ans = 0;
		for (j = 0; j < d; j++) {
			for (k = 0; k < l; k++)
				if (!mark[k][s[j][k]]) break;
			if (k == l) ans++;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}
