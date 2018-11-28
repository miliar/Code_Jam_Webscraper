#include<cstdio>
#include<vector>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define _max(a, b) ((a) > (b) ? (a) : (b))
using namespace std;

char a[111][111];
int n, m, T;
int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	cin>> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		bool f = 0;
		scanf("%d%d\n", &n, &m);
		for (int i = 1; i <= n; i++) scanf("%s", a[i] + 1);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++) if (a[i][j] == '#')
			{
				if (i == n || j == m || a[i][j + 1] != '#' || a[i + 1][j] != '#' || a[i + 1][j + 1] != '#')
				{
					f = 1;
					break;
				}
				a[i][j] = '/', a[i + 1][j] = '\\', a[i][j + 1] = '\\', a[i + 1][j + 1] = '/';
			}
			if (f) break;
		}
		if (f)
		{
			puts("Impossible");
			continue;
		}
		for (int i = 1; i <= n; i++, puts(""))
			for (int j = 1; j <= m; j++) printf("%c", a[i][j]);
	}
	return 0;
}
