#if 1
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
using namespace std;
int table[501][501]; //table[i][j] number i palce rank j
int C(int n, int k)
{
	if (n < 2 * k) k = n - k;
	int sol = 1;
	for (int i = n; i > n - k; i--)
		sol *= i;
	for (int i = 1; i <= k; i++)
		sol /= i;
	return sol;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++)
	{
		int n;
		scanf("%d", &n);
		memset(table, 0, sizeof(table));
		for (int i = 2; i <= n; i++) table[i][1] = 1;
		for (int i = 3; i <= n; i++)
			for (int j = 2; j < i; j++)
			{
				if (i == 5 && j == 4)
				{
					int a = 1;
				}
				for (int k = 1; k < j; k++)
				{
					if (i - j - 1 < j - k - 1) continue;
					int choose = C(i - j - 1, j - k - 1);
					table[i][j] = (table[i][j] + table[j][k] * choose) % 100003;
				}
				//printf("table[%d][%d] = %d\n", i, j, table[i][j]);
			}
		int sol = 0;
		for (int i = 1; i <= n; i++)
			sol = (sol + table[n][i]) % 100003;
		printf("Case #%d: %d\n", c, sol);
	}
}
#endif