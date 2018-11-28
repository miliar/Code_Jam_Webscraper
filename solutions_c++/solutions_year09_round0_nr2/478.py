#include <iostream>
#include <string>

using namespace std;

const int MAX_H = 100;
const int MAX_W = 100;
const int MAX_N = MAX_H * MAX_W;

int T;
int H;
int W;

int altitudes[MAX_H][MAX_W];

char basinAt;
char basin[MAX_H][MAX_W];

const int dy[] = { -1,  0, 0, 1 };
const int dx[] = {  0, -1, 1, 0 };

char fill(int y, int x)
{
	char &res = basin[y][x];
	if (res != 0)
		return res;
	int ny = -1;
	int nx = -1;
	for (int i = 0; i < 4; ++i) {
		int cy = y + dy[i];
		int cx = x + dx[i];
		if (0 <= cy && cy < H && 0 <= cx && cx < W && altitudes[cy][cx] < altitudes[y][x] && (ny == -1 || altitudes[cy][cx] < altitudes[ny][nx])) {
			ny = cy;
			nx = cx;
		}
	}
	if (ny == -1) 
		res = basinAt++;
	else 
		res = fill(ny, nx);
	return res;
}

int main()
{
	scanf("%d", &T);
	for (int casenum = 1; casenum <= T; ++casenum) {
		scanf("%d %d", &H, &W);
		for (int y = 0; y < H; ++y)
			for (int x = 0; x < W; ++x)
				scanf("%d", &altitudes[y][x]);
		basinAt = 'a';
		memset(basin, 0, sizeof(basin));
		printf("Case #%d:\n", casenum);
		for (int y = 0; y < H; ++y) {
			for (int x = 0; x < W; ++x) 
				printf("%c ", basin[y][x] = fill(y, x));
			printf("\n");
		}
		assert(basinAt <= 'z' + 1);
	}
	return 0;
}
