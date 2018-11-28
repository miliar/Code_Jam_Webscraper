#include <iostream>
#include <cstdio>

using namespace std;

const double eps = 1e-9;

int n, m, d;
int a[20][20];

int GetInt()
{
	char c = '?';
	while (c < '0' || c > '9') cin >> c;
	return c - '0';
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int o;
	cin >> o;
	int I = 0;
	while (o--)
	{
		I++;
		cout << "Case #" << I << ": ";
		int max = 2;
		cin >> n >> m >> d;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				a[i][j] = GetInt();
			}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				for (int k = max + 1; k <= n; k++)
				if (k > max && i + k - 1< n && j + k - 1 < n)
				{
					double c = k / 2.0;
					double sx = 0;
					double sy = 0;
					for (int I = i; I < i + k; I++)
						for (int J = j; J < j + k; J++)
						if ((I != i || J != j)
						&& (I != i || J != j + k - 1)
						&& (I != i + k - 1 || J != j)
						&& (I != i + k - 1 || J != j + k - 1))
						{
							double cx = (I - i) + 0.5;
							double cy = (J - j) + 0.5;
							cx = c - cx;
							cy = c - cy;
							sx += cx * (d + a[I][J]);
							sy += cy * (d + a[I][J]);
						}
					if (sx > -eps && sx < eps && sy < eps && sy > -eps)
						max = k;
				}
		if (max > 2) cout << max;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}