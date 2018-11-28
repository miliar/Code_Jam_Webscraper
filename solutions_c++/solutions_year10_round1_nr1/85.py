#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/3)
#define MAXN 64

typedef long long lint;

using namespace std;

char _field[MAXN][MAXN], field[MAXN][MAXN];

void gravity(int n)
{
	for (int x = 0; x < n; x++)
		for (int y = n-1; y >= 0; y--)
			if (field[y][x] != '.') {
				char c = field[y][x];
				field[y][x] = '.';

				for (int y2 = n-1; y2 >= 0; y2--)
					if (field[y2][x] == '.') {
						field[y2][x] = c;
						break;
					}
			}
}

int check(int n, int k, char c)
{
	static int dx[4] = {0, 1, -1, 1}, dy[4] = {-1, 0, -1, -1};

	for (int dir = 0; dir < 4; dir++)
		for (int y = 0; y < n; y++)
			for (int x = 0; x < n; x++) {
				int y2 = y, x2 = x;
				int many = 0;

				while (many < k && 0 <= y2 && y2 < n && 0 <= x2 && x2 < n && field[y2][x2] == c) {
					many ++;
					y2 += dy[dir], x2 += dx[dir];
				}

				if (many >= k)
					return 1;
			}

	return 0;
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n, k;

		scanf("%d %d", &n, &k);
		
		for (int y = 0; y < n; y++)
			for (int x = 0; x < n; x++)
				scanf(" %c", &_field[y][x]);

		for (int y = 0; y < n; y++)
			for (int x = 0; x < n; x++)
				field[x][n-1-y] = _field[y][x];

		gravity(n);

		int r1 = check(n, k, 'R'), r2 = check(n, k, 'B');

		printf("Case #%d: ", t+1);
		if (r1 && r2)
			printf("Both\n");
		if (r1 && !r2)
			printf("Red\n");
		if (!r1 && r2)
			printf("Blue\n");
		if (!r1 && !r2)
			printf("Neither\n");
	}

	return 0;
}
