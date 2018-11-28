#include <iostream>
#include <string.h>
#include <stdio.h>
#define MIN(a, b)    ((a) < (b) ? (a) : (b))
#define MAX(a, b)    ((a) > (b) ? (a) : (b))
using namespace std;

int r, c, d;
int mp[1000][1000];
double h, w;

void Update(int i, int j, int ii, int jj, int k, int md)
{
	if (k % 2 == 1)
	{
		if (md == 0)
		{
			h += (ii - k / 2) * mp[i + ii][j + jj];
			w += (jj - k / 2) * mp[i + ii][j + jj];
		}
		else
		{
			h -= (ii - k / 2) * mp[i + ii][j + jj];
			w -= (jj - k / 2) * mp[i + ii][j + jj];
		}
	}
	else
	{
		if (md == 0)
		{
			h += ((double)(ii - k / 2) + 0.5) * mp[i + ii][j + jj];
			w += ((double)(jj - k / 2) + 0.5) * mp[i + ii][j + jj];
		}
		else
		{
			h -= ((double)(ii - k / 2) + 0.5) * mp[i + ii][j + jj];
			w -= ((double)(jj - k / 2) + 0.5) * mp[i + ii][j + jj];
		}
	}
}


void Solve()
{
	int i, j, k, res = 0;
	int ii, jj;
	char str[1000];
	scanf("%d%d%d", &r, &c, &d);
	for (i = 0; i < r; i++)
	{
		scanf("%s", str);
		for (j = 0; j < c; j++)
			mp[i][j] = str[j] - '0' + d;
	}
	for (i = 0; i + 3 <= r; i++)
		for (j = 0; j + 3 <= c; j++)
			for (k = MIN(r - i, c - j); k >= 3; k--)
			{
				h = w = 0;
				for (ii = 0; ii < k; ii++)
					for (jj = 0; jj < k; jj++)
						Update(i, j, ii, jj, k, 0);
				Update(i, j, 0, 0, k, 1);
				Update(i, j, 0, k - 1, k, 1);
				Update(i, j, k - 1, 0, k, 1);
				Update(i, j, k - 1, k - 1, k, 1);
				if (h == 0 && w == 0)
					res = MAX(k, res);
			}
	if (res == 0)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", res);
}

int main()
{
	int t, f;
	freopen("b-small-attempt1.in", "r", stdin);
	freopen("b-small-attempt1.out", "w", stdout);
	cin >> t;
	for (f = 1; f <= t; f++)
	{
		printf("Case #%d: ", f);
		Solve();
	}
	return 0;
}

