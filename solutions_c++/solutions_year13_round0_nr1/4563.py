#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int n;
	cin >> n;
	for (int k=1; k<=n; k++)
	{
		int mas[4][4] = {0};
		int count = 0;
		for (int i=0; i<4; i++)
		{
			string s;
			cin >> s;
			for (int j=0; j<4; j++)
			{
				if (s[j] == 'O')
					mas[i][j] = 1;
				if (s[j] == 'X')
					mas[i][j] = 2;
				if (s[j] == 'T')
					mas[i][j] = 3;
				if (mas[i][j] > 0)
					count++;
			}
		}
		int res = 0; 
		for (int i=0; i<4; i++)
		{
			int x = 0;
			for (int j=0; j<4; j++)
				x += mas[i][j] > 1;
			if (x == 4)
				res = 2;
			x = 0;
			for (int j=0; j<4; j++)
				x += mas[i][j] & 1;
			if (x == 4)
				res = 1;
			x = 0;
			for (int j=0; j<4; j++)
				x += mas[j][i] > 1;
			if (x == 4)
				res = 2;
			x = 0;
			for (int j=0; j<4; j++)
				x += mas[j][i] & 1;
			if (x == 4)
				res = 1;
		}
		int x = 0, x2 = 0;
		for (int i=0; i<4; i++)
		{
			x += mas[i][i] > 1;
			x2 += mas[i][3-i] > 1;
		}
		if (x == 4 || x2 == 4)
			res = 2;
		x = 0, x2 = 0;
		for (int i=0; i<4; i++)
		{
			x += mas[i][i] & 1;
			x2 += mas[i][3-i] & 1;
		}
		if (x == 4 || x2 == 4)
			res = 1;
		if (res == 2)
			cout << "Case #" << k << ": " << "X won" << endl;
		if (res == 1)
			cout << "Case #" << k << ": " << "O won" << endl;
		if (res == 0)
			if (count == 16)
				cout << "Case #" << k << ": " << "Draw" << endl;
			else
				cout << "Case #" << k << ": " << "Game has not completed" << endl;

	}
	return 0;
}