#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
using namespace std;

int m, n;
vector<vector<char> > pic;
bool isValid(int i, int j)
{
	if (i + 1 < m && j + 1 < n)
	{
		if (pic[i][j] == '#' && pic[i + 1][j] == '#' && pic[i][j + 1] == '#' && pic[i + 1][j + 1] == '#')
		{
			return true;
		}
	}
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;
	for(int tc = 1; tc <= t; tc++)
	{
		cin >> m >> n;

		pic.assign(m, vector<char>(n));
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> pic[i][j];
			}
		}

		bool isPossible = true;
		for (int j = 0; j < n && isPossible; j++)
		{
			for (int i = 0; i < m && isPossible; i++)
			{
				if (pic[i][j] == '#')
				{
					if (isValid(i, j))
					{
						pic[i][j] = '/';
						pic[i + 1][j] = '\\';
						pic[i][j + 1] = '\\';
						pic[i + 1][j + 1] = '/';
					}
					else
					{
						isPossible = false;
					}
				}
			}
		}

		cout << "Case #" << tc << ": " << endl;
		if (!isPossible)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for (int i = 0; i < m; i++)
			{
				for (int j = 0; j < n; j++)
				{
					cout << pic[i][j];
				}
				cout << endl;
			}
		}
	
	}

	return 0;
}