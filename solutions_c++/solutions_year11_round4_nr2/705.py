#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int W[10][10];
int R, C, D;
bool check(int x, int y, int size)
{
	int X = 0, Y = 0;
	for (int i = 0; i < size; ++i)
	{
		for (int j = 0; j < size; ++j)
		{
			if (i == 0 || i == size - 1)
			{
				if (j == 0 || j == size - 1)
					continue;
			}
			if (size & 1)
			{
				X += W[x + i][y + j] * (i - size / 2);
				Y += W[x + i][y + j] * (j - size / 2);
			}
			else
			{
				if (i < size / 2)
				{
					X += W[x + i][y + j] * ((i - size / 2) * 2 + 1);
				}
				else
				{
					X += W[x + i][y + j] * ((i + 1 - size / 2) * 2 - 1);
				}
				if (j < size / 2)
				{
					Y += W[x + i][y + j] * ((j - size / 2) * 2 + 1);
				}
				else
				{
					Y += W[x + i][y + j] * ((j + 1 - size / 2) * 2 - 1);
				}
			}
		}
	}
	return X == 0 && Y == 0;
}
bool find(int size)
{
	for (int i = 0; i + size <= R; ++i)
	{
		for (int j = 0; j + size <= C; ++j)
		{
			if (check(i, j, size)) return true;
		}
	}
	return false;
}
void solve()
{
	
	scanf ("%d%d%d", &R, &C, &D);
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			char c;
			scanf ("\n%c", &c);
			W[i][j] = D + c - '0';
		}
	}
	for (int i = min(R, C); i >= 3; --i)
	{
		if (find(i))
		{
			printf ("%d\n", i);
			return;
		}
	}
	printf ("IMPOSSIBLE\n");
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}