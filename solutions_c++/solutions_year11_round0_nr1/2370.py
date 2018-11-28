#include <iostream>
#include <cstdio>

using namespace std;

int m;
char c[2000];
int r[2000];

int Get(char C, int z)
{
	while (z < m && c[z] != C) z++;
	if (z == m) return -1;
	else return z;
}

int modify(int x, int X)
{
	if (x < X) return x + 1;
	if (x > X) return x - 1;
	return x;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	int I = 0;
	while (n--)
	{
		I++;
		cout << "Case #" << I << ": ";
		cin >> m;
		for (int i = 0; i < m; i++)
		{
			cin >> c[i] >> r[i];
		}
		int x = 1;
		int y = 1;
		int i = 0;
		int nx = Get('B', 0);
		int ny = Get('O', 0);
		int k = 0;
		while (i < m)
		{
			k++;
			bool fx = true;
			bool fy = true;
			if (r[nx] != x) 
			{
				x = modify(x, r[nx]);
				fx = false;
			}
			if (r[ny] != y)
			{
				y = modify(y, r[ny]);
				fy = false;
			}
			if (nx == i && fx && r[nx] == x)
			{
				i++;
				fy = false;
				nx = Get('B', i);
			}
			if (ny == i && fy && r[ny] == y)
			{
				i++;
				ny = Get('O', i);
			}
		}
		cout << k << endl;
	}
	return 0;
}