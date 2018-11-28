#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <climits>
#include <cmath>
#define maxN 1000

using namespace std;

int a[maxN][maxN];
int N;
int ci, cj;

inline bool
ok(int x, int y, int dx, int dy)
{
//	cout << " " << x << " " << y << " " << dx << " " << dy << endl;
	return dx < 0 || dx > N * 2 - 2 || dy < 0 || dy > N * 2 - 2 || a[dx][dy] < 0 || a[x][y] < 0 || a[dx][dy] == a[x][y];
}

int
main()
{
	int T, z;
	cin >> T;
	for (z = 1; z <= T; z++)
	{
		cin >> N;
		for (int i = 0; i < N * 2; i++)
			for (int j = 0; j < N * 2; j++)
				a[i][j] = -1;
		for (int i = 0; i < 2 * N - 1; i++)
		{
			int count = 0, start = 0;
			if (i < N)
			{
				count = i + 1;
				start = (N - 1) - i;
			}
			else
			{
				count = N - (i - (N - 1));
				start = i - (N - 1);
			}
			for (int j = 0; j < count ;j++)
			{
				cin >> a[i][start];
				start += 2;
			}
		}
/*		for (int i = 0; i < N * 2 - 1; i++)
		{
			for (int j = 0; j < N * 2 - 1; j++)
				if (a[i][j] < 0)
					cout << " ";
				else
					cout << a[i][j];
			cout << endl;
		}*/
		int minsize = INT_MAX;
		int ansx, ansy;
		for (int i = 0; i < N * 2 - 1; i++)
			for (int j = 0; j < N * 2 - 1; j++)
			{
				ci = i, cj = j;
				int s, d, gg, g;
				for (int x = 0; x < N * 2 - 1; x++)
					for (int y = 0; y < N * 2 - 1; y++)
						if (!ok(x, y, i * 2 - x, y) || !ok(x, y, x, j * 2 - y))
							goto failed;
				gg = max(abs(i - j), abs(i + j + 2 - N * 2));
				g = gg / 2 + N / 2;
				if (N % 2)
					if (gg % 2)
						s = 2 * (g + 1);
					else
						s = 2 * g + 1;
				else
					if (gg % 2)
						s = 2 * g+ 1;
					else
						s = 2 * g;
				if (s < minsize)
				{
					minsize = s;
					ansx = i;
					ansy = j;
				}
failed:;
			}
//		cout << ansx << " " << ansy << endl;
		cout << "Case #" << z << ": " << minsize * minsize - N * N << endl;
	}
	return 0;
}

