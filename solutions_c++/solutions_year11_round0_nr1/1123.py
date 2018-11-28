#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

int const MAX = 1000;

int main()
{
	int i, n, t, j, time, x, o, b, lasto, lastb, timeo, timeb;
	char c;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for(i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		time = 0;
		lasto = 1;
		lastb = 1;
		timeo = 0;
		timeb = 0;
		for(j = 0; j < n; j++)
		{
			scanf("%c", &c);
			while(c == ' ') scanf("%c", &c);
			scanf("%d", &x);
			if(c == 'O')
			{
				if(fabs(lasto - x) <= timeo)
				{
					timeb++;
					timeo = 0;
					lasto = x;
					time++;
				}
				else
				{
					timeb += 1 + (fabs(lasto - x) - timeo);
					time += 1 + (fabs(lasto - x) - timeo);
					timeo = 0;
					lasto = x;
				}
			}
			else
			{
				if(fabs(lastb - x) <= timeb)
				{
					timeo += 1;
					time++;
					timeb = 0;
					lastb = x;
				}
				else
				{
					timeo += 1 + (fabs(lastb - x) - timeb);
					time += 1 + (fabs(lastb - x) - timeb);
					timeb = 0;
					lastb = x;
				}
			}
		}
		printf("Case #%d: %d\n", i, time);
	}
    return 0;
}