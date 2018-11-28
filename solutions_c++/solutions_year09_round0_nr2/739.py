#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory>
#include <queue>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()

typedef long double ld;
typedef long long int64;
typedef pair<ld, ld> pt;

#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define y1 PALEVO

int a[200][200];
char ans[200][200];
bool g[200][200][4];
bool used[200][200];
int n, m;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

queue <int> qx, qy;

void bfs(int x, int y, char c)
{
	ans[x][y] = c;
	used[x][y] = true;
	qx.push(x);
	qy.push(y);
	while (!qx.empty())
	{
		x = qx.front();
		qx.pop();
		y = qy.front();
		qy.pop();
		for (int k = 0; k < 4; k++)
		{
			if (g[x][y][k] && !used[x + dx[k]][y + dy[k]])
			{
				used[x + dx[k]][y + dy[k]] = true;
				ans[x + dx[k]][y + dy[k]] = c;
				qx.push(x + dx[k]);
				qy.push(y + dy[k]);
			}
		}
	}
}

int main()
{
	
	int t;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cin >> t;
	for (int test = 0; test < t; test++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &a[i][j]);
			}
		}
		memset(used, 0, sizeof used);
		memset(g, 0, sizeof g);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				int idx = -1;
				int val = a[i][j];
				for (int k = 0; k < 4; k++)
				{
					int nx = i + dx[k];
					int ny = j + dy[k];
					if (0 <= nx && nx < n && 0 <= ny && ny < m && a[nx][ny] < val)
					{
						idx = k;
						val = a[nx][ny];
					}
				}
				if (idx != -1)
				{
					g[i][j][idx] = true;
					g[i + dx[idx]][j + dy[idx]][3 - idx] = true;
				}
			}
		}
		char c = 'a';
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (!used[i][j])
				{
					bfs(i, j, c);
					++c;
				}
			}
		}
		printf("Case #%d:\n", test + 1);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				printf("%c", ans[i][j]);
				if (j < m - 1)
					printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}

