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

const int MAX_N = 100 + 10;
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int testNum;
int n, m;
int h[MAX_N][MAX_N];
int parent[MAX_N * MAX_N];
char color[MAX_N * MAX_N];

int findParent(int id)
{
	if (parent[id] == -1)
		return id;
	else
		return parent[id] = findParent(parent[id]);
}
int next(int i, int j)
{
	int lowest = h[i][j];
	int lowestId = -1;
	for (int d = 0; d < 4; d++)
		if (0 <= i + dx[d] && i + dx[d] < n && 0 <= j + dy[d] && j + dy[d] < m && h[i + dx[d]][j + dy[d]] < lowest)
		{
			lowest = h[i + dx[d]][j + dy[d]];
			lowestId = (i + dx[d]) * m + j + dy[d];
		}
	return lowestId;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) 
				scanf("%d", &h[i][j]);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				parent[i * m + j] = next(i, j);
		printf("Case #%d:\n", testInd + 1);
		char curColor = 'a';
		fill(color, color + n * m, '0');
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				int id = findParent(i * m + j);
				if (color[id] == '0')
					color[id] = curColor++;
				color[i * m + j] = color[id];
				printf("%c%c", color[i * m + j], j == m - 1 ? '\n' : ' ');
			}
	}
	return 0;
}
