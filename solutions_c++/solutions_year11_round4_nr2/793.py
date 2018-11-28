#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;

int r, c, d;
int w[500][500];

pair<double, double> calc(int i, int j, int k, double x, double y)
{
	pair<double, double> result = make_pair<double>(0, 0);
	for (int ii = i; ii < i + k; ++ii)
		for (int jj = j; jj < j + k; ++jj)
		{
			if (ii == i && jj == j)	continue;
			if (ii == i && jj == j + k - 1)	continue;
			if (ii == i + k - 1 && jj == j)	continue;
			if (ii == i + k - 1 && jj == j + k - 1)	continue;
			result.first += ((ii + 0.5) - x) * (w[ii][jj] + d);
			result.second += ((c - jj - 0.5) - y) * (w[ii][jj] + d);
		}
	return result;
}

double abs(double x)
{
	return x > 0 ? x : -x;
}

int cmp(double a, double b)
{
	if (abs(a - b) < 1e-6)
		return 0;
	else if (a < b)
		return -1;
	else
		return 1;
}

void solve()
{
	cin >> r >> c >> d;
	for (int i = 0; i < r; ++i)
	{
		string s;
		cin >> s;
		for (int j = 0; j < c; ++j)
			w[i][j] = s[j] - '0';
	}

	int ans = 0;
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			for (int k = 3; k <= min(r, c); ++k)
			{
				if (i + k > r)	continue;
				if (j + k > c)	continue;
				pair<double, double> cc = calc(i, j, k, i + k * 0.5, c - j - k * 0.5);
				if (cmp(cc.first, 0) == 0 && cmp(cc.second, 0) == 0)
				{
					if (k > ans)	ans = k;
				}
				/*
				double x = i + k * 0.5, y = j + k * 0.5;
				double delta = k;
				while (delta > 1e-6)
				{
					pair<double, double> xx = calc(i, j, k, x, y);
					cerr << "x = " << x << " y = " << y << " c = " << xx.first << ", " << xx.second << endl;
					bool changed = false;
					if (xx.first < 0)
					{
						pair<double, double> oo = calc(i, j, k, x + delta, y);
						if (oo.first > xx.first && abs(oo.first) < abs(xx.first))
						{
							x += delta;
							changed = true;
						}
						oo = calc(i, j, k, x - delta, y);
						if (oo.first > xx.first && abs(oo.first) < abs(xx.first))
						{
							x -= delta;
							changed = true;
						}
					}
					if (xx.first > 0)
					{
						pair<double, double> oo = calc(i, j, k, x + delta, y);
						if (oo.first < xx.first && abs(oo.first) < abs(xx.first))
						{
							x += delta;
							changed = true;
						}
						oo = calc(i, j, k, x - delta, y);
						if (oo.first < xx.first && abs(oo.first) < abs(xx.first))
						{
							x -= delta;
							changed = true;
						}
					}
					if (xx.second < 0)
					{
						pair<double, double> oo = calc(i, j, k, x, y + delta);
						if (oo.second > xx.second && abs(oo.second) < abs(xx.second))
						{
							y += delta;
							changed = true;
						}
						oo = calc(i, j, k, x, y - delta);
						if (oo.second > xx.second && abs(oo.second) < abs(xx.second))
						{
							y -= delta;
							changed = true;
						}
					}
					if (xx.second > 0)
					{
						pair<double, double> oo = calc(i, j, k, x, y + delta);
						if (oo.second < xx.second && abs(oo.second) < abs(xx.second))
						{
							y += delta;
							changed = true;
						}
						oo = calc(i, j, k, x, y - delta);
						if (oo.second < xx.second && abs(oo.second) < abs(xx.second))
						{
							y -= delta;
							changed = true;
						}
					}
					if (!changed)	delta *= 0.5;
				}
				*/
			}
	if (ans < 3)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

