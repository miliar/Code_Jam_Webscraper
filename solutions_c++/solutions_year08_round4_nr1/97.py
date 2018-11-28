#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define INF 0x3f7f7f7f

int a[2][10001];
int g[10001], c[10001];
int m;

int fun (int n, int val)
{
	if (n > m) return -1;
	if (a[val][n] == -1)
	{
		a[val][n] = INF;
		if (g[n])
			if (val) a[val][n] <?= fun (2*n + 1, 1) + fun (2*n + 2, 1);
			else
			{
				a[val][n] <?= fun(2*n + 1, 0) + fun (2*n + 2, 0);
				a[val][n] <?= fun(2*n + 1, 0) + fun (2*n + 2, 1);
				a[val][n] <?= fun(2*n + 1, 1) + fun (2*n + 2, 0);
			}
		else
			if (val)
			{
				a[val][n] <?= fun(2*n + 1, 1) + fun (2*n + 2, 1);
				a[val][n] <?= fun(2*n + 1, 0) + fun (2*n + 2, 1);
				a[val][n] <?= fun(2*n + 1, 1) + fun (2*n + 2, 0);
			}
			else a[val][n] <?= fun (2*n + 1, 0) + fun (2*n + 2, 0);
		if (c[n])
			if (g[n])
				if (val)
				{
					a[val][n] <?= 1 + fun(2*n + 1, 1) + fun (2*n + 2, 1);
					a[val][n] <?= 1 + fun(2*n + 1, 0) + fun (2*n + 2, 1);
					a[val][n] <?= 1 + fun(2*n + 1, 1) + fun (2*n + 2, 0);
				}
				else a[val][n] <?= 1 + fun (2*n + 1, 0) + fun (2*n + 2, 0);
			else
				if (val) a[val][n] <?= 1 + fun (2*n + 1, 1) + fun (2*n + 2, 1);
				else
				{
					a[val][n] <?= 1 + fun(2*n + 1, 0) + fun (2*n + 2, 0);
					a[val][n] <?= 1 + fun(2*n + 1, 0) + fun (2*n + 2, 1);
					a[val][n] <?= 1 + fun(2*n + 1, 1) + fun (2*n + 2, 0);
				}
	}
	return a[val][n];
}

int main()
{
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++)
	{
		int v;
		cin >> m >> v;
		memset (g, 0, sizeof(g));
		memset (c, 0, sizeof(g));
		memset (a, -1, sizeof(a));
		for (int i = 0; i < (m-1)/2; i++) cin >> g[i] >> c[i];
		for (int i = (m-1)/2; i < m; i++)
		{
			int val;
			cin >> val;
			a[val][i] = 0;
			a[!val][i] = INF;
		}
		int ret = fun (0, v);
		cout << "Case #" << cc << ": ";
		if (ret == INF) cout << "IMPOSSIBLE" << endl;
		else cout << ret << endl;
	}
	return 0;
}
