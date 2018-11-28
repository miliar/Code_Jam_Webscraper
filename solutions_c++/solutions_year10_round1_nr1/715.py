#include <cassert>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;


char a[128][128];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;

	for (int testi = 1; testi <= testn; ++testi)
	{
		int n, k;
		cin >> n >> k;

		for (int j = n - 1; j > -1; --j)
		{
			for (int i = 0; i < n; ++i)
			{
				cin >> a[i][j];
			}
		}

		for (int i = n - 2; i > -1; --i)
		{
			for (int j = 0; j < n; ++j)
			{
				int lastrow = n - 1;

				for (int t = i + 1; t < n; ++t)
				{
					if (a[t][j] != '.')
					{
						lastrow = t - 1;
						break;
					}
				}

				swap(a[lastrow][j], a[i][j]);
			}
		}

		int rwin = false, bwin = false;

		for (int i = 0; i < n; ++i)
		{
			int rcount = 0;
			int bcount = 0;

			int rvcount = 0;
			int bvcount = 0;

			for (int j = 0; j < n; ++j)
			{
				rcount = a[i][j] == 'R' ? rcount + 1 : 0;
				bcount = a[i][j] == 'B' ? bcount + 1 : 0;

				rvcount = a[j][i] == 'R' ? rvcount + 1 : 0;
				bvcount = a[j][i] == 'B' ? bvcount + 1 : 0;

				if (rcount >= k || rvcount >= k)
				{
					rwin = true;
				}

				if (bcount >= k || bvcount >= k)
				{
					bwin = true;
				}
			}

			rcount = 0;
			bcount = 0;

			rvcount = 0;
			bvcount = 0;

			for (int j = 0; i + j < n; ++j)
			{
				rcount = a[i + j][j] == 'R' ? rcount + 1 : 0;
				bcount = a[i + j][j] == 'B' ? bcount + 1 : 0;

				rvcount = a[j][i + j] == 'R' ? rvcount + 1 : 0;
				bvcount = a[j][i + j] == 'B' ? bvcount + 1 : 0;

				if (rcount >= k || rvcount >= k)
				{
					rwin = true;
				}

				if (bcount >= k || bvcount >= k)
				{
					bwin = true;
				}
			}

			rcount = 0;
			bcount = 0;

			for (int j = 0; i + j < n; ++j)
			{
				rcount = a[i + j][n - 1 - j] == 'R' ? rcount + 1 : 0;
				bcount = a[i + j][n - 1 - j] == 'B' ? bcount + 1 : 0;

				if (rcount >= k)
				{
					rwin = true;
				}

				if (bcount >= k)
				{
					bwin = true;
				}
			}

			rcount = 0;
			bcount = 0;

			for (int j = 0; i - j > -1; ++j)
			{
				rcount = a[i - j][j] == 'R' ? rcount + 1 : 0;
				bcount = a[i - j][j] == 'B' ? bcount + 1 : 0;

				if (rcount >= k)
				{
					rwin = true;
				}

				if (bcount >= k)
				{
					bwin = true;
				}
			}

			if (rwin && bwin)
			{
				break;
			}
		}

		cout << "Case #" << testi << ": ";

		if (rwin)
		{
			if (bwin)
			{
				cout << "Both";
			}
			else
			{
				cout << "Red";
			}
		}
		else
		{
			if (bwin)
			{
				cout << "Blue";
			}
			else
			{
				cout << "Neither";
			}
		}

		cout << endl;
	}

	return 0;
}