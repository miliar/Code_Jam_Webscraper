#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int casen = 1; casen <= cases; casen++)
	{
		cout << "Case #" << casen << ":" << endl;
		int n, m;
		cin >> n >> m;
		vector< vector <char> > a(n);
		int bcount = 0;
		for (int i = 0; i < n; ++i)
		{
			a[i].resize(m);
			for (int j = 0; j < m; ++j)
			{
				cin >> a[i][j];
				if (a[i][j] == '#')
					bcount++;
			}
		}
		if (bcount % 4 != 0)
		{
			cout << "Impossible" << endl;
			continue;
		}
		bool ffail = false;
		for (int i = 0; i < n-1; ++i)
		{
			bool fail = false;
			for (int j = 0; j < m-1; ++j)
			{
				if (a[i][j] == '#')
				{
					if (a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#')
					{
						a[i][j] = '/';
						a[i+1][j] = '\\';
						a[i][j+1] = '\\';
						a[i+1][j+1] = '/';
					}
					else
					{
						cout << "Impossible" << endl;
						fail = true;
						break;
					}
				}

			}	
			if (fail)
			{
				ffail = true;
				break;
			}	
		}
		if (ffail)
			continue;
		else
		{
			for (int i = 0; i < n; ++i)
			{
				for (int j = 0; j < m; ++j)
				{
					cout << a[i][j];
				}
				cout << endl;
			}
		}
	}
}