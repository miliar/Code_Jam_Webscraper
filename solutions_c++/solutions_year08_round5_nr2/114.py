#include <stdio.h>

#define MAX 128

struct {
	int x, y, step;
}queue[MAX * MAX];

int r, c, use[MAX][MAX], count, end;
char map[MAX][MAX];

int wall(int x, int y) {
	if(x < 0 || x >= r || y < 0 || y >= c)return 1;
	if(map[x][y] == '#')return 1;
	return 0;
}
int side_wall(int x, int y) {
	if(wall(x - 1, y))return 1;
	if(wall(x + 1, y))return 1;
	if(wall(x, y - 1))return 1;
	if(wall(x, y + 1))return 1;
	return 0;
}
void move(int x, int y, int step) {
	if(wall(x, y))return;
	if(use[x][y])return;

	queue[count].x = x;
	queue[count].y = y;
	queue[count].step = step;
	count++;

	use[x][y] = 1;
	if(map[x][y] == 'X') {
		printf(" %d", step);
		end = 1;
	}
}
void warp(int x, int y, int step) {
	int i;

	for(i = y - 1; !wall(x, i); i--);
	move(x, i + 1, step);
	for(i = y + 1; !wall(x, i); i++);
	move(x, i - 1, step);
	for(i = x - 1; !wall(i, y); i--);
	move(i + 1, y, step);
	for(i = x + 1; !wall(i, y); i++);
	move(i - 1, y, step);
}

void find_ans() {
	int i, j;

	count = 0;
	end = 0;
	scanf("%d %d", &r, &c);
	for(i = 0; i < r; i++) {
		scanf("%s", map[i]);
		for(j = 0; j < c; j++) {
			use[i][j] = 0;
			if(map[i][j] == 'O') {
				move(i, j, 0);
			}
		}
	}

	for(i = 0; i < count && !end; i++) {
		move(queue[i].x + 1, queue[i].y, queue[i].step + 1);
		move(queue[i].x - 1, queue[i].y, queue[i].step + 1);
		move(queue[i].x, queue[i].y + 1, queue[i].step + 1);
		move(queue[i].x, queue[i].y - 1, queue[i].step + 1);
		if(side_wall(queue[i].x, queue[i].y)) {
			warp(queue[i].x, queue[i].y, queue[i].step + 1);
		}
	}

	if(!end)printf(" THE CAKE IS A LIE");
}

int main(int argc, char *argv[])
{
	int i, n;

	scanf("%d", &n);
	for(i = 1; i <= n; i++) {
		printf("Case #%d:", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
