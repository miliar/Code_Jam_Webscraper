#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

char mas[4][4];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int t;
	cin >> t;
	for (int d = 1; d <= t; d++)
	{
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> mas[i][j];
			}
		}

		int to = 0, tx = 0, w = 0, win = 0, ansx = 0, anso = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				to += mas[i][j] == 'O' || mas[i][j] == 'T';
				tx += mas[i][j] == 'X' || mas[i][j] == 'T';
				w = mas[i][j] == '.';
			}
			ansx += tx == 4; tx = 0;
			anso += to == 4; to = 0;
		}

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				to += mas[j][i] == 'O' || mas[j][i] == 'T';
				tx += mas[j][i] == 'X' || mas[j][i] == 'T';
				w = mas[j][i] == '.';
			}
			ansx += tx == 4; tx = 0;
			anso += to == 4; to = 0;
		}

		for (int i = 0; i < 4; i++)
		{
			to += mas[i][i] == 'O' || mas[i][i] == 'T';
			tx += mas[i][i] == 'X' || mas[i][i] == 'T';
			w = mas[i][i] == '.';
		}
		ansx += tx == 4; tx = 0;
		anso += to == 4; to = 0;

		for (int i = 0; i < 4; i++)
		{
			to += mas[i][3 - i] == 'O' || mas[i][3 - i] == 'T';
			tx += mas[i][3 - i] == 'X' || mas[i][3 - i] == 'T';
			w = mas[i][3 - i] == '.';
		}
		ansx += tx == 4; tx = 0;
		anso += to == 4; to = 0;

		printf("Case #%d: ", d);
		if (ansx) cout << "X won" << endl;
		else if (anso) cout << "O won" << endl;
		else if (w) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}
	
	
	return 0;
}