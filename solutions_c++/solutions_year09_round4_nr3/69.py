#include <cstdio>
#include <queue>

using namespace std;

const int MAXR = 10;
const int MAXC = 6;

int r, c, f;

char maze[MAXR + 1][MAXC + 1];
int msks[MAXR + 1];

int dp[MAXR + 1][MAXC + 1][1 << MAXC];

int need[MAXC + 1][1 << MAXC];

int geth(int i, int j)
{
	int ret = 0;
	while (maze[i][j] == '.') {
		++i;
		++ret;
	}
	return ret;
}

void update(int i, int j, int msk, int dpval)
{
	if (dp[i][j][msk] == -1 || dp[i][j][msk] > dpval) {
		dp[i][j][msk] = dpval;
	}
}

void rundp(int i, int j, int msk)
{
	memset(need, -1, sizeof(need));
	need[j][msks[i + 1]] = dp[i][j][msk];
	queue<pair<int, int> > q;
	q.push(make_pair(j, msks[i + 1]));
	while (!q.empty()) {
		int curcol = q.front().first;
		int curmsk = q.front().second;
		q.pop();
		int dpval = need[curcol][curmsk];
		if (curcol > 0) {
			int leftcol = curcol - 1;
			if (!(msk & (1 << leftcol))) {
				if (!(curmsk & (1 << leftcol))) {
					int d = geth(i + 2, leftcol) + 1;
					if (d <= f) {
						if (d == 1) {
							update(i + 1, leftcol, curmsk, dpval);
						}
						else {
							update(i + d, leftcol, msks[i + d], dpval);
						}
					}
				}
				else {
					int nextmsk = curmsk ^ (1 << leftcol);
					if (need[curcol][nextmsk] == -1 || need[curcol][nextmsk] > dpval + 1) {
						need[curcol][nextmsk] = dpval + 1;
						q.push(make_pair(curcol, nextmsk));
					}
					if (need[leftcol][curmsk] == -1 || need[leftcol][curmsk] > dpval) {
						need[leftcol][curmsk] = dpval;
						q.push(make_pair(leftcol, curmsk));
					}
				}
			}
		}
		if (curcol < c - 1) {
			int leftcol = curcol + 1;
			if (!(msk & (1 << leftcol))) {
				if (!(curmsk & (1 << leftcol))) {
					int d = geth(i + 2, leftcol) + 1;
					if (d <= f) {
						if (d == 1) {
							update(i + 1, leftcol, curmsk, dpval);
						}
						else {
							update(i + d, leftcol, msks[i + d], dpval);
						}
					}
				}
				else {
					int nextmsk = curmsk ^ (1 << leftcol);
					if (need[curcol][nextmsk] == -1 || need[curcol][nextmsk] > dpval + 1) {
						need[curcol][nextmsk] = dpval + 1;
						q.push(make_pair(curcol, nextmsk));
					}
					if (need[leftcol][curmsk] == -1 || need[leftcol][curmsk] > dpval) {
						need[leftcol][curmsk] = dpval;
						q.push(make_pair(leftcol, curmsk));
					}
				}
			}
		}
	}
}

int run()
{
	scanf("%d %d %d", &r, &c, &f);
	for (int i = 0; i < r; ++i) {
		scanf("%s", maze[i]);
		msks[i] = 0;
		for (int j = c - 1; j >= 0; --j) {
			msks[i] <<= 1;
			if (maze[i][j] == '#') ++msks[i];
		}
	}
	for (int j = c - 1; j >= 0; --j) {
		maze[r][j] = '#';
		msks[r] = (1 << c) - 1;
	}
	memset(dp, -1, sizeof(dp));
	dp[0][0][msks[0]] = 0;
	for (int i = 0; i < r - 1; ++i) {
		for (int j = 0; j < c; ++j) {
			for (int msk = 0; msk < (1 << c); ++msk) {
				if (dp[i][j][msk] != -1) {
					rundp(i, j, msk);
				}
			}
		}
	}
	int res = -1;
	for (int i = 0; i < c; ++i) {
		for (int msk = 0; msk < (1 << c); ++msk) {
			if (dp[r - 1][i][msk] != -1) {
				if (res == -1 || res > dp[r - 1][i][msk]) {
					res = dp[r - 1][i][msk];
				}
			}
		}
	}
	return res;
}

int main()
{
	freopen("Bin.txt", "r", stdin);
	freopen("Bout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int ret = run();
		printf("Case #%d: ", i);
		if (ret == -1) {
			puts("No");
		}
		else {
			printf("Yes %d\n", ret);
		}
	}
	return 0;
}