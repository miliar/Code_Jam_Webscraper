#include <stdio.h>

#define MAX 128
#define MAXA 1024000000

int h, w;
int map[MAX][MAX], next[MAX][MAX];
int di[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
char ans[MAX][MAX], ch;

void find_next(int x, int y) {
	int i, j;

	for(i = 0; i < 4; i++) {
		if(map[x + di[i][0]][y + di[i][1]] == MAXA)continue;
		if(map[x][y] > map[x + di[i][0]][y + di[i][1]])break;
	}
	if(i == 4) {
		next[x][y] = -1;
		return;
	}

	for(i = 0; i < 4; i++) {
		if(map[x + di[i][0]][y + di[i][1]] == MAXA)continue;
		for(j = i + 1; j < 4; j++) {
			if(map[x + di[j][0]][y + di[j][1]] == MAXA)continue;
			if(map[x + di[i][0]][y + di[i][1]] > map[x + di[j][0]][y + di[j][1]])break;
		}
		if(j == 4) {
			next[x][y] = i;
			return;
		}
	}
	printf("Error\n");
}

void find_all(int x, int y) {
	int i, tmp;

	if(ans[x][y])return;
	ans[x][y] = ch;

	for(i = 0; i < 4; i++) {
		if(map[x + di[i][0]][y + di[i][1]] == MAXA)continue;
		tmp = next[x + di[i][0]][y + di[i][1]];
		if(di[i][0] + di[tmp][0] == 0 && di[i][1] + di[tmp][1] == 0)
			find_all(x + di[i][0], y + di[i][1]);
	}
}

void find_sink(int x, int y) {
	while(next[x][y] != -1) {
		x += di[next[x][y]][0];
		y += di[next[x][y]][1];
	}

	find_all(x, y);
	ch++;
}

void find_ans() {
	int i, j;

	scanf("%d %d", &h, &w);

	for(i = 0; i <= h + 1; i++)
		map[i][0] = map[i][w + 1] = MAXA;
	for(j = 0; j <= w + 1; j++)
		map[0][j] = map[h + 1][j] = MAXA;

	for(i = 1; i <= h; i++)
		for(j = 1; j <= w; j++)
			scanf("%d", &map[i][j]);

	for(i = 1; i <= h; i++)
		for(j = 1; j <= w; j++)
			find_next(i, j);

	for(i = 1; i <= h; i++)
		for(j = 1; j <= w; j++)
			ans[i][j] = 0;

	ch = 'a';
	for(i = 1; i <= h; i++)
		for(j = 1; j <= w; j++)
			if(!ans[i][j])
				find_sink(i, j);

	for(i = 1; i <= h; i++) {
		for(j = 1; j <= w; j++) {
			if(j > 1)
				printf(" ");
			printf("%c", ans[i][j]);
		}
		printf("\n");
	}
}

int main(int argc, char *argv[])
{
	int i, t;

	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		printf("Case #%d:\n", i);
		find_ans();
	}

	return 0;
}
