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
#include <cstring>
using namespace std;

int r, c, d;

int matrix[500][500];
int somme[500][500];

int rect (int ib, int ie, int jb, int je)
{
	int result = somme[ie-1][je-1];

	if (ib > 0)
	{
		result -= somme[ib-1][je-1];
	}
	if (jb > 0)
	{
		result -= somme[ie-1][jb-1];
	}
	if (ib > 0 && jb > 0)
	{
		result += somme[ib-1][jb-1];
	}

//	cout << "rect " << ib << " " << ie << " " << jb << " " << je << " = " << result << endl;

	return result;
}

bool check (int ib, int jb, int k)
{
//	cout << "check " << ib << " " << jb << " " << k << endl;
	double center;
	double somma;

	somma = 0;
	center = ib + double(k-1) / 2;

//	cout << "i " << center << endl;
	for (int i = ib; i < ib+k; i += 1)
	{
		if (i == ib || i == ib+k-1)
		{
			somma += rect (i, i+1, jb+1, jb+k-1) * (center - i);
		}
		else
		{
			somma += rect (i, i+1, jb, jb+k) * (center - i);
		}
	}

//	cout << somma << endl;
	if (fabs(somma) > 0.0000001)
	{
		return false;
	}

	somma = 0;
	center = jb + double(k-1) / 2;

//	cout << "j " << center << endl;
	for (int j = jb; j < jb+k; j += 1)
	{
		if (j == jb || j == jb+k-1)
		{
			somma += rect (ib+1, ib+k-1, j, j+1) * (center - j);
		}
		else
		{
			somma += rect (ib, ib+k, j, j+1) * (center - j);
		}
	}
//	cout << somma << endl;

	if (fabs(somma) > 0.0000001)
	{
		return false;
	}

	return true;
}

void solve ()
{
	cin >> r >> c >> d;

	char a;

	for (int i = 0; i < r; i += 1)
	{
		for (int j = 0; j < c; j += 1)
		{
			cin >> a;
			matrix[i][j] = a - '0';
		}
	}

	somme[0][0] = matrix[0][0];
	for (int j = 1; j < c; j += 1)
	{
		somme[0][j] = matrix[0][j] + somme[0][j-1];
	}

	for (int i = 1; i < r; i += 1)
	{
		somme[i][0] = matrix[i][0] + somme[i-1][0];
		for (int j = 1; j < c; j += 1)
		{
			somme[i][j] = matrix[i][j] + somme[i][j-1] + somme[i-1][j] - somme[i-1][j-1];
		}
	}

	int result = -1;

	for (int l = 3; l <= min (r, c); l += 1)
	{
		bool found = false;

		for (int i = 0; !found && i < r-l+1; i += 1)
		{
			for (int j = 0; !found && j < c-l+1; j += 1)
			{
				found = check (i, j, l);
			}
		}

		if (found)
			result = l;
	}

	if (result == -1)
	{
		cout << "IMPOSSIBLE" << endl;
	}
	else
	{
		cout << result << endl;
	}
}

int main ()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i += 1)
	{
		cout << "Case #" << i+1 << ": ";
		solve ();
	}
}

