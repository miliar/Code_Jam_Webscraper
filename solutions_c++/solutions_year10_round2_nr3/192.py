#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int f[512][512], ans[512];

int main()
{
	freopen("f:\\C-large.in", "r", stdin);
	freopen("f:\\C-large.out", "w", stdout);

	for (int n = 0; n < 512; n++)
		f[n][0] = 0;
	for (int m = 0; m < 512; m++)
		f[0][m] = 1;
	for (int n = 0; n < 512; n++)
	{
		for (int m = 0; m < 512; m++)
		{
			for (int k = 1; k <= m; k++)
			{
				if (n - k >= 0)
				{
					f[n][m] = (f[n][m] + f[n - k][m]) % 100003;
				}
			}
		}
	}
	
	for (int i = 0; i < 512; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			ans[i] = (ans[i] + f[j][i - j]) % 100003;
			if (ans[i] < 0) ans[i] += 100003;
		}
	}
	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", t_case, ans[n - 1]);
	}
	return 0;
}
