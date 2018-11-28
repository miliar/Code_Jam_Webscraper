#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("A-large.out","w",stdout);

	int t, r, c;
	char a[52][52];
	int i, j;
	bool fail;
	cin >> t;
	for (int ca = 1; ca <= t; ++ca)
	{
		fail = false;
		cin >> r >> c;
		for (i = 1; i <= r; ++i)
		{
			for (j = 1; j <= c; ++j)
			{
				cin >> a[i][j];
			}
		}

		for (i = 0; i <= r; ++i)
		{
			a[i][0] = '.';
			a[i][c+1] = '.';
		}

		for (j = 0; j <= c; ++j)
		{
			a[0][j] = '.';
			a[r+1][j] = '.';
		}

		for (i = 1; i <= r; ++i)
		{
			for (j = 1; j <= c; ++j)
			{
				if (a[i][j] == '#')
				{
					if (a[i][j + 1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
					{
						a[i][j] = '/';
						a[i+1][j+1] = '/';
						a[i][j+1] = '\\';
						a[i+1][j] = '\\';
					}
					else
					{
						fail = true;
						break;
					}
				}
			}
			if (fail == true)
				break;
		}
		cout << "Case #" << ca << ":" << endl;
		if (fail == true)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for (i = 1; i <= r; ++i)
			{
				for (j = 1; j <= c; ++j)
				{
					cout << a[i][j];
				}
				cout << endl;
			}
		}
	}
	return 0;
}