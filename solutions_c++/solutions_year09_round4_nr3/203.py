#include <cstdio>
#include <cstring>

// from code library
const int MAXN = 110;
#define _clr(x) memset(x, 0xff, sizeof(int) * n)

int hungary(int n, const bool mat[][MAXN], int * match1, int * match2) {
	int s[MAXN], t[MAXN], p, q, ret = 0, i, j, k;
	_clr(match1);
	_clr(match2);
	for (i = 0; i < n; ret += (match1[i++] >= 0)) {
		_clr(t);
		for (s[p = q = 0] = i; p <= q && match1[i] < 0; p++) {
			for (k = s[p], j = 0; j < n && match1[i] < 0; j++) {
				if (mat[k][j] && t[j] < 0) {
					s[++q] = match2[j];
					t[j] = k;
					if (s[q] < 0) {
						for (p = j; p >= 0; j = p) {
							match2[j] = k = t[j];
							p = match1[k];
							match1[k] = j;
						}
					}
				}
			}
		}
	}
	return ret;
}

inline int pathCover(int n, const bool mat[][MAXN], int * pre, int * next) {
	return n - hungary(n, mat, next, pre);
}

bool g[110][110];
int pre[110];
int next[110];

int main() {
    int t, T, i, j, p;
    int n, k;
    int price[110][30];

    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d%d", &n, &k);
        for (i = 0; i < n; i++)
            for (j = 0; j < k; j++)
                scanf("%d", &price[i][j]);
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                g[i][j] = true;
                for (p = 1; p < k; p++) {
                    if ((price[i][p - 1] < price[j][p - 1]) && (price[i][p] < price[j][p]))
                        continue;
                    g[i][j] = false;
                    break;
                }
            }
        }
        /*
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++)
                printf("%d ", g[i][j]);
            printf("\n");
        }
        */
        int ret = pathCover(n, g, pre, next);
        printf("%d\n", ret);
    }
}
