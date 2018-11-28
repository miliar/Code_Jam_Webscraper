#include <iostream>

using namespace std;

char a[4][4];

void solve()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] != 'X' && a[i][j] != 'T')
				break;
			else if (j == 3)
			{
				cout << "X won" << endl;
				return;
			}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[j][i] != 'X' && a[j][i] != 'T')
				break;
			else if (j == 3)
			{
				cout << "X won" << endl;
				return;
			}
	for (int i = 0; i < 4; i++)
		if (a[i][i] != 'X' && a[i][i] != 'T')
			break;
		else if (i == 3)
		{
			cout << "X won" << endl;
			return;
		}
	for (int i = 0; i < 4; i++)
		if (a[i][3 - i] != 'X' && a[i][3 - i] != 'T')
			break;
		else if (i == 3)
		{
			cout << "X won" << endl;
			return;
		}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] != 'O' && a[i][j] != 'T')
				break;
			else if (j == 3)
			{
				cout << "O won" << endl;
				return;
			}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[j][i] != 'O' && a[j][i] != 'T')
				break;
			else if (j == 3)
			{
				cout << "O won" << endl;
				return;
			}
	for (int i = 0; i < 4; i++)
		if (a[i][i] != 'O' && a[i][i] != 'T')
			break;
		else if (i == 3)
		{
			cout << "O won" << endl;
			return;
		}
	for (int i = 0; i < 4; i++)
		if (a[i][3 - i] != 'O' && a[i][3 - i] != 'T')
			break;
		else if (i == 3)
		{
			cout << "O won" << endl;
			return;
		}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] == '.')
			{
				cout << "Game has not completed" << endl;
				return;
			}
	cout << "Draw" << endl;
}

int main()
{
	int count;
	cin >> count;
	for (int i = 0; i < count; i++)
	{
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
				cin >> a[x][y];
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
