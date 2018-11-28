#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <cmath>
#include <cassert>
using namespace std;

int tc;
int n;

int matrix[100][100];
int wins[100][3];

double wp[100];
double owp[100];
double oowp[100];

int main ()
{
	cin >> tc;

	cout.setf (ios::fixed);
	cout.precision (9);

	for (int t = 0; t < tc; t += 1)
	{
		cin >> n;

		char c;

		for (int i = 0; i < n; i += 1)
		{
			wins[i][0] = 0;
			wins[i][1] = 0;
			wins[i][2] = 0;
			for (int j = 0; j < n; j += 1)
			{
				cin >> c;

				if (c == '1')
				{
					matrix[i][j] = 0;
				}
				else if (c == '0')
				{
					matrix[i][j] = 1;
				}
				else
				{
					matrix[i][j] = 2;
				}
				wins[i][matrix[i][j]] += 1;
			}
		}

		for (int i = 0; i < n; i += 1)
		{
			wp[i] = double(wins[i][0]) / (wins[i][0] + wins[i][1]);
		}

		for (int i = 0; i < n; i += 1)
		{
			int conta = 0;
			owp[i] = 0;

			for (int j = 0; j < n; j += 1)
			{
				if (matrix[i][j] < 2)
				{
					conta += 1;
					wins[j][matrix[j][i]] -= 1;
					owp[i] += double(wins[j][0]) / (wins[j][0] + wins[j][1]);
					wins[j][matrix[j][i]] += 1;
				}
			}

			owp[i] /= conta;
		}

		for (int i = 0; i < n; i += 1)
		{
			int conta = 0;
			oowp[i] = 0;

			for (int j = 0; j < n; j += 1)
			{
				if (matrix[i][j] < 2)
				{
					conta += 1;
					oowp[i] += owp[j];
				}
			}

			oowp[i] /= conta;
		}

		cout << "Case #" << t+1 << ":\n";

		for (int i = 0; i < n; i += 1)
		{
			cout << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << "\n";
		}
	}
}

