#include <stdio.h>

int t, T, C, D, N, i, n, j, k;
char c[36][4], d[28][3], s[101];
char res[101];

int main() {
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		n = 0;
		scanf("%d", &C);
		for (i = 0; i < C; i++) scanf("%s", c[i]);
		scanf("%d", &D);
		for (i = 0; i < D; i++) scanf("%s", d[i]);
		scanf("%d", &N);
		scanf("%s", s);
		for (i = 0; i < N; i++) {
			res[n++] = s[i];
			if (n <= 1) continue;

			for (j = 0; j < C; j++) {
				if ((res[n-1] == c[j][0] && res[n-2] == c[j][1]) || (res[n-1] == c[j][1] && res[n-2] == c[j][0])) {
					res[--n - 1] = c[j][2];
					break;
				}
			}
			if (j == C) {
				for (j = 0; j < D; j++) {
					if (res[n-1] == d[j][0]) {
						for (k = 0; k < n; k++) if (res[k] == d[j][1]) {n = 0; break;}
						if (k < n) break; 
					}
					if (res[n-1] == d[j][1]) {
						for (k = 0; k < n; k++) if (res[k] == d[j][0]) {n = 0; break;}
						if (k < n) break; 
					}
				}
			}
		}
		printf("Case #%d: [", t);
		if (n > 0) printf("%c", res[0]);
		for (i = 1; i < n; i++) printf(", %c", res[i]);
		printf("]\n");
	}
	return 0;
}
