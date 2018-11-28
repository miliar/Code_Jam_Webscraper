#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

#define cin fin
#define cout fout

int f[501][501];
int c[501][501];

int ans[501];

int main()
{
	memset(c, 0, sizeof(0));

	c[0][0] = 1;
	c[1][0] = 1;
	c[1][1] = 1;
	for (int i = 2; i < 501; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			c[i][j] = c[i-1][j];
			if (j-1 >= 0)
				c[i][j] += c[i-1][j-1];

			c[i][j] %= 100003;
		}
	}

	memset(f, 0, sizeof(f));

	f[2][0] = 0;
	f[2][1] = 1;

	for (int i = 3; i < 501; i++)
	{
		f[i][1] = 1;

		for (int k = 2; k <= i-1; k++)
		{
			f[i][k] = 0;

			for (int x = 0; x <= i - k - 1 && k - 1 - x >= 0; x++)
			{
				int y = k - 1 - x;
				f[i][k] = (f[i][k] + c[i-k-1][x] * f[k][y]) % 100003;
			}			
		}		
	}

	for (int i = 2; i < 501; i++)
	{
		ans[i] = 0;
		for (int j = 1; j <= i-1; j++)
		{
			ans[i] += f[i][j];
			ans[i] %= 100003;
		}
	}

	int testcases, n;

	cin >> testcases;
	for (int i = 0; i < testcases; i++)
	{
		cin >> n;
		cout << "Case #" << i+1 << ": " << ans[n] << endl;
	}

	return 0;
}