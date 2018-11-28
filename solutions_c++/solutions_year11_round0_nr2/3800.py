#include <cstdio>

using namespace std;

#define CMAX	36
#define DMAX	28
#define NMAX	100

int T, t;
int C, D, N;

char c[CMAX][3], d[DMAX][2], e[NMAX];
int i, j, ei, en;

int find(char c) {
	int k;

	for (k = 0; k < en; k++) {
		if (e[k] == c) {
			en = -1;
			return 1;
		}
	}

	return 0;
}

int main() {
	scanf("%d", &T);
	for (t = 0; t < T; t++) {
		scanf("%d ", &C);
		for (i = 0; i < C; i++) {
			scanf("%c%c%c ", &c[i][0], &c[i][1], &c[i][2]);
		}

		scanf("%d ", &D);
		for (i = 0; i < D; i++) {
			scanf("%c%c ", &d[i][0], &d[i][1]);
		}

		scanf("%d ", &N);
		en = 0;
		for (i = 0; i < N; i++, en++) {
			scanf("%c", &e[en]);
			for (j = 0; j < C; j++) {
				if (en > 0 &&
					((e[en - 1] == c[j][0] && e[en] == c[j][1]) ||
					(e[en - 1] == c[j][1] && e[en] == c[j][0]))) {

					e[en - 1] = c[j][2];
					en--;
					break;
				}
			}

			for (j = 0; j < D; j++) {
				if (e[en] == d[j][0]) {
					if (find(d[j][1]))
						break;
				}
				
				if (e[en] == d[j][1]) {
					if (find(d[j][0]))
						break;
				}
			}
		}

		printf("Case #%d: [", t + 1);
		en--;
		for (i = 0; i < en; i++) {
			printf("%c, ", e[i]);
		}
		if (en >= 0)
			printf("%c]\n", e[en]);
		else
			printf("]\n");
	}

	return 0;
}

