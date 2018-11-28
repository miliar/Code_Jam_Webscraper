#include <iostream>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int ti = 0; ti < t; ++ti)
	{
		cout << "Case #" << (ti + 1) << ": ";
		char a[4][4];
		char w;
		bool dotsfound = false;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				cin >> a[i][j];
				if (a[i][j] == '.')
					dotsfound = true;
			}
			// 10 lines to check
			// 4 horizontals
			bool found = false;
			int x, o;
			bool icontinue = true;
			for (int i = 0; i < 4 && icontinue; ++i)
			{
				x = 0; o = 0;
				for (int j = 0; j < 4; ++j)
				{
					if (a[i][j] == 'X')
						x++;
					if (a[i][j] == 'O')
						o++;
					if (a[i][j] == 'T')
					{ x++; o++; }
					if (x == 4)
					{
						cout << "X won";
						icontinue = false;
						found = true;
						break;
					}
					if (o == 4)
					{
						cout << "O won";
						icontinue = false;
						found = true;
						break;
					}
				}
			}
			// 4 verticals
			icontinue = true;
			for (int i = 0; !found && i < 4 && icontinue; ++i)
			{
				x = 0; o = 0;
				for (int j = 0; j < 4; ++j)
				{
					if (a[j][i] == 'X')
						x++;
					if (a[j][i] == 'O')
						o++;
					if (a[j][i] == 'T')
					{ x++; o++; }
					if (x == 4)
					{
						cout << "X won";
						icontinue = false;
						found = true;
						break;
					}
					if (o == 4)
					{
						cout << "O won";
						icontinue = false;
						found = true;
						break;
					}
				}
			}

			// main diagonal
			x = 0; o = 0;
			for (int i = 0; i < 4; ++i)
			{
				if (a[i][i] == 'X')
					x++;
				if (a[i][i] == 'O')
					o++;
				if (a[i][i] == 'T')
				{ x++; o++; }
				if (x == 4)
				{
					cout << "X won";
					found = true;
					break;
				}
				if (o == 4)
				{
					cout << "O won";
					found = true;
					break;
				}
			}

			x = 0; o = 0;
			// secondary diagonal
			for (int i = 0; i < 4; ++i)
			{
				if (a[i][3-i] == 'X')
					x++;
				if (a[i][3-i] == 'O')
					o++;
				if (a[i][3-i] == 'T')
				{ x++; o++; }
				if (x == 4)
				{
					cout << "X won";
					found = true;
					break;
				}
				if (o == 4)
				{
					cout << "O won";
					found = true;
					break;
				}
			}

			if (!found)
			{
				if (dotsfound)
					cout << "Game has not completed";
				else 
					cout << "Draw";
			}
			cout << endl;
	}
	return 0;
}