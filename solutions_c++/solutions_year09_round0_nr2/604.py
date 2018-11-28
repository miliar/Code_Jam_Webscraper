#include <stdio.h>
#include <vector>

using namespace std;

int height[100][100];
char mark[100][100];
vector< pair<int, int> > edge[100][100];
int tc, h, w, step;

int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

void fill(int y, int x, int color) {
	mark[y][x] = 'a' + color;
	for (int i = 0; i < edge[y][x].size(); i ++) {
		int yy = edge[y][x][i].first;
		int xx = edge[y][x][i].second;
		if (mark[yy][xx] == 0)
			fill(yy, xx, color);
	}
	return;
}

int main () {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t ++) {
		scanf("%d %d", &h, &w);
		for (int i = 0; i < h; i ++)
			for (int j = 0; j < w; j ++) {
				scanf("%d", &height[i][j]);
				mark[i][j] = 0;
				edge[i][j].clear();
			}
		step = 0;
		for (int i = 0; i < h; i ++)
			for (int j = 0; j < w; j ++) {
				int cost = height[i][j], y0, x0;
				for (int k = 0; k < 4; k ++) {
					int y1 = i + dir[k][0];
					int x1 = j + dir[k][1];
					if (x1 < 0 || x1 >= w || y1 < 0 || y1 >= h) continue;
					if (height[y1][x1] < cost) {
						cost = height[y1][x1];
						x0 = x1;
						y0 = y1;
					}
				}
				if (cost != height[i][j]) {
					pair <int, int> p1, p2;
					p1.first = y0, p1.second = x0;
					edge[i][j].push_back(p1);
					p2.first = i, p2.second = j;
					edge[y0][x0].push_back(p2);
				}
			}
		for (int i = 0; i < h; i ++)
			for (int j = 0; j < w; j ++)
				if (mark[i][j] == 0) {
					fill(i, j, step);
					step ++;
				}
		printf("Case #%d:\n", t);
		for (int i = 0 ; i < h; i ++) {
			for (int j = 0; j < w; j ++)
				printf("%c ", mark[i][j]);
			printf("\n");
		}
	}
	return 0;
}
