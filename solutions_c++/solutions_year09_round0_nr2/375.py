#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>

#define rep(i, n) for (int i = 0; i < n; i++)
#define INT_INF 0x3f3f3f3f

using namespace std;

int D[][2] = {
	{-1, 0},
	{0, -1},
	{0, 1},
	{1, 0}
};

int alt[110][110];
char basin[110][110];
char curr;
int H, W;

char dfs(int x, int y) {
	if (basin[x][y]) return basin[x][y];

	int minalt = alt[x][y];
	int minx, miny;
	rep(i, 4) {
		int nextx = x + D[i][0];
		int nexty = y + D[i][1];
		if (nextx >= 0 && nextx < H && nexty >= 0 && nexty < W && alt[nextx][nexty] < minalt) {
			minalt = alt[nextx][nexty];
			minx = nextx;
			miny = nexty;
		}
	}

	if (minalt < alt[x][y]) {
		basin[x][y] = dfs(minx, miny);
	}
	else basin[x][y] = curr++;

	return basin[x][y];
}

int main() {
	int C;
	scanf("%d", &C);

	rep(c, C) {
		scanf("%d %d", &H, &W);
		curr = 'a';
		
		memset(basin, 0 , sizeof(basin));

		rep(i, H) {
			rep(j, W) {
				scanf("%d", &alt[i][j]);
			}
		}

		rep(i, H) {
			rep(j, W) {
				dfs(i, j);
			}
		}

		printf("Case #%d:\n", c+1);

		rep(i, H) {
			rep(j, W) {
				if (j) printf(" ");
				printf("%c", basin[i][j]);
			}
			printf("\n");
		}
	}
}

