#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;

char mat[105][105];
int height[105][105];
int dir[4][2] = {
-1,0,
0,-1,
0,1,
1,0
};
int n, m;
char curr_id;
void lable(int x, int y)
{
	if (mat[x][y])return;
	int pos = -1, best = 0x7fffffff;
	for (int i = 0; i < 4; ++i)
	{
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
		if (height[nx][ny] < best && height[nx][ny] < height[x][y]) best = height[nx][ny], pos = i;
	}
	if (pos == -1)
	{
		mat[x][y] = curr_id++;
	}
	else
	{
		int nx = x + dir[pos][0];
		int ny = y + dir[pos][1];
		if (mat[nx][ny] == 0) lable(nx, ny);
		mat[x][y] = mat[nx][ny];
	}
}
int main()
{
	//freopen("test_b.in", "r", stdin);freopen("test_b.out", "w", stdout);
	//freopen("B-small-attempt0.in", "r", stdin);freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);freopen("B-large.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int casid = 1;
	while (cas--)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) scanf("%d", height[i]+j);
		curr_id = 'a';
		memset(mat, 0, sizeof(mat));
		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (mat[i][j] == 0) lable(i, j);
		printf("Case #%d:\n", casid++);
		for (int i = 0; i < n; ++i)
		{
			putchar(mat[i][0]);
			for (int j = 1; j < m; ++j) printf(" %c", mat[i][j]);
			puts("");
		}
	}
	return 0;
}
