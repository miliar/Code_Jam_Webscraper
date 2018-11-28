#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

int testNum = 0;
int n, m;
double result;
char c[1000][1000];
bool possible;

void read()
{
	cin >> n >> m;
	int i, j;
	for (i = 1; i <= n; ++i)
	{
		c[i][0] = '.';
		c[i][m + 1] = '.';
		for (j = 1; j <= m; ++j)
			cin >> c[i][j];
	}
	for (j = 0; j <= m + 1; ++j)
	{
		c[0][j] = '.';
		c[n + 1][j] = '.';
	}
}

void printOut()
{
	cout << "Case #" << testNum << ": \n";
	if (!possible)
		cout << "Impossible\n";
	else
	{
		int i,j;
		for (i = 1; i <= n; ++i)
		{
			for (j = 1; j <= m; ++j)
				cout << c[i][j];
			cout << "\n";
		}
	}
}

void solve()
{
	read();
	possible = true;
	int i, j;
	for (i = 1; i <= n; ++i)
		for (j = 1; j <= m; ++j)
		{
			if (c[i][j] == '#')
			{
				if ((c[i + 1][j] != '#') || (c[i + 1][j + 1] != '#') || (c[i][j + 1] != '#'))
				{
					possible = false;
					printOut();
					return;
				}
				else
				{
					c[i][j] = '/';
					c[i][j + 1] = '\\';
					c[i + 1][j + 1] = '/';
					c[i + 1][j] = '\\';
				}
			}
		}
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		cerr << testNum << "\n";
		++testNum;
		solve();
		--t;
	}
return 0;
}