#include <cstdio>
using namespace std;


int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t, T, i, j, c, d, n;
	char inv[30][30];
	char opp[30][30];
	char str[200];
	char st[200];
	for (t = 1, scanf("%d", &T); t <= T; t++) {
		for (i = 0; i < 30; i++) {
			for (j = 0; j < 30; j++) {
				inv[i][j] = opp[i][j] = ' ';
			}
		}
		scanf("%d", &c);
		for (i = 0; i < c; i++) {
			scanf("%s", str);
			inv[str[0] - 'A'][str[1] - 'A'] = inv[str[1] - 'A'][str[0] - 'A'] = str[2];
			//printf("invoke : %c %c -> %c\n", str[0], str[1], str[2]);
		}
		scanf("%d", &d);
		for (i = 0; i < d; i++) {
			scanf("%s", str);
			opp[str[0] - 'A'][str[1] - 'A'] = opp[str[1] - 'A'][str[0] - 'A'] = '1';
		}
		scanf("%d", &n);
		scanf("%s", str);
		int top = 0;
		for (i = 0; i < n; i++) {
			/*printf("%dtemp - case %d: [", top, t);
			for (j = 0; j < top; j++) {
				printf("%c, ", st[j]);
			}
			if (top > 0) printf("%c", st[top]);
			printf("]\n");
			*/
			if (top > 0) {
				if (inv[str[i] - 'A'][st[top-1] - 'A'] != ' ') {
					//printf("%c ->", st[top-1]);
					st[top-1] = inv[str[i] - 'A'][st[top-1] - 'A'];
					//printf("%c\n", st[top-1]);
					continue;
				}
				for (j = 0; j < top; j++) {
					if (opp[st[j] - 'A'][str[i] - 'A'] != ' ') {
						//printf("opp %c %c\n", st[j], str[i]);
						top = 0;
						j = n + 1;
					}
				}
				if (j > n) continue;
			}
			st[top++] = str[i];
		}
		printf("Case #%d: [", t);
		for (i = 0; i < top - 1; i++) {
			printf("%c, ", st[i]);
		}
		if (top > 0) printf("%c", st[top-1]);
		printf("]\n");
	}
	fclose(stdout);
	return 0;
}
