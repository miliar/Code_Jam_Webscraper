#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#define file "a"
#define ldb long double
#define LL long long
const ldb eps = 1e-9;
const int INF = 1 << 30;
const LL LINF = 1ll << 60;
const ldb LDINF = 1e+70;
using namespace std;
int n, k;

char a[52][52], b[52][52];

void Load()
{
	cin >> n >> k;
		int i, j;
		for (i = 0; i < n;i++)
		{
			for (j = 0; j < n; j++)
			{
				cin >> a[i][j];
			}
		}
}

void Solve(int Test)
{
	int i, j;
	memset(b, 0, sizeof(b));
	
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			b[j][n - i - 1] = a[i][j];
		}
	}
	
	int res = 0, black, red, last;


	for (i = 0; i < n; i++)
	{
		last = n - 1;
		for (j = n - 1; j >= 0; j--)
		{
			if (b[j][i] == 'R' || b[j][i] == 'B')
			{
				b[last][i] = b[j][i];
				last--;
			}
		}
		for (j = last; j >= 0; j--) b[j][i] = '.';
	}
	int x, y, l;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			x = i, y = j;
			red = black = 0;
			for (l = 0; x < n && y < n && l < k; l++)
			{
				if (b[x][y] == 'R') red++;
				if (b[x][y] == 'B') black++;
				x++;
				y++;
			}
			if (black == k) res |= 1;
			if (red == k) res |= 2;
			x = i, y = j;
			red = black = 0;
			for (l = 0; x < n && y >= 0 && l < k; l++)
			{
				if (b[x][y] == 'R') red++;
				if (b[x][y] == 'B') black++;
				x++;
				y--;
			}
			if (black == k) res |= 1;
			if (red == k) res |= 2;
			x = i, y = j;
			red = black = 0;
			for (l = 0; x < n && l < k; l++)
			{
				if (b[x][y] == 'R') red++;
				if (b[x][y] == 'B') black++;
				x++;
			}
			if (black == k) res |= 1;
			if (red == k) res |= 2;
			x = i, y = j;
			red = black = 0;
			for (l = 0; y < n && l < k; l++)
			{
				if (b[x][y] == 'R') red++;
				if (b[x][y] == 'B') black++;
				y++;
			}
			if (black == k) res |= 1;
			if (red == k) res |= 2;
		}
	}
	cout << "Case #" << Test << ": ";
	if (res == 0)  cout << "Neither\n";
	else if (res == 1) cout << "Blue\n";
	else if (res == 2) cout << "Red\n";
	else cout << "Both\n";
}

int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}