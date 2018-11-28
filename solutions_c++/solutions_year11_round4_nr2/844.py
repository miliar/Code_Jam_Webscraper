#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++)
	{
		char s;
		int R, C, D;
		cin >> R >> C >> D;

		vector<vector<int> > a(R, vector<int>(C));
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cin >> s;
				a[i][j] = D + (s - '0');
			}
		}

		double c;
		int x, y;
		bool gotcha = false;
		for (int k = min(R, C); k >= 3 && !gotcha; k--)
		{
			c = (k + .0) / 2;
			for (int i = 0; i <= R - k && !gotcha; i++)
			{
				for (int j = 0; j <= C - k && !gotcha; j++)
				{
					double x_res = 0, y_res = 0;
					for (int m = 0; m < k; m++)
					{
						for (int n = 0; n < k; n++)
						{
							if (!((m == 0 && n == 0) || (m == 0 && n == k - 1) || (m == k - 1 && n ==0) || (m == k -1 && n == k -1)))
							{
								x = i + m;
								y = j + n;
								x_res += (k - m - 0.5 - c) * a[x][y];
								y_res += (k - n - 0.5 - c) * a[x][y];
							}
 						}
					}

					if (x_res == 0 && y_res == 0)
					{
						cout << "Case #" << tc << ": " << k << endl;
						gotcha = true;
					}
				}
			}
		}

		if (!gotcha)
		{
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}