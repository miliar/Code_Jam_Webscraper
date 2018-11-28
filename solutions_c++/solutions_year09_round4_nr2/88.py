#include <cstdio>

const int maxn = 60;
const int inf = 0x7fffffff;

char mat[maxn][maxn];
int opt[maxn][maxn][maxn][2]; //row fr to side
int R, C, F;

void Update(int &a, int b) {
	if (a > b) a = b;
}

int Fall(int r, int c, int add) {
	int i;
	for (i = r; i + 1 < R && mat[i + 1][c] == '.'; i++);
	if (i + add > r + F) i = R;
	return i;
}

void Solve() {
	scanf("%d %d %d", &R, &C, &F);
	int i, j, k, l;
	for (i = 0; i < R; i++)
		scanf("%s", mat[i]);
	for (i = 0; i < R; i++)
		for (j = 0; j < C; j++)
			for (k = 0; k < C; k++)
				for (l = 0; l < 2; l++)
					opt[i][j][k][l] = inf;
	opt[0][0][0][0] = 0;
	int fr, to, side, posi, ff, tt;
	for (i = 0; i + 1 < R; i++)
		for (fr = 0; fr < C; fr++)
			for (to = fr; to < C; to++)
				for (side = 0; side < 2; side++)
					if (opt[i][fr][to][side] < inf) {
						int prev = opt[i][fr][to][side];
						posi = side == 0 ? fr : to;
						int ll, rr;
						for (ll = posi; ll >= 0 && mat[i + 1][ll] == '#' && (mat[i][ll] == '.' || fr <= ll); ll--);
						for (rr = posi; rr < C && mat[i + 1][rr] == '#' && (mat[i][rr] == '.' || rr <= to); rr++);
						if (ll >= 0 && (mat[i][ll] == '.' || fr <= ll) && mat[i + 1][ll] == '.') Update(opt[Fall(i, ll, 0)][ll][ll][0], prev);
						if (rr < C && (mat[i][rr] == '.' || rr <= to) && mat[i + 1][rr] == '.') Update(opt[Fall(i, rr, 0)][rr][rr][0], prev);
						ll++;
						rr--;
						//printf("%d %d %d   %d,   ,ll = %d, rr = %d\n", i, fr, to, posi, ll, rr);
						for (ff = ll; ff <= rr; ff++)
							for (tt = ff; tt <= rr; tt++) {
								if (ll < ff)
									if (i + 1 == R - 1 || i + 2 < R && mat[i + 2][ff] == '#')
										Update(opt[i + 1][ff][tt][0], prev + tt - ff + 1);
									else
										Update(opt[Fall(i + 1, ff, 1)][ff][ff][0], prev + tt - ff + 1);
								if (tt < rr)
									if (i + 1 == R - 1 || i + 2 < R && mat[i + 2][tt] == '#')
										Update(opt[i + 1][ff][tt][1], prev + tt - ff + 1);
									else
										Update(opt[Fall(i + 1, tt, 1)][ff][tt][1], prev + tt - ff + 1);
							}
					}
	int ans = inf;
	for (fr = 0; fr < C; fr++)
		for (to = fr; to < C; to++)
			for (side = 0; side < 2; side++)
				Update(ans, opt[R - 1][fr][to][side]);
	if (ans == inf) printf("No\n");
	else printf("Yes %d\n", ans);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}