#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 5000;

int nl, nd, nt;

char word[maxn + 5][20];

int main() {
	char pattern[410];
	char split[20][30];
	int len[20];

	while (scanf("%d %d %d", &nl, &nd, &nt) != EOF) {
		for (int i = 0; i < nd; i++) {
			scanf(" %s", word[i]);
		}

		for (int t = 1; t <= nt; t++) {
			scanf(" %s", pattern);

			int i = 0, j = 0, k = 0;
			while (k < nl) {
				if (pattern[i] == '(') {
					j = i + 1;
					while (pattern[j] != ')') j++;
					memcpy(split[k], &pattern[i + 1], j - i - 1);
					len[k] = j - i - 1;
					sort(split[k], split[k] + len[k]);
					i = j + 1;
				}
				else {
					split[k][0] = pattern[i];
					len[k] = 1;
					i++;
				}
				k++;
			}

			/*for (k = 0; k < nl; k++) {
				for (i = 0; i < len[k]; i++) {
					printf("%c", split[k][i]);
				}
				printf("\n");
			}*/

			int res = 0, lo, hi, mid;
			for (i = 0; i < nd; i++) {
				for (j = 0; j < nl; j++) {
					lo = 0, hi = len[j] - 1;

					while (lo <= hi) {
						mid = (lo + hi) >> 1;

						if (split[j][mid] == word[i][j]) break;
						else if (split[j][mid] < word[i][j]) {
							lo = mid + 1;
						}
						else hi = mid - 1;
					}
					if (lo > hi) break;
				}

				if (j >= nl) res++;
			}

			printf("Case #%d: %d\n", t, res);
		}
	}

	return 0;
}
