#include <cstdio>
using namespace std;


int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t, T, i, j, n, m;
	char s[200][200];
	for (t = 1, scanf("%d", &T); t <= T; t++) {
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				if (s[i][j] == '#') {
					if (i > 0 && (s[i-1][j] == '1' || s[i-1][j] == '2')) {
						s[i][j] = s[i-1][j] + 2;
					} else if (j > 0 && (s[i][j-1] == '1' || s[i][j-1] == '3')) {
						s[i][j] = s[i][j-1] + 1;
					} else s[i][j] = '1';
				}
			}
		}
		int c[5];
		c[0] = c[1] = c[2] = c[3] = c[4] = 0;
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				if (s[i][j] == '#') c[0]++;
				else if (s[i][j] != '.') c[s[i][j] - '0']++;
			}
		}
		printf("Case #%d:\n", t);
		if (c[0] == 0 && (c[1] == c[2] && c[1] == c[3] && c[1] == c[4])) {
			for (i = 0; i < n; i++) {
				for (j = 0; j < m; j++) {
					if (s[i][j] == '1' || s[i][j] == '4') s[i][j] = '/';
					if (s[i][j] == '2' || s[i][j] == '3') s[i][j] = '\\';
				}
			}
			for (i = 0; i < n; i++) {
				printf("%s\n", s[i]);
			}
		} else {
			printf("Impossible\n");
		}
	}
	fclose(stdout);
	return 0;
}
