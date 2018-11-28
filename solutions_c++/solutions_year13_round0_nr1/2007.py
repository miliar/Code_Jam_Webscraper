#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

bool checkwin(vector<string> field, char c)
{
	bool f1 = true, f2 = true;
	for (int i = 0; i < 4; ++i)
	{
		f1 = f1 && ((field[i][i] == c) || (field[i][i] == 'T'));
		f2 = f2 && ((field[i][3 - i] == c) || (field[i][3 - i] == 'T'));
	}
	if (f1 || f2)
	{
		return true;
	}
	for (int i = 0; i < 4; ++i)
	{
		f1 = true;
		f2 = true;
		for (int j = 0; j < 4; ++j)
		{
			f1 = f1 && ((field[i][j] == c) || (field[i][j] == 'T'));
			f2 = f2 && ((field[j][i] == c) || (field[j][i] == 'T'));
		}
		if (f1 || f2)
		{
			return true;
		}
	}
	return false;
}

bool checkend(vector<string> field)
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (field[i][j] == '.')
			{
				return false;
			}
		}
	}
	return true;
}

string solve(vector<string> field)
{
	if (checkwin(field, 'X'))
	{
		return "X won";
	}
	if (checkwin(field, 'O'))
	{
		return "O won";
	}
	if (checkend(field))
	{
		return "Draw";
	}
	return "Game has not completed";
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		vector<string> field(4);
		for (int j = 0; j < 4; ++j)
		{
			cin >> field[j];
		}
		cout << "Case #" << i + 1 << ": " << solve(field) << endl;
	}
	return 0;
}