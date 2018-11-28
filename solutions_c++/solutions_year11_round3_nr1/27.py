#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>
#include <iomanip>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int row, column;
		cin >> row >> column;

		vector <string> table(row);
		getline(cin, table[0]);

		for (int i = 0; i < row; ++i)
			getline(cin, table[i]);

		bool res = true;

		for (int i = 0; i < row - 1; ++i)
		{
			for (int j = 0; j < column - 1; ++j)
			{
				if (table[i][j] == '#')
				{
					if (table[i][j + 1] != '#' || table[i + 1][j] != '#' || table[i + 1][j + 1] != '#')
						res = false;

					table[i][j] = '/';
					table[i][j + 1] = '\\';
					table[i + 1][j] = '\\';
					table[i + 1][j + 1] = '/';				
				}
			}
		}

		for (int i = 0; i < row; ++i)
			for (int j = 0; j < column; ++j)
				if (table[i][j] == '#')
					res = false;

		cout << "Case #" << test + 1 << ":" << endl;
		if (!res)
			cout << "Impossible" << endl;
		else
		{
			for (int i = 0; i < row; ++i)
				cout << table[i] << endl;
		}
	}

	return 0;
}