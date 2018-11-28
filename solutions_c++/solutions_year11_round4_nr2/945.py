#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>

#define maxN (1000 + 100)

using namespace std;

int r, c, d;
int a[maxN][maxN];

int solve ()
{
	cin >> r >> c >> d;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			char x; cin >> x;
			a[i][j] = x - '0';
		}

	int res = -1;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			int x = 0, y = 0;
			for (int l = 1, k = 3; (i - l) >= 0 && (j - l) >= 0 && (i + l) < r && (j + l) < c; l++, k += 2)
			{
				for (int jj = j - l + 1; jj <= j + l - 1; jj++)
					x += (j - jj) * (d + a[i - l][jj]),		y += l * (d + a[i - l][jj]);
				for (int jj = j - l + 1; jj <= j + l - 1; jj++)
					x += (j - jj) * (d + a[i + l][jj]),		y += -l * (d + a[i + l][jj]);
				for (int ii = i - l + 1; ii <= i + l - 1; ii++)
					y += (i - ii) * (d + a[ii][j - l]),		x += l * (d + a[ii][j - l]);
				for (int ii = i - l + 1; ii <= i + l - 1; ii++)
					y += (i - ii) * (d + a[ii][j + l]),		x += -l * (d + a[ii][j + l]);

				x += (l - 1) * (d + a[i - l + 1][j - l + 1]);	y += (l - 1) * (d + a[i - l + 1][j - l + 1]);
				x += -(l - 1) * (d + a[i - l + 1][j + l - 1]);	y += (l - 1) * (d + a[i - l + 1][j + l - 1]);
				x += -(l - 1) * (d + a[i + l - 1][j + l - 1]);	y += -(l - 1) * (d + a[i + l - 1][j + l - 1]);
				x += (l - 1) * (d + a[i + l - 1][j - l + 1]);	y += -(l - 1) * (d + a[i + l - 1][j - l + 1]);

				cerr << i << ' ' << j << ' ' << k << ' ' << l << ' ' << ' ' << x << ' ' << y << endl;

				if (x == 0 && y == 0)
					res = max (res, k);
			}
			
			x = 0; y = 0;

			for (int l = 2, k = 4; (i - l) >= 0 && (j - l) >= 0 && (i + l) <= r && (j + l) <= c; l++, k += 2)
			{
				for (int jj = j - l + 1; jj < j + l - 1; jj++)
					x += (2 * (j - jj) - 1) * (d + a[i - l][jj]),		y += (2 * l - 1) * (d + a[i - l][jj]);
				//cerr << x << ' ' << y << endl;
				for (int jj = j - l + 1; jj < j + l - 1; jj++)
					x += (2 * (j - jj) - 1) * (d + a[i + l - 1][jj]),	y += -(2 * l - 1) * (d + a[i + l - 1][jj]);
				//cerr << x << ' ' << y << endl;
				for (int ii = i - l + 1; ii < i + l - 1; ii++)
					y += (2 * (i - ii) - 1) * (d + a[ii][j - l]),		x += (2 * l - 1) * (d + a[ii][j - l]);
				//cerr << x << ' ' << y << endl;
				for (int ii = i - l + 1; ii < i + l - 1; ii++)
					y += (2 * (i - ii) - 1) * (d + a[ii][j + l - 1]),	x += -(2 * l - 1) * (d + a[ii][j + l - 1]);
				//cerr << x << ' ' << y << endl;

				x += (2 * l - 3) * (d + a[i - l + 1][j - l + 1]);	y += (2 * l - 3) * (d + a[i - l + 1][j - l + 1]);
				//cerr << x << ' ' << y << endl;
				x += -(2 * l - 3) * (d + a[i - l + 1][j + l - 2]);	y += (2 * l - 3) * (d + a[i - l + 1][j + l - 2]);
				//cerr << x << ' ' << y << endl;
				x += -(2 * l - 3) * (d + a[i + l - 2][j + l - 2]);	y += -(2 * l - 3) * (d + a[i + l - 2][j + l - 2]);
				//cerr << x << ' ' << y << endl;
				x += (2 * l - 3) * (d + a[i + l - 2][j - l + 1]);	y += -(2 * l - 3) * (d + a[i + l - 2][j - l + 1]);
				//cerr << x << ' ' << y << endl;

				//cerr << i << ' ' << j << ' ' << k << ' ' << l << ' ' << ' ' << x << ' ' << y << endl;

				if (x == 0 && y == 0)
					res = max (res, k);
			}
		}

	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int res = solve();
		if (res == -1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
