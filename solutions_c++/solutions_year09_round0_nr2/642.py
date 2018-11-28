#include <cstdio>
#include <cstring>
#define maxn 110

using namespace std;

const int dl[4] = {-1, 0, 0, 1};
const int dc[4] = {0, -1, 1, 0};

int n, m, i, j, tt, q;
int v[maxn][maxn], antx[maxn][maxn], anty[maxn][maxn];
char ch, rez[maxn][maxn], pun;

void init() {
	memset(v, 0, sizeof(v));
	memset(rez, 0, sizeof(rez));
}

void read() {
	scanf("%d%d", &n, &m);
	for (i = 1; i <= n; i++) 
		for (j = 1; j <= m; j++)
			scanf("%d", &v[i][j]);
}

void solve() {
	int lnou, cnou, l, c, d, min, mind;
	bool ok;

	ch = 'a' - 1;

	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++) if (rez[i][j] == 0) {
			min = 2000000000;
			l = i; c = j; ok = 1;
			while (ok) {
//				rez[l][c] = ch;
				for (d = 0; d < 4; d++) {
					lnou = l + dl[d];
					cnou = c + dc[d];
					if (lnou > 0 && lnou <= n && cnou > 0 && cnou <= m) 
						if (v[lnou][cnou] < min) {
							min = v[lnou][cnou];
							mind = d;
						}
				}

	//			fprintf(stderr, "%d %d  %d %d  %d %d\n", i, j, l, c, v[l][c], min);

				if (min < v[l][c]) {
					ok = 1;
					antx[l + dl[mind]][c + dc[mind]] = l;
					anty[l + dl[mind]][c + dc[mind]] = c;
					l = l + dl[mind]; c = c + dc[mind];
					if (rez[l][c] != 0) {
						pun = rez[l][c];
						ok = 0;
					}
				}
				else {
					ok = 0;
					ch++;
					pun = ch;
				}
			}

			while (l != i || c != j) {
				rez[l][c] = pun;
				lnou = antx[l][c]; cnou = anty[l][c];
				l = lnou; c = cnou;
			}
			rez[i][j] = pun;
		}

}

inline void afis() {
	int i, j;
	printf("Case #%d:\n", q);

	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++)
			printf("%c ", rez[i][j]);
		printf("\n");
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d", &tt);
	for (q = 1; q <= tt; q++) {
		init();
		read();
		solve();
		afis();
	}

	return 0;
}
