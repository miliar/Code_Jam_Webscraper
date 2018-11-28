#include <stdio.h>
#include <string.h>

int T, n;
char m[50][50];
bool chk[50];
int p[50];
int cnt;

int main() {
	int lT, i, j;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (lT = 1; lT <= T; lT++) {
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
			scanf("%s", m[i]);
		memset(chk, 0, sizeof(chk));
		cnt = 0;
		for (i = 1; i <= n; i++) {
			for (j = n; j >= 1; j--)
				if (m[i][j] == '1') break;
			while (chk[j]) j++;
			chk[j] = true;
			p[i] = j;
		}
		for (i = 1; i <= n; i++)
			for (j = i + 1; j <= n; j++)
				if (p[i] > p[j]) cnt++;
		printf("Case #%d: %d\n", lT, cnt);
	}
	return 0;
}