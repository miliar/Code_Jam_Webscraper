#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

const int MAX_SIZE = 100;

int w, h;
int dx1, dy1;
int dx2, dy2;
int sx, sy;
bool used[MAX_SIZE][MAX_SIZE];

bool inRange(int i, int j)
{
	return (0 <= i && i < w && 0 <= j && j < h);
}
void dfs(int x, int y)
{
	if (!inRange(x, y))
		return;
	if (used[x][y])
		return;
	used[x][y] = true;
	dfs(x + dx1, y + dy1);
	dfs(x + dx2, y + dy2);
}
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d", &w, &h);
		scanf("%d%d", &dx1, &dy1);
		scanf("%d%d", &dx2, &dy2);
		scanf("%d%d", &sx, &sy);
		memset(used, 0, sizeof(used));
		dfs(sx, sy);
		int cnt = 0;
		for (int i = 0; i < w; i++)
			for (int j = 0; j < h; j++)
				if (used[i][j])
					cnt++;
		printf("Case #%d: %d\n", testInd + 1, cnt);
	}
	return 0;
}
