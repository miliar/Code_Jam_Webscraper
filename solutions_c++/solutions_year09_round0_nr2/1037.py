#include <cstdio>

const int MAX = 128;

int H, W;
int h[MAX][MAX];
char letter[MAX][MAX];
char next_basin;

// North, West, East, South
int dx[] = {0, -1, +1,  0};
int dy[] = {-1, 0,  0, +1};

char go(int y, int x)
{
	if (letter[y][x] != '.')
		return letter[y][x];

	int next_x, next_y, min_h = h[y][x];
	for (int i = 0; i < 4; i++) {
		int y1 = y+dy[i], x1 = x+dx[i];
		if (x1 < 0 || x1 >= W || y1 < 0 || y1 >= H)
			continue;
		if (h[y1][x1] < min_h) {
			min_h = h[y1][x1];
			next_x = x1;
			next_y = y1;
		}
	}

	if (min_h >= h[y][x])
		return letter[y][x] = next_basin++;
	return letter[y][x] = go(next_y, next_x);
}

void solve()
{
	scanf("%d %d", &H, &W);
	for (int y = 0; y < H; y++)
		for (int x = 0; x < W; x++) {
			scanf("%d", &h[y][x]);
			letter[y][x] = '.';
		}

	next_basin = 'a';
	for (int y = 0; y < H; y++) {
		for (int x = 0; x < W; x++) {
			if (letter[y][x] == '.')
				go(y, x);
			if (x)
				putchar(' ');
			putchar(letter[y][x]);
		}
		puts("");
	}
}

int main()
{
//	freopen("input.txt", "rt", stdin);
	int num_tests;
	scanf("%d", &num_tests);
	for (int i_test = 0; i_test < num_tests; i_test++) {
		printf("Case #%d:\n", i_test+1);
		solve();
	}
}