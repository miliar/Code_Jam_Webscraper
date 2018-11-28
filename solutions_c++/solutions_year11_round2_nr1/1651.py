#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int t, i, j, k;
	int a[100][100];
	double b[100][3];
	int win, lose, op;
	double allwin;

	cin >> t;
	for (int ca = 1; ca <=t; ++ca)
	{
		int n;
		cin >> n;
		char c;
		for (i = 0; i < n; ++i)
		{
			win = 0;
			lose = 0;
			for (j = 0; j < n; ++j)
			{
				cin >> c;
				if (c == '.')
				{
					a[i][j] = -1;
				}
				else if (c == '1')
				{
					a[i][j] = 1;
					win++;
				}
				else
				{
					a[i][j] = 0;
					lose++;
				}
			}

			b[i][0] = (win + lose) == 0 ? 0 : win * 1.0 / (win + lose) * 1.0;
		}

		for (i = 0; i < n; ++i)
		{
			op = 0;
			allwin = 0;
			for (j = 0; j < n; ++j)
			{
				if (a[i][j] != -1)
				{
					op++;
					win = 0;
					lose = 0;
					for (k = 0; k < n; ++k)
					{
						if (k == i)
							continue;
						if (a[j][k] == 1)
							win++;
						else if (a[j][k] == 0)
							lose++;
					}
					allwin += (win + lose) == 0 ? 0 : win * 1.0 / (win + lose) * 1.0;
				}
			}
			b[i][1] = op == 0 ? 0 : allwin * 1.0 / op * 1.0;
		}

		for (i = 0; i < n; ++i)
		{
			op = 0;
			allwin = 0;
			for (j = 0; j < n; ++j)
			{
				if (a[i][j] != -1)
				{
					op++;
					allwin += b[j][1];
				}
			}
			b[i][2] = op == 0 ? 0 : allwin * 1.0 / op * 1.0;
		}

		cout << "Case #" << ca << ":" << endl;
		for (i = 0; i < n; ++i)
		{
			cout << b[i][0] / 4 + b[i][1] / 2 + b[i][2] / 4 << endl;
		}
	}

	return 0;
}