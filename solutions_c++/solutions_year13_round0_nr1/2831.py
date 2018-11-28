#include <cstdio>

using namespace std;

const int N = 4;

char b[N][N];

int draw() {
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			if (b[i][j] == '.')
				return 3;
	return 2;
}

bool hasWon(int x, int y, char ch, int ax, int ay) {
	if (x == N || y == N || x < 0 || y < 0)
		return true;
	if (b[x][y] != ch && b[x][y] != 'T')
		return false;
	return hasWon(x+ax, y+ay, ch, ax, ay);
}

int solve() {
	bool valX, valO;
	valX = hasWon(0, 0, 'X', 1, 1);
	valO = hasWon(0, 0, 'O', 1, 1);
	valO |= hasWon(3, 0, 'O', -1, 1);
	valX |= hasWon(3, 0, 'X', -1, 1);

	for (int i = 0; i < N; ++i) {
		valX |= hasWon(i, 0, 'X', 0, 1);
		valO |= hasWon(i, 0, 'O', 0, 1);
		valX |= hasWon(0, i, 'X', 1, 0);
		valO |= hasWon(0, i, 'O', 1, 0);
	}
	if (valX)
		return 1;
	if (valO)
		return 0;

	return draw();
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int t;
	scanf("%d\n", &t);
	for (int cur = 1; cur <= t; ++cur) {
		gets(b[0]);
		gets(b[1]);
		gets(b[2]);
		gets(b[3]);
		scanf("\n");

		printf("Case #%d: ", cur);
		int res = solve();
		if (res == 1)
			printf("X won\n");
		else if (res == 0)
			printf("O won\n");
		else if (res == 2)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}

	return 0;
}
