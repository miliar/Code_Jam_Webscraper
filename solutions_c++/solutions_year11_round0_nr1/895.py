#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

vector < pair < int, int > > a;
int n;

int d[110][110][110];

queue < pair < int, pair < int, int > > > q;

#define mp(a, b, c) make_pair((a), make_pair((b), (c)))

bool val(int u)
{
	return (1 <= u && u <= 100);
}

void solve(int test)
{
	a.clear();
	scanf("%d", &n);
	for (int i = 1; i <= n; i ++)
	{
		string s;
		int d;
		cin >> s;
		cin >> d;
		if (s == "O") a.push_back(make_pair(1, d)); else a.push_back(make_pair(2, d));
	}

	for (int i = 1; i <= 100; i ++)
		for (int j = 1; j <= 100; j ++)
			for (int k = 0; k <= 100; k ++)
				d[i][j][k] = 1000000000;

	q.push(mp(1, 1, 0));
	d[1][1][0] = 0;
	while (!q.empty())
	{
		pair < int, pair < int, int > > p = q.front(); q.pop();
		int u = p.first, v = p.second.first, w = p.second.second;
		if (w == n) continue;

		for (int i = -1; i <= 1; i ++)
			for (int j = -1; j <= 1; j ++)
				if (val(u + i) && val(v + j))
				{
					int nu = u + i, nv = v + j, nw = w;
					if (a[w].first == 1 && i == 0 && u == a[w].second) nw ++; else
						if (a[w].first == 2 && j == 0 && v == a[w].second) nw ++;
					if (d[nu][nv][nw] > d[u][v][w] + 1)
					{
						d[nu][nv][nw] = d[u][v][w] + 1;
						q.push(mp(nu, nv, nw));
					}
				}
	}
	int res = 1000000000;
	for (int i = 1; i <= 100; i ++)
		for (int j = 1; j <= 100; j ++)
			res = min(res, d[i][j][n]);
	printf("Case #%d: %d\n", test, res);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++)
		solve(i);
	return 0;
}