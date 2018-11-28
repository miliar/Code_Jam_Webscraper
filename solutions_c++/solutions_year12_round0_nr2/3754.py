#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <algorithm>

using namespace std;

int a[105];
int n, p, s;

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, ca = 1;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d%d%d", &n, &s, &p);
		int i = 0, ans = 0;
		for ( i=0; i<n; i++)
			scanf("%d", &a[i]);
		sort(a, a+n);
		int t = max(p, 0)+max(p-2, 0)+max(p-2, 0);
		for ( i=0; i<n; i++)
		{
			if (a[i] >= t)
				break;
		}
		for ( ; i<n; i++)
		{
			if (p == 1 || p == 0)
			{
				if (a[i] >= t)
					ans ++;
				continue;
			}
			if (a[i] == t || a[i] == t+1)
			{
				if (s)
				{
					s --;
					ans ++;
				}
			}
			else
			{
				ans ++;
			}
		}
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}

