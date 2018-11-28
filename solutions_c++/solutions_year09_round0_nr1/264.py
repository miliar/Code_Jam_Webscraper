#include <stdio.h>
#include <string.h>

char dict[5005][20];
char pattern[1000];
int mark[20][26];

int main() {

	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);

	int l, d, n;
	scanf("%d%d%d", &l, &d, &n);

	for (int i = 0; i < d; i ++) scanf("%s", dict[i]);
	for (int i = 0; i < n; i ++) {
		scanf("%s", pattern);
		int p = 0, len = strlen(pattern), cnt = 0;
		memset(mark, 0, sizeof(mark));
		while (p < len) {
			if (pattern[p] == '(') {
				p ++;
				while (pattern[p] != ')') mark[cnt][pattern[p++] - 'a'] = 1;
				p ++;
			} else {
				mark[cnt][pattern[p++] - 'a'] = 1;
			}
			cnt ++;
		}

		int ans = 0;
		for (int j = 0; j < d; j ++) {
			int flag = 1;
			for (int k = 0; k < l; k ++) {
				if (!mark[k][dict[j][k] - 'a']) {
					flag = 0;
					break;
				}
			}
			ans += flag;
		}

		printf("Case #%d: %d\n", i + 1, ans);
	}

	return 0;
}