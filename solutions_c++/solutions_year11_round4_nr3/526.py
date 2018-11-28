#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

int main()
{
	int i, n, j, p, t, k, r, ans;
	bool ok = false;
	freopen("b.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &t);
	for(i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		ans = 0;
		for(k = 2; k < n; k++)
		{
			ok = true;
			for(j = 2; j < k; j++)
			{
				if(k % j == 0)
				{
					ok = false;
					break;
				}
			}
			j = 1;
			if(ok)
			{
				p = k;
				while(p * k <= n)
				{
					j++;
					p *= k;
				}
			}
			ans += j - 1;
		}
		if(n == 1)
		{
			printf("Case #%d: 0\n", i);
		}
		else
			printf("Case #%d: %d\n", i, ans + 1);
	}
    return 0;
}
