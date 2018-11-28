#include <stdio.h>
#include <string.h>

int acceptc[15][26];
char words[5000][20];
char pattern[1000];
int l, d, n, res;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i ++) {
		scanf("%s", words[i]);
	}
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < 15; j ++)
			for (int k = 0; k < 26; k ++)
				acceptc[j][k] = 0;
		scanf("%s", pattern);
		int tmp = 0, pos = 0;
		int	len = strlen(pattern);
		while (tmp != len) {
			if (pattern[tmp] == '(') {
				while (pattern[++tmp] != ')') {
					int index = pattern[tmp] - 'a';
					acceptc[pos][index] = 1;
				}
				pos ++;
				tmp ++;
			} else {
				int index = pattern[tmp] - 'a';
				acceptc[pos][index] = 1;
				pos ++;
				tmp ++;
			}
		}
		res = 0;
		for (int j = 0; j < d; j ++) {
			bool flag = 0;
			for (int k = 0; k < l; k ++) {
				int index = words[j][k] - 'a';
				if (acceptc[k][index] == 0) {
					flag = 1;
					break;
				}
			}
			if (!flag) res ++;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
