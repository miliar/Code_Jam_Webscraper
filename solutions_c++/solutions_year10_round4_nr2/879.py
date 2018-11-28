#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int n, t;
int a[200][100];
int c[200];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d", &n);
		for (int i = 1; i < 2 * n; i++)
			if (i <= n)
				c[i] = i;
			else
				c[i] = n - (i - n);
		for (int i = 1; i < 2 * n; i++)
			for (int j = 1; j <= c[i]; j++
				scanf("%d", &a[i][j]);
		for (size = 2; size <= k; size++)
		{
			bool bb = true;
			for (int i = n - size + 1; i <= n; i++)
				for (int j = 
		}
	}
	return 0;
}
