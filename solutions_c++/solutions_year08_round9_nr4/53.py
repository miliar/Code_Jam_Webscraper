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

struct unionfind
{
	int* p;
	unionfind(int size)
	{
		p = new int[size];
		for(int i = 0; i < size; ++i) p[i] = i;
	}
	void uni(int x, int y)
	{
		x = find(x); y = find(y);
		if(x == y) return;
		p[y] = x;
	}
	int find(int x)
	{
		if(p[x] == x) return x;
		return p[x] = find(p[x]);
	}
	bool same(int x, int y)
	{
		return find(x) == find(y);
	}
};

char ma[40][40];
int d[2][40][40];
int used[40][40];
int prev[2][40][40][2];
int dir[4][2] =
{
	{-1, 0}, {0, 1}, {1, 0}, {0, -1},
};

bool isin(int x, int y, int n, int m)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

void bfs(int sx, int sy, int p, int n, int m)
{
	d[p][sx][sy] = 0;
	queue<int> que;
	que.push(sx); que.push(sy);
	while(que.size())
	{
		int x = que.front(); que.pop();
		int y = que.front(); que.pop();
		for(int i = 0; i < 4; ++i)
		{
			int nx = x + dir[i][0], ny = y + dir[i][1];
			if(!isin(nx, ny, n, m) || d[p][nx][ny] != INF || ma[nx][ny] == '.') continue;
			d[p][nx][ny] = d[p][x][y] + 1;
			prev[p][nx][ny][0] = x;
			prev[p][nx][ny][1] = y;
			que.push(nx); que.push(ny);
		}
	}
}

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; ++i) scanf("%s", ma[i]);
		int fx = -1, fy = -1;
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j) if(ma[i][j] == 'T' && (i || j))
			{
				fx = i; fy = j;
				goto next;
			}
		}
		next:
		for(int k = 0; k < 2; ++k)
			for(int i = 0; i < n; ++i)
				for(int j = 0; j < m; ++j) d[k][i][j] = INF;
		memset(used, 0, 40 * 40 * 4);
		bfs(0, 0, 0, n, m);
		used[0][0] = 1;
		int res = 0;
		if(fx != -1)
		{
			bfs(fx, fy, 1, n, m);
			res = d[0][fx][fy] * (d[0][fx][fy] + 1) / 2;
			int px = fx, py = fy;
			while(px || py)
			{
				used[px][py] = 1;
				int temp = px;
				px = prev[0][px][py][0];
				py = prev[0][temp][py][1];
			}
		}
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j) if(!used[i][j] && ma[i][j] != '.')
			{
				res += min(d[0][i][j], d[1][i][j]);
			}
		}
		printf("Case #%d: ", t);
		printf("%d\n", res);
	}
	return 0;
}
