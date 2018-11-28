#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXN 105

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int T, H, W;
int R[MAXN][MAXN], Color[MAXN][MAXN];
char Ans[MAXN][MAXN];
pair <int, int> App[MAXN * MAXN];

int cmp(pair <int, int> p1, pair <int, int> p2){
	return R[p1.first][p1.second] > R[p2.first][p2.second];
}

int dfs(int x, int y, char c){
	Ans[x][y] = c;
	for (int i = 0; i < 4; i ++){
		int nx = x + dx[i], ny = y + dy[i];
		if (nx < H && nx >= 0 && ny < W && ny >= 0 && Color[nx][ny] == Color[x][y] && !Ans[nx][ny]) dfs(nx, ny, c);
	}
	return 0;
}

int main(void){
	int tc = 1;
	for (scanf("%d", &T); T; T --){
		int aSize = 0;
		scanf("%d%d", &H, &W);
		for (int i = 0; i < H; i ++){
			for (int j = 0; j < W; j ++){
				scanf("%d", R[i] + j);
				App[aSize ++] = make_pair(i, j);
			}
		}
		sort(App, App + aSize, cmp);
		memset(Color, 255, sizeof(Color));
		int cSize = 0;
		for (int i = 0; i < aSize; i ++){
			int x = App[i].first, y = App[i].second;
			if (Color[x][y] != -1) continue;
			while (1){
				int dir = -1;
				for (int j = 0; j < 4; j ++){
					int nx = x + dx[j], ny = y + dy[j];
					if (nx >= 0 && nx < H && ny >= 0 && ny < W && R[nx][ny] < R[x][y]){
						if (dir == -1) dir = j;
						else if (R[nx][ny] < R[x + dx[dir]][y + dy[dir]]) dir = j;
					}
				}
				if (dir == -1) break;
				x += dx[dir];
				y += dy[dir];
			}
			int nowColor;
			if (Color[x][y] != -1) nowColor = Color[x][y];
			else nowColor = cSize ++;
			x = App[i].first;
			y = App[i].second;
			Color[x][y] = nowColor;
			while (1){
				int dir = -1;
				for (int j = 0; j < 4; j ++){
					int nx = x + dx[j], ny = y + dy[j];
					if (nx >= 0 && nx < H && ny >= 0 && ny < W && R[nx][ny] < R[x][y]){
						if (dir == -1) dir = j;
						else if (R[nx][ny] < R[x + dx[dir]][y + dy[dir]]) dir = j;
					}
				}
				if (dir == -1) break;
				x += dx[dir];
				y += dy[dir];
				Color[x][y] = nowColor;
			}
		}
		memset(Ans, 0, sizeof(Ans));
		cSize = 0;
		for (int i = 0; i < H; i ++){
			for (int j = 0; j < W; j ++){
				if (!Ans[i][j]){
					dfs(i, j, cSize + 'a');
					cSize ++;
				}
			}
		}
		printf("Case #%d:\n", tc ++);
		for (int i = 0; i < H; i ++){
			for (int j = 0; j < W; j ++){
				putchar(Ans[i][j]);
				if (j + 1 < W) printf(" ");
				else printf("\n");
			}
		}
	}
	return 0;
}
