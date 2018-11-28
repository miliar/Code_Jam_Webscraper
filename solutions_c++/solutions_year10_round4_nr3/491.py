#include<stdio.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

int map[2][200][200];
int ymax = 105, xmax = 105;
int rect[2000][4];
int nrect;

bool checkmap(int f)
{
	int i, j;

	for (i = 0; i < ymax; i ++) {
		for (j = 0; j < xmax; j ++) {
			if (map[f][i][j] == 1)
				return false;
		}
	}

	return true;
}

int solve()
{
	int i, j, k;
	int round;
	int f;

	f = 0;
	for (i = 0; i < ymax; i ++) {
		for (j = 0; j < xmax; j ++) {
			map[f][i][j] = 0;
		}
	}

	for (i = 0; i < nrect; i ++) {
		for (j = rect[i][1]; j <= rect[i][3]; j ++) {
			for (k = rect[i][0]; k <= rect[i][2]; k ++) {
				map[f][j][k] = 1;
			}
		}
	}

	for (round = 0; ; round ++) {
		if (checkmap(f))
			return round;

		for (i = 0; i < ymax; i ++) {
			for (j = 0; j < xmax; j ++) {
				map[1 - f][i][j] = 0;
			}
		}

		for (i = 1; i < ymax - 1; i ++) {
			for (j = 1; j < xmax - 1; j ++) {
				if (map[f][i - 1][j] == 1 && map[f][i][j - 1] == 1) {
					map[1-f][i][j] = 1;
				}
				else if (map[f][i - 1][j] == 0 && map[f][i][j - 1] == 0) {
					map[1-f][i][j] = 0;
				}
				else {
					map[1-f][i][j] = map[f][i][j];
				}
			}
		}

		f = 1 - f;
	}
}

int main()
{
	int i, j, k;
	int t, nowt;

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;
		scanf("%d", &nrect);
		for (i = 0; i < nrect; i ++) {
			scanf("%d%d%d%d", &rect[i][0], &rect[i][1], &rect[i][2], &rect[i][3]);
		}

		printf("Case #%d: %d\n", nowt, solve());
	}

	return 0;
}
