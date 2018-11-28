#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <cmath>
#include <cassert>
using namespace std;

int r, c;

char matrix[50][50];

void solve ()
{
	cin >> r >> c;

	for (int i = 0; i < r; i += 1)
	{
		for (int j = 0; j < c; j += 1)
		{
			cin >> matrix[i][j];
		}
	}

	for (int i = 0; i < r-1; i += 1)
	{
		for (int j = 0; j < c-1; j += 1)
		{
			if (matrix[i][j] == '#')
			{
				if (matrix[i+1][j] == '#' && matrix[i+1][j+1] == '#' && matrix[i][j+1] == '#')
				{
					matrix[i][j] = '/';
					matrix[i][j+1] = '\\';
					matrix[i+1][j] = '\\';
					matrix[i+1][j+1] = '/';
				}
				else
				{
					cout << "Impossible" << endl;
					return;
				}
			}
		}
	}

	for (int i = 0; i < r; i += 1)
	{
		if (matrix[i][c-1] == '#')
		{
			cout << "Impossible" << endl;
			return;
		}
	}

	for (int i = 0; i < c; i += 1)
	{
		if (matrix[r-1][i] == '#')
		{
			cout << "Impossible" << endl;
			return;
		}
	}

	for (int i = 0; i < r; i += 1)
	{
		for (int j = 0; j < c; j += 1)
		{
			cout << matrix[i][j];
		}
		cout << endl;
	}
}

int main ()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i += 1)
	{
		cout << "Case #" << i+1 << ":" << endl;
		solve ();
	}
}

