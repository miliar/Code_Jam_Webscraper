#include <stdio.h>
#include <string.h>

int l, d, n;
char t[5000][16], s[30000000];
bool S[15][26], chk;
int cnt;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, k;
	scanf("%d%d%d", &l, &d, &n);
	for (i = 0; i < d; i++)
		scanf("%s", t[i]);
	for (i = 1; i <= n; i++) {
		scanf("%s", s);
		memset(S, 0, sizeof(S));
		chk = false;
		for (j = k = 0; s[j] != (char) NULL; j++) {
			if (s[j] == '(')
				chk = true;
			else if (s[j] == ')') {
				chk = false;
				k++;
			} else {
				S[k][s[j] - 'a'] = true;
				if (!chk) k++;
			}
		}
		cnt = 0;
		for (j = 0; j < d; j++) {
			for (k = 0; k < l; k++)
				if (!S[k][t[j][k] - 'a']) break;
			if (k == l) cnt++;
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}