#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const int N = 55;
string g[N];
char f[N][N];
int n, k;
const int dx[] = {1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1};

int calc(int x, int y, int xx, int yy)
{
	int cnt = 1;
	while (f[x+cnt*xx][y+cnt*yy] == f[x][y])
		cnt++;
	return cnt-1;
}
void work()
{
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
			cin >> g[i];
	for (int i = 1; i <= n; i++)
	{
		while (g[i].find('.') != string::npos)
			g[i].erase(g[i].find('.'), 1);
	}
//	for (int i = 1; i <= n; i++)
//		cout << g[i] << endl;
		
	memset(f, '.', sizeof(f));
	for (int i = 1; i <= n; i++)
		for (int j = g[i].size()-1; j >= 0; j--)
			f[i][n+j-(g[i].size()-1)] = g[i][j];
/*
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			cout << f[i][j];
		cout << endl;
	}
*/
	bool red = false;
	bool blue = false;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (f[i][j] == 'R' || f[i][j] == 'B')
			{
				for (int p = 0; p < 4; p++)
				{
					int l1 = calc(i, j, dx[p], dy[p]);
					int l2 = calc(i, j, -dx[p], -dy[p]);
					if (l1 + l2 + 1 >= k)
					{
						if (f[i][j] == 'R') red = true;
						else blue = true;
					}
				}
			}
	if (red && blue)
		cout << "Both" << endl;
	else if (red)
		cout << "Red" << endl;
	else if (blue)
		cout << "Blue" << endl;
	else
		cout << "Neither" << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		work();
	}
}