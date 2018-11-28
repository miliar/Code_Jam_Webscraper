#include <iostream>
#include <climits>

#define INF (INT_MAX/2)
#define MAXY 64
#define MAXX 64

using namespace std;

char map[MAXY][MAXX];
int nrow, ncol, maxjump;

int solve(int y, int x)
{
	if (y >= nrow-1)
		return 0;

	int left = x, right = x;

	while (left-1 >= 0 && map[y+1][(left-1)] == '#' && map[y][left-1] == '.')
		left --;

	while (right+1 < ncol && map[y+1][right+1] == '#' && map[y][right+1] == '.')
		right ++;

	int ret = INF;

	for (int x2 = left; x2 <= right; x2++)
		if (map[y+1][x2] == '#') {
			map[y+1][x2] = '.';
			
			if (x2-1 >= left)
				ret = min(ret, 1+solve(y, x2-1));
			if (x2+1 <= right)
				ret = min(ret, 1+solve(y, x2+1));

			map[y+1][x2] = '#';
		}

	if (left-1 >= 0 && map[y][left-1] == '.') {
		int fallsize = 0;

		int y2;
		for (y2 = y; map[y2+1][left-1] == '.' && y2+1 <= nrow-1; y2++, fallsize ++);


		if (fallsize <= maxjump)
			ret = min(ret, solve(y2, left-1));
	}
	if (right+1 < ncol && map[y][right+1] == '.') {
		int fallsize = 0;

		int y2;
		for (y2 = y; map[y2+1][right+1] == '.' && y2+1 <= nrow-1; y2++, fallsize ++);

		if (fallsize <= maxjump)
			ret = min(ret, solve(y2, right+1));
	}

	return ret;
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		scanf("%d %d %d", &nrow, &ncol, &maxjump);

		for (int y = 0; y < nrow; y++)
			for (int x = 0; x < ncol; x++)
				scanf(" %c", &map[y][x]);

		for (int x = 0; x < ncol; x++)
			map[nrow][x] = '.';

		int ret = solve(0, 0);

		if (ret < INF)
			printf("Case #%d: Yes %d\n", t+1, ret);
		else
			printf("Case #%d: No\n", t+1);
	}

	return 0;
}
