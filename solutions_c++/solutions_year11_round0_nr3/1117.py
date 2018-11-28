#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int n, t, i, a, b, max, s, j;
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		scanf("%d", &n);
		scanf("%d", &a);
		max = a;
		s = a;
		for(j = 0; j < n - 1; j++)
		{
			scanf("%d", &b);
			a ^= b;
			s += b;
			if(b < max)
			{
				max = b;
			}
		}
		if(a == 0)
		{
			printf("Case #%d: %d\n", i + 1, s - max);
		}
		else
		{
			printf("Case #%d: NO\n", i + 1);
		}
	}
    return 0;
}
