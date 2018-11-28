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

const int MAX_SIZE = 30;
const int MAX_CNT = MAX_SIZE * MAX_SIZE;
const int DX[4] = {1, 0, -1, 0};
const int DY[4] = {0, 1, 0, -1};
const int INF = 1000000000;

int n, m;
int cnt;
char chess[MAX_SIZE][MAX_SIZE + 1];
int dist[MAX_SIZE][MAX_SIZE][MAX_SIZE][MAX_SIZE];
pair<int, int> prev[MAX_SIZE][MAX_SIZE][MAX_SIZE][MAX_SIZE];
bool used[MAX_SIZE][MAX_SIZE];
pair<int, int> tree[MAX_CNT];
int distT[MAX_CNT];
int prevT[MAX_CNT];
bool usedT[MAX_CNT];

bool isValid(int i, int j)
{
	return (0 <= i && i < n && 0 <= j && j < m && chess[i][j] != '.');
}
void bfs(int sx, int sy)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			dist[sx][sy][i][j] = -1;
			prev[sx][sy][i][j] = make_pair(-1, -1);
		}
	static queue<pair<int, int> > q;
	q.push(make_pair(sx, sy));
	dist[sx][sy][sx][sy] = 0;
	while (!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int k = 0; k < 4; k++)
		{
			int tx = x + DX[k];
			int ty = y + DY[k];
			if (isValid(tx, ty) && dist[sx][sy][tx][ty] == -1)
			{
				dist[sx][sy][tx][ty] = dist[sx][sy][x][y] + 1;
				prev[sx][sy][tx][ty] = make_pair(x, y);
				q.push(make_pair(tx, ty));
			}
		}
	}
}
void setPathUsed(int from, int to)
{
	int sx = tree[from].first;
	int sy = tree[from].second;
	int tx = tree[to].first;
	int ty = tree[to].second;
	while (tx > -1)
	{
		used[tx][ty] = true;
		pair<int, int> tmp = prev[sx][sy][tx][ty];
		tx = tmp.first;
		ty = tmp.second;
	}
}
int mst()
{
	int ret = 0;
	for (int k = 0; k < cnt; k++)
	{
		distT[k] = INF;
		usedT[k] = false;
		prevT[k] = -1;
	}
	static priority_queue<pair<int, int> > q;
	q.push(make_pair(0, 0));
	distT[0] = 0;
	while (!q.empty())
	{
		int d = q.top().first;
		int i = q.top().second;
		q.pop();
		if (usedT[i])
			continue;
		usedT[i] = true;
		ret += (d + 1) * d / 2;
		for (int j = 0; j < cnt; j++)
			if (!usedT[j] && distT[j] > dist[tree[i].first][tree[i].second][tree[j].first][tree[j].second])
			{
				distT[j] = dist[tree[i].first][tree[i].second][tree[j].first][tree[j].second];
				prevT[j] = i;
				q.push(make_pair(distT[j], j));
			}
	}
	for (int k = 0; k < cnt; k++)
		if (prevT[k] != -1)
			setPathUsed(prevT[k], k);
	return ret;
}
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", chess[i]);
		cnt = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (isValid(i, j))
				{
					used[i][j] = false;
					if (chess[i][j] == 'T')
						tree[cnt++] = make_pair(i, j);
					bfs(i, j);
				}
		int ans = mst();
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (isValid(i, j) && !used[i][j])
				{
					used[i][j] = true;
					int minDist = INF;
					for (int k = 0; k < cnt; k++)
						minDist = min(minDist, dist[i][j][tree[k].first][tree[k].second]);
					ans += minDist;
				}
		printf("Case #%d: %d\n", testInd + 1, ans);
	}
	return 0;
}
