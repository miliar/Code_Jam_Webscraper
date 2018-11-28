#include <iostream>
#include <string>
using namespace std;
int v[4][4];
bool result = false;
bool empty = false;

bool isComparable(int x, int y, int val)
{
	if ((val == 3) || val == 0 || v[x][y] == 0)
	{
		return false;
	}
	if ((v[x][y] == val) || (v[x][y] == 3))
	{
		return true;
	}
	return false;
}

bool arrIsOk(int x, int y, int val)
{
	int isOk = 0;
	if ((val == 0) || v[x][y] == 0)
	{
		return false;
	}

	for (int i = 0; i < 4; i++)
	{
		if ((v[x][i] == val) || (v[x][i] == 3))
		{
			isOk++;
		}
	}
	if (isOk == 4)
	{
		return true;
	}
	else
	{
		isOk = 0;
	}
	for (int i = 0; i < 4; i++)
	{
		if ((v[i][y] == val) || (v[i][y] == 3))
		{
			isOk++;
		}
	}
	if (isOk == 4)
	{
		return true;
	}
	
	return false;
}

void alg()
{
	for (int i = 0; i < 4; i++)
	{
		string s;
		/*getline(cin, s);*/
		cin >> s;
		for (int j = 0; j < 4; j++)
		{
			switch (s[j])
			{
			case 'X':
				v[i][j] = 'X';
				break;
			case 'O':
				v[i][j] = 'O';
				break;
			case '.':
				v[i][j] = 0;
				empty = true;
				break;
			case 'T':
				v[i][j] = 3;
				break;
			default:
				break;
			}
		}
	}
	if (v[0][0] != 3)
	{
		if (isComparable(1,1,v[0][0]) && isComparable(2,2,v[0][0]) && isComparable(3,3,v[0][0]))
		{
			if (v[0][0] == 'X')
			{
				cout << "X won\n";
				result = true;
				return;
			}
			else
			{
				cout << "O won\n";
				result = true;
				return;
			}
		}
	}
	else
	{
		if (isComparable(0,0,v[1][1]) && isComparable(2,2,v[0][0]) && isComparable(3,3,v[0][0]))
		{
			if (v[1][1] == 'X')
			{
				cout << "X won\n";
				result = true;
				return;
			}
			else
			{
				cout << "O won\n";
				result = true;
				return;
			}
		}
	}
	if (v[0][3] != 3)
	{
		if (isComparable(1,2,v[0][3]) && isComparable(2,1,v[0][3]) && isComparable(3,0,v[0][3]))
		{
			if (v[0][3] == 'X')
			{
				cout << "X won\n";
				result = true;
				return;
			}
			else
			{
				cout << "O won\n";
				result = true;
				return;
			}
		}
	}
	else
	{
		if (isComparable(0,3,v[2][1]) && isComparable(1,2,v[2][1]) && isComparable(3,0,v[2][1]))
		{
			if (v[2][1] == 'X')
			{
				cout << "X won\n";
				result = true;
				return;
			}
			else
			{
				cout << "O won\n";
				result = true;
				return;
			}
		}
	}
	
	for (int i = 0; i < 4; i++)
	{
		if (arrIsOk(i, 0, 'X') || arrIsOk(0, i, 'X'))
		{
			cout << "X won\n";
			result = true;
			return;
		}
		if (arrIsOk(i, 0, 'O') || arrIsOk(0, i, 'O'))
		{
			cout << "O won\n";
			result = true;
			return;
		}
	}
}

int main()
{
	int d;
	cin >> d;
	for (int case_no = 1; case_no <= d; ++case_no) {
		cout << "Case #" << case_no << ": ";
		alg();
		if (!result)
		{
			if (!empty)
			{
				cout << "Draw\n";
			}
			else
			{
				cout << "Game has not completed\n";
			}
		}
		result = false;
		empty = false;
	}
	return 0;
}