#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

char bark[520][520];
int cut[520][520];

unsigned char chartoint(unsigned char ch)
{
	if (isdigit(ch))
		return ch - '0';

	return ch - 'A' + 10;
}

bool is_alternate(int x, int y, int z, int n, char white)
{
	int i = 0;
	char color = white;

	for (i = 0; y+i < n && i < z; i++)
	{
		if (bark[x][y+i] != color)
			return false;
		color = (color == 1 ? 0 : 1);
	}

	return (i == z);
}

bool can_cut(int x, int y, int z, int m, int n, char white)
{
	int i, j;
	char color = white;

	for (i = x, j = 0; i < m && j < z; i++, j++)
	{
		if (!is_alternate(i, y, z, n, color))
			return false;
		color = (color == 1 ? 0 : 1);
	}

	return (j == z);
}

int how_large(int x, int y, int m, int n)
{
	int i;

	for (i = 512; i; i--)
		if (can_cut(x, y, i, m, n, bark[x][y]))
			return i;

	return -1;
}

void cut_it(int x, int y, int z)
{
	int i, j, xx, yy;

	for (xx = x, i = 0; i < z; i++, xx++)
		for (yy = y, j = 0; j < z; j++, yy++)
			bark[xx][yy] = -1;
}

void update_cut(int m, int n)
{
	int j, k;

	for (j = 0; j < m; j++)
		for (k = 0; k < n; k++)
			cut[j][k] = how_large(j, k, m, n);
}

int main()
{
	int n, i, t, j, k, m, x, y, mx, my;
	unsigned char ch;
	map<int, int> mi;
	map<int, int>::reverse_iterator mi_rev;

	cin >> t;
	for (i = 0; i < t; i++)
	{
		memset(bark, 0, sizeof(bark));
		mi.clear();

		cin >> m >> n;
		for (j = 0; j < m; j++)
		{
			for (k = 0; k < n;)
			{
				cin >> ch;
				x = chartoint(ch);

				for (y = (1 << 3); y; y >>= 1)
				{
					if (x & y)
						bark[j][k] = 1;
					k++;
				}
			}
		}

		while(true)
		{
			update_cut(m, n);

			mx = my = -1;
			for (j = 0; j < m && mx == -1 && my == -1; j++)
				for (k = 0; k < n && mx == -1 && my == -1; k++)
					if (bark[j][k] >= 0)
					{
						mx = j;
						my = k;
					}

			if (mx == -1 && my == -1)
				break;

			for (j = 0; j < m; j++)
				for (k = 0; k < n; k++)
					if (cut[j][k] > cut[mx][my] && bark[j][k] >= 0)
					{
						mx = j;
						my = k;
					}

			if (cut[mx][my])
			{
				mi[cut[mx][my]]++;
				cut_it(mx, my, cut[mx][my]);
			}
		}

		cout << "Case #" << i+1 << ": " << mi.size() << endl;

		mi_rev = mi.rbegin();
		while(mi_rev != mi.rend())
		{
			cout << mi_rev->first << ' ' << mi_rev->second << endl;
			mi_rev++;
		}
	}

	return 0;
}
