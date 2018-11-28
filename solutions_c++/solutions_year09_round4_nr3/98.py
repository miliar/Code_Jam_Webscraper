#include <cstdio>
#include <cstring>

const int MAXN = 105;
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

bool E[MAXN][MAXN];
int a[MAXN][MAXN];

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int N, K;
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < K; j++)
                scanf("%d", &a[i][j]);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                E[i][j] = true;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                for (int k = 0; k < K; k++)
                    if (a[i][k] >= a[j][k])
                        E[i][j] = false;
/*for (int i = 0; i < N; i++)
{
    for (int j = 0; j < N; j++)
        printf("%d ", E[i][j]);
    putchar('\n');
}*/
        int pre[MAXN], next[MAXN];
        printf("Case #%d: %d\n", cas, pathCover(N, E, pre, next));
    }
    return 0;
}
