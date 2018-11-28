#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int a[100][100];
int n, m, d;
int res;
double c_n = 0.0, c_m = 0.0;


double mass_n(int i, int j)
{
	return (i+0.5-c_n)*a[i][j];
}

double mass_m(int i, int j)
{
	return (j+0.5-c_m)*a[i][j];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TEST_NUMBER;
	cin >> TEST_NUMBER;

	for (int TEST = 1; TEST <= TEST_NUMBER; TEST++)
	{
		cin >> n >> m >> d;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				char c;
				cin >> c;
				a[i][j] = c-'0'+d;
			}

		res = 0;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				for (int k = 3; k <= 11; k++)
				{
					if (i+k-1 >= n || j+k-1 >= m)
						continue;

					double m_n, m_m;
					m_n = 0;
					m_m = 0;
					double mm = 0;

					for (int t = 1; t < k-1; t++)
					{
						mm += a[i][j+t];
						m_n += mass_n(i, j+t);
						m_m += mass_m(i, j+t);
					}
					for (int t = 1; t < k-1; t++)
						for (int r = 0; r < k; r++)
						{
							mm += a[i+t][j+r];
							m_n += mass_n(i+t, j+r);
							m_m += mass_m(i+t, j+r);
						}
					for (int t = 1; t < k-1; t++)
					{
						mm += a[i+k-1][j+t];
						m_n += mass_n(i+k-1, j+t);
						m_m += mass_m(i+k-1, j+t);
					}

					m_n /= mm;
					m_m /= mm;

					if (abs(m_n-((double)i+(double)k/2.0)) + abs(m_m-((double)j+(double)k/2.0)) < 1e-8)
						res = max(res, k);
				}

				
		cout << "Case #" << TEST << ": ";
		if (res > 0)
			cout << res;
		else
			cout << "IMPOSSIBLE";

		cout << endl;
	}

	return 0;
}