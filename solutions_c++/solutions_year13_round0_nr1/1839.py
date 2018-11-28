#include <iostream>

using namespace std;

char a[4][4];
int c[4];
int t, cnt;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int k = 0; k < t; k++)
	{
		cnt = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> a[i][j];
				if (a[i][j] != '.')
				{
					cnt++;
				}
			}
		}		

		int f = 0;

		for (int i = 0; i < 4 && f == 0; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				c[j] = 0;
			}
			for (int j = 0; j < 4; j++)
			{
				switch (a[i][j])
				{
				case 'X':
					c[0]++;
					break;
				case 'O':
					c[1]++;
					break;
				case 'T':
					c[2]++;
					break;
				default:
					break;
				}
			}

			if (c[0] + c[2] == 4)
			{
				f = 1;
			}
			else
			{
				if (c[1] + c[2] == 4)
				{
					f = 2;
				}
			}			
		}

		for (int i = 0; i < 4 && f == 0; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				c[j] = 0;
			}
			for (int j = 0; j < 4; j++)
			{
				switch (a[j][i])
				{
				case 'X':
					c[0]++;
					break;
				case 'O':
					c[1]++;
					break;
				case 'T':
					c[2]++;
					break;
				default:
					break;
				}
			}

			if (c[0] + c[2] == 4)
			{
				f = 1;
			}
			else
			{
				if (c[1] + c[2] == 4)
				{
					f = 2;
				}
			}		
		}

		if (f == 0)
		{
			for (int i = 0; i < 4; i++)
			{
				c[i] = 0;
			}
			for (int i = 0; i < 4; i++)
			{
				switch (a[i][i])
				{
				case 'X':
					c[0]++;
					break;
				case 'O':
					c[1]++;
					break;
				case 'T':
					c[2]++;
					break;
				default:
					break;
				}
			}
			if (c[0] + c[2] == 4)
			{
				f = 1;
			}
			else
			{
				if (c[1] + c[2] == 4)
				{
					f = 2;
				}
			}
		}

		if (f == 0)
		{
			for (int i = 0; i < 4; i++)
			{
				c[i] = 0;
			}
			for (int i = 0; i < 4; i++)
			{
				switch (a[i][3 - i])
				{
				case 'X':
					c[0]++;
					break;
				case 'O':
					c[1]++;
					break;
				case 'T':
					c[2]++;
					break;
				default:
					break;
				}
			}
			if (c[0] + c[2] == 4)
			{
				f = 1;
			}
			else
			{
				if (c[1] + c[2] == 4)
				{
					f = 2;
				}
			}
		}

		cout << "Case #" << k + 1 << ": ";
		if (f == 1)
		{
			cout << "X won" << endl;
		}
		else
		{
			if (f == 2)
			{
				cout << "O won" << endl;
			}
			else
			{
				if (cnt == 16)
				{
					cout << "Draw" << endl;
				}
				else
				{
					cout << "Game has not completed" << endl;
				}
			}
		}
	}
	return 0;
}