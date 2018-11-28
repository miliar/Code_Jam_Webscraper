#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define FOR(i, L, R) for (int i = (L); i <= (R); ++i)
#define ROF(i, R, L) for (int i = (R); i >= (L); --i)

using namespace std;

const int INF = ~0U >> 3;

int T, P;
int M[4007], w[4007];
int f[4007][50];

int main()
{
	scanf("%d", &T);
	FOR(testCase, 1, T) {
		scanf("%d", &P);
		int n = 1 << P;
		FOR(i, n, n * 2 - 1) {
			scanf("%d", M + i);
			M[i] = P - M[i];
		}
		ROF(l, P - 1, 0)
			FOR(i, 1 << l, (1 << l + 1) - 1) scanf("%d", w + i);
		ROF(i, 2 * n - 1, 1)
			FOR(j, 0, P) {
				if (i >= n) {
					if (j >= M[i]) f[i][j] = 0;
					else f[i][j] = INF;
				} else {
					f[i][j] = min(f[i * 2][j] + f[i * 2 + 1][j], INF);
					if (j < P)
						f[i][j] = min(f[i][j], f[i * 2][j + 1] + f[i * 2 + 1][j + 1] + w[i]);
				}
			}
		printf("Case #%d: %d\n", testCase, f[1][0]);
	}
//	system("pause");
}
