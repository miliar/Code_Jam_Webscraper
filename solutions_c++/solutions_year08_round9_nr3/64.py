#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <complex>
#include <bitset>

#define PI 3.14159265358979
#define EPS 1E-10
#define INF 1000000000

using namespace std;

int hint[5][5];
int isset[5][5];
int dir[9][2] =
{
	{-1, -1}, {-1, 0}, {-1, 1}, {0, 0},
	{0, -1}, {0, 1}, {1, -1}, {1, 0},
	{1, 1},
};

int go(int r, int c, int x, int y)
{
	if(y == c)
	{
		if(x)
		{
			for(int i = 0; i < c; ++i) if(hint[x - 1][i]) return 0;
		}
		return go(r, c, x + 1, 0);
	}
	if(x == r)
	{
		for(int i = 0; i < c; ++i) if(hint[r - 1][i]) return 0;
		int res = 0;
		for(int i = 0; i < c; ++i) res += isset[r / 2][i];
		return res;
	}
	int res = 0;
	for(int i = 0; i < 2; ++i)
	{
		isset[x][y] = i;
		bool ok = true;
		for(int j = 0; j < 9; ++j)
		{
			int dx = x + dir[j][0], dy = y + dir[j][1];
			if(dx < 0 || dy < 0 || dx >= r || dy >= c) continue;
			hint[dx][dy] -= i;
			if(hint[dx][dy] < 0) ok = false;
		}
		if(ok) res = max(res, go(r, c, x, y + 1));
		for(int j = 0; j < 9; ++j)
		{
			int dx = x + dir[j][0], dy = y + dir[j][1];
			if(dx < 0 || dy < 0 || dx >= r || dy >= c) continue;
			hint[dx][dy] += i;
		}
	}
	return res;
}

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int r, c;
		cin >> r >> c;
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j) cin >> hint[i][j];
		}
		printf("Case #%d: ", t);
		printf("%d\n", go(r, c, 0, 0));
	}
	return 0;
}
