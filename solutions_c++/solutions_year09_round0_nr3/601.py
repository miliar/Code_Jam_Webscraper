#include <stdio.h>
#include <string.h>

char codejam[20] = {"welcome to code jam"};
char sent[1000];

int f[600][20];

int tc, res;

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d\n", &tc);
	for (int t = 0; t < tc; t ++) {
		gets(sent);
		memset(f, 0, sizeof(f));
		res = 0;
		int len = strlen(sent);
		for (int i = 0; i < len; i ++)
			if (sent[i] == 'w') f[i][1] = 1;
		for (int i = 0; i < len; i ++) {
			for (int j = 2; j < 20; j ++)
				if (sent[i] == codejam[j - 1]) {
					for (int k = 0; k < i; k ++) {
						f[i][j] += f[k][j - 1];
					}
					f[i][j] %= 10000;
				}
		}
		for (int i = 0; i < len; i ++) {
			res += f[i][19];
			res %= 10000;
		}
		printf("Case #%d: %d%d%d%d\n", t + 1, (res % 10000) / 1000, (res % 1000) / 100, (res % 100) / 10, res % 10);
	}
	return 0;
}
