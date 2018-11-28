#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int n, m;
vector<vector<char> > a;

char sym(int x, int y)
{
	if (x >= n || y >= m)
		return '!';
	return a[x][y];
}

void solve(int test)
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			if (a[i][j] == '#')
			{
				if (sym(i + 1, j) == '#' && sym(i + 1, j + 1) == '#' && sym(i, j + 1) == '#')
				{
					a[i][j] = '/';
					a[i + 1][j] = (char)92;
					a[i + 1][j + 1] = '/';
					a[i][j + 1] = (char)92;
				} else{
					cout << "Case #" << test + 1 << ":" << endl << "Impossible" << endl;
					return;
				}
			}
		}
	cout << "Case #" << test + 1 << ":" << endl;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
			cout << a[i][j] ;
		cout << endl;
	}
	
}

int main()
{
//	char c;
//	cin >> c;
//	cout << (int) c << endl;
	
//	return 0;
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int T;
	cin >> T;

	for (int col = 0; col < T; ++col)
	{
		a.clear();
		cin >> n >> m;
		a.resize(n);
		for (int i = 0; i < n; ++i)
		{
			a[i].resize(m);
			for (int j = 0; j < m; ++j)
				cin >> a[i][j];
		}
		solve(col);
	}
	return 0;
}
