#include <iostream>
#include <queue>
#include<algorithm>
using namespace std;

int X, Y;

int map[150][150];
char mark[150][150];

int temp_x, temp_y;
char this_mark;

struct point {
	int x;
	int y;
};

int find_max() {
	int t = -1;
	for (int xx = 0; xx < X; xx++) {
		for (int yy = 0; yy < Y; ++yy) {
			if (mark[xx][yy] <= 0 && map[xx][yy] > t) {
				t = map[xx][yy];
				temp_x = xx;
				temp_y = yy;
			}
		}
	}
	return t;
}

void remark(char a, char b) {
	for (int xx = 0; xx < X; xx++) {
		for (int yy = 0; yy < Y; ++yy) {
			if (mark[xx][yy] == a)
				mark[xx][yy] = b;
		}
	}
}

bool mark_basins(int xx, int yy) {
	point pp;
	pp.x = xx;
	pp.y = yy;
	mark[xx][yy] = this_mark;

	bool can_go = true;
	while (can_go) {

		int tx = pp.x;
		int ty = pp.y;
		int height = map[tx][ty];

		// north
		if (pp.x > 0 && map[pp.x - 1][pp.y] < height) {
			tx = pp.x - 1;
			ty = pp.y;
			height = map[tx][ty];
		}

		// west
		if (pp.y > 0 && map[pp.x][pp.y - 1] < height) {
			tx = pp.x;
			ty = pp.y - 1;
			height = map[tx][ty];
		}

		// east
		if (pp.y < Y - 1 && map[pp.x][pp.y + 1] < height) {
			tx = pp.x;
			ty = pp.y + 1;
			height = map[tx][ty];
		}

		// South
		if (pp.x < X - 1 && map[pp.x + 1][pp.y] < height) {
			tx = pp.x + 1;
			ty = pp.y;
			height = map[tx][ty];
		}

		if (tx == pp.x && ty == pp.y) {
			can_go = false;
		} else {
			if (mark[tx][ty] > 0) {
				if (this_mark != mark[tx][ty]) {
					remark(this_mark, mark[tx][ty]);
					return false;
				} else
					return true;
			} else {
				mark[tx][ty] = this_mark;
				pp.x = tx;
				pp.y = ty;
			}
		}
	}
	return true;
}

char dfs(int xx, int yy) {
	int tx = xx;
	int ty = yy;
	int height = map[tx][ty];
	// north
	if (xx > 0 && map[xx - 1][yy] < height) {
		tx = xx - 1;
		ty = yy;
		height = map[tx][ty];
	}

	// west
	if (yy > 0 && map[xx][yy - 1] < height) {
		tx = xx;
		ty = yy - 1;
		height = map[tx][ty];
	}

	// east
	if (yy < Y - 1 && map[xx][yy + 1] < height) {
		tx = xx;
		ty = yy + 1;
		height = map[tx][ty];
	}

	// South
	if (xx < X - 1 && map[xx + 1][yy] < height) {
		tx = xx + 1;
		ty = yy;
		height = map[tx][ty];
	}
	if (tx == xx && ty == yy) {
		//drainage basin
		if (mark[xx][yy] <= 0) {
			mark[xx][yy] = this_mark;
			this_mark++;
		}
	} else {
		if (mark[tx][ty] > 0)
			mark[xx][yy] = mark[tx][ty];
		else
			mark[xx][yy] = dfs(tx, ty);
	}
	return mark[xx][yy];
}

void calc() {
	while (find_max() >= 0) {
		/*
		 if (mark_basins(temp_x, temp_y)) {
		 this_mark++;
		 }
		 */
		dfs(temp_x, temp_y);
	}
}

void calc2() {
	for (int xx = 0; xx < X; xx++) {
		for (int yy = 0; yy < Y; ++yy) {
			/*
			 if (mark_basins(temp_x, temp_y)) {
			 this_mark++;
			 }
			 */
			dfs(xx, yy);
		}
	}
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-largett.ttt", "w", stdout);

	int K;
	cin >> K;
	for (int i = 0; i < K; ++i) {
		this_mark = 'a';
		cin >> X >> Y;
		temp_x = 0;
		temp_y = 0;

		memset(map, 0, sizeof(int) * 150 * 150);
		memset(mark, 0, sizeof(char) * 150 * 150);

		for (int xx = 0; xx < X; xx++) {
			for (int yy = 0; yy < Y; ++yy) {
				scanf("%d", &(map[xx][yy]));
			}
		}

		calc2();

		printf("Case #%d:\n", i + 1);
		/*
		 for (int xx = 0; xx < X; xx++) {
		 for (int yy = 0; yy < Y; ++yy) {
		 printf("%d", map[xx][yy]);
		 if (yy != Y - 1)
		 printf(" ");
		 }
		 printf("\n");
		 }
		 */
		for (int xx = 0; xx < X; xx++) {
			for (int yy = 0; yy < Y; ++yy) {
				printf("%c", mark[xx][yy]);
				if (yy != Y - 1)
					printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}
