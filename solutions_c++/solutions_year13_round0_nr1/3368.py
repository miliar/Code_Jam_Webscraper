#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

int a[4][4];

string f()
{
	for (int i = 0; i < 4; i++)
	{
		int sum = 0;
		for (int j = 0; j < 4; j++)	sum += a[i][j];
		if (sum == 4 || sum == 103)		return "X won";
		if (sum == -4 || sum == 97)		return "O won";

		sum = 0;
		for (int j = 0; j < 4; j++)	sum += a[j][i];
		if (sum == 4 || sum == 103)		return "X won";
		if (sum == -4 || sum == 97)		return "O won";
	}

	int sum = a[0][0] + a[1][1] +  a[2][2] + a[3][3];
	if (sum == 4 || sum == 103)		return "X won";
	if (sum == -4 || sum == 97)		return "O won";

	sum = a[0][3] + a[1][2] +  a[2][1] + a[3][0];
	if (sum == 4 || sum == 103)		return "X won";
	if (sum == -4 || sum == 97)		return "O won";

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] == 0)
				return "Game has not completed";

	return "Draw";
}

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;		cin >> tc;
	for (int T = 1; T <= tc; T++)
	{
		string s;
		for (int i = 0; i < 4; i++)
		{
			cin >> s;
			for (int j = 0; j < 4; j++)
			{
				if (s[j] == 'X')	a[i][j] = 1;
				if (s[j] == 'O')	a[i][j] = -1;
				if (s[j] == 'T')	a[i][j] = 100;
				if (s[j] == '.')	a[i][j] = 0;
			}
		}
		
		cout << "Case #" << T << ": " << f() << endl;
	}
}