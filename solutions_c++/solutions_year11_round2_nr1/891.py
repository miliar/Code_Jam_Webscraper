#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

char grid[100][100];
double wp[100], owp[100], oowp[100];
int n;

int main()
{
	int ncases;

	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			int w = 0, l = 0;
			for (int j = 0; j < n; j++)
			{
				cin >> grid[i][j];
				if (grid[i][j] == '1')
					w++;
				else if (grid[i][j] == '0')
					l++;
			}
			wp[i] = (double)w / (double)(w + l);
			//cout << i << " " << wp[i] << endl;
		}

		int op;
		fill(owp, owp + 100, 0.0);
		for (int i = 0; i < n; i++)
		{
			op = 0;
			for (int j = 0; j < n; j++)
			{
				int w = 0, l = 0;
				if (grid[i][j] != '.')
					for (int k = 0; k < n; k++)
						if (k != i)
						{
							if (grid[j][k] == '1')
								w++;
							else if (grid[j][k] == '0')
								l++;
						}
				if (w + l > 0)
				{
					owp[i] += (double)(w) / (double)(w + l);
					op++;
				}
			}
			owp[i] /= op;
			//cout << i << " " << owp[i] << endl;
		}

		int oowpc;
		fill(oowp, oowp + 100, 0.0);
		for (int i = 0; i < n; i++)
		{
			oowpc = 0;
			for (int j = 0; j < n; j++)
			{
				if (grid[i][j] != '.')
				{
					oowpc++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= oowpc;
			//cout << i << " " << oowp[i] << endl;
		}

		printf("Case #%i:\n", caseno);
		for (int i = 0; i < n; i++)
			printf("%.6f\n", (.25 * wp[i] + .50 * owp[i] + .25 * oowp[i]));
	}
}
