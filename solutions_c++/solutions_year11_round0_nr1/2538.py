#include <stdio.h>
#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int t, n;
const int inf = 1000 * 1000 * 1000;
vector<int> T, L;
int d[1 << 7][1 << 7][1 << 7];
int u[1 << 7][1 << 7][1 << 7];
const int dx[9] = {0, 0, 0, 1, 1, 1, -1, -1, -1};
const int dy[9] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
queue<int> Q;

bool bound(int x, int y)
{
	return x >= 1 && y >= 1 && x <= 100 && y <= 100;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		int k, x;
		cin >> k;
		n = k;
		T.assign(k, 0);
		L.assign(k, 0);
		string s;
		for(int i = 0; i < k; ++i)
		{
			cin >> s;
			T[i] = s == "O";
			cin >> L[i];
		}
		Q.push(1);
		Q.push(1);
		Q.push(0);
		memset(u, 0, sizeof(u));
		memset(d, 0, sizeof(d));
		u[1][1][0] = 1;
		while (!Q.empty())
		{
			int x = Q.front();
			Q.pop();
			int y = Q.front();
			Q.pop();
			int k = Q.front();
			Q.pop();
			if (k == n)
				continue;
			for(int i = 0; i < 9; ++i)
			{
				int tox = x + dx[i];
				int toy = y + dy[i];
				if (bound(tox, toy))
				{
					if (!u[tox][toy][k])
					{
						d[tox][toy][k] = d[x][y][k] + 1;
						u[tox][toy][k] = 1;
						Q.push(tox);
						Q.push(toy);
						Q.push(k);
					}
					if (dx[i] == 0)
					{
						if (!u[tox][toy][k + 1] && T[k] && L[k] == tox)
						{
							d[tox][toy][k + 1] = d[x][y][k] + 1;
							u[tox][toy][k + 1] = 1;
							Q.push(tox);
							Q.push(toy);
							Q.push(k + 1);
						}
					}
					if (dy[i] == 0)
					{
						if (!u[tox][toy][k + 1] && !T[k] && L[k] == toy)
						{
							d[tox][toy][k + 1] = d[x][y][k] + 1;
							u[tox][toy][k + 1] = 1;
							Q.push(tox);
							Q.push(toy);
							Q.push(k + 1);
						}
					}
				}
			}
		}
		int res = inf;
		for(int i = 0; i < (1 << 7); ++i)
			for(int j = 0; j < (1 << 7); ++j)
				if (d[i][j][n] > 0)
					res = min(res, d[i][j][n]);
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}