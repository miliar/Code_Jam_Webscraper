#include <stdio.h>
#include <string.h>

const char *w = "welcome to code jam";
const int l = strlen(w);
int cs, ct, tot;
char s[600];
int ans[2][600];

int main()
{
//	freopen("c.in", "r", stdin);
	int i, j, k, u;
	scanf("%d\n", &cs);
	for (ct = 1; ct <= cs; ct++) {
		gets(s);
		u = 0;
		memset(ans, 0, sizeof(ans));
		for (j = 0; s[j]; j++)
			if (s[j] == w[0]) ans[u][j] = 1;

		for (i = 1; i < l; i++) {
			memset(ans[!u], 0, sizeof(ans[!u]));
			for (j = 0; s[j]; j++)
			if (s[j] == w[i]) {
				for (k = 0; k < j; k++)
					ans[!u][j] += ans[u][k] % 10000;
			}
			u = !u;
		}

		tot = 0;
		for (j = 0; s[j]; j++)
			tot += ans[u][j] % 10000;
		printf("Case #%d: %04d\n", ct, tot);

	}
	
	return 0;
}

