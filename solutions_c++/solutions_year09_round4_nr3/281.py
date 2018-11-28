#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int n, m;
bool g[201][201];
int p[201][56];
bool vis[201];
int from[201];

bool match(int u)
{
	for (int i = 0; i < n; i++)
		if (!vis[i] && g[u][i])
		{
			vis[i] = true;
			if (from[i] == -1 || match(from[i]))
			{
				from[i] = u;
				return true;
			}
		}
	return false;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t, T;
	cin >> T;
	int a, b;
	for (int t = 1; t <= T; t++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> p[i][j];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (i != j)
				{
					g[i][j] = true;
					for (int k = 0; k < m; k++)
						if (p[i][k] <= p[j][k])
							g[i][j] = false;
				}
		int ans = 0;
		memset(from, 0xff, sizeof(from));
		for (int i = 0; i < n; i++)
		{
			memset(vis, 0, sizeof(vis));
			if (match(i)) ans++;
		}
		cout << "Case #" << t << ": " << n-ans << endl;
	}
}