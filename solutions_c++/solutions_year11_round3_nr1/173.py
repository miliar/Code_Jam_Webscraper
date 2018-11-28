#include <iostream>
#include <string>

using namespace std;

int n,m,t;

string s;

int mas[53][53];

int main()
{
	freopen("A32.in", "rt", stdin);
	freopen("A32.out", "wt", stdout);

	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		bool lab = 1;
		cin >> n >> m;

		for (int j = 0; j < n; j++)
		{
			cin >> s;

			for (int k = 0; k < m; k++)
			{
				if (s[k] == '#')
				{
					mas[j][k] = 1;
				}
				else
				{
					mas[j][k] = 0;
				}
			}
		}

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < m; k++)
			{
				if (mas[j][k] == 1)
				{
					if ((j < n-1) && (k < m-1) && (mas[j+1][k] == 1) && (mas[j][k+1] == 1) && (mas[j+1][k+1] == 1))
					{
						mas[j][k] = -1;
						mas[j+1][k] = -2;
						mas[j][k+1] = -2;
						mas[j+1][k+1] = -1;
					}
					else
					{
						lab = 0;
					}
				}
			}
		}

		cout << "Case #" << i << ":" << endl;

		if (lab == 0)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for (int j = 0; j < n; j++)
			{
				for (int k = 0; k < m; k++)
				{
					if (mas[j][k] == 0)
					{
						cout << ".";
					}
					else if (mas[j][k] == -1)
					{
						cout << "/";
					}
					else
					{
						cout << "\\";
					}
				}

				cout << endl;
			}
		}

	}

	return 0;
}