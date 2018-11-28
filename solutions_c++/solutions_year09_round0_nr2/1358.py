#include <cstdio>
#include <cstring>

int elevations[128][128];
char basin[128][128];
int H, W;
int dxy[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

int kamo(int x, int y){
	if (x <= 0 || y <= 0 || x > H || y > W) return -1;

	int minp = 0;

	for (int p = 1; p < 4; ++p){
		if (elevations[x+dxy[p][0]][y+dxy[p][1]] < elevations[x+dxy[minp][0]][y+dxy[minp][1]]) minp = p;
	}
	if (elevations[x+dxy[minp][0]][y+dxy[minp][1]] >= elevations[x][y]) return -1;
	return minp;
}

void load(){
	scanf("%d%d", &H, &W);

	memset(elevations, 0x3f, sizeof elevations);

	for (int i = 1; i <= H; ++i){
		for (int j = 1; j <= W; ++j){
			scanf("%d", &elevations[i][j]);
			basin[i][j] = '.';
		}
	}
}

void dfs(int x, int y, char mark){
	if (basin[x][y] != '.') return;

	basin[x][y] = mark;

	int p = kamo(x, y);

	if (p != -1) dfs(x+dxy[p][0], y+dxy[p][1], mark);

	for (p = 0; p < 4; ++p){
		if (kamo(x-dxy[p][0], y-dxy[p][1]) == p) dfs(x-dxy[p][0], y-dxy[p][1], mark);
	}
}

int main(){
	int tp = 0;
	scanf("%d", &tp);

	for (int tt = 1; tt <= tp; ++tt){
		load();
		char bs = 'a';

		for (int i = 1; i <= H; ++i){
			for (int j = 1; j <= W; ++j){
				if (basin[i][j] == '.') dfs(i, j, bs++);
			}
		}

		printf("Case #%d:\n", tt);
		for (int i = 1; i <= H; ++i){
			for (int j = 1; j <= W; ++j){
				printf("%c ", basin[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}
