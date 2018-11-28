# include <iostream>
# include <stdio.h>
# include <string>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int r, c;
		cin >> r >> c;
		string a[51];
		for (int i = 0; i < r; ++i)
			cin >> a[i];

		cout << "Case #" << test << ": " << endl;

		bool possible = true;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (a[i][j] == '#')
				{
					if (i == r - 1 || j == c - 1 || a[i + 1][j] != '#' || 
						a[i][j + 1] != '#' || a[i + 1][j + 1] != '#')
					{
						possible = false;
					}
					else
					{
						a[i][j] = '/';
						a[i][j + 1] = '\\';
						a[i + 1][j] = '\\';
						a[i + 1][j + 1] = '/';
					}
				}
		if (possible)
		{
			for (int i = 0; i < r; ++i)
				cout << a[i] << endl;
		}
		else
		{
			cout << "Impossible" << endl;
		}		
	}

	return 0;
}