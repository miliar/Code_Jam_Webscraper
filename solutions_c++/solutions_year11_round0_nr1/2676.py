#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cmath>
using namespace std;
int main ()
{
	int cas, n, i, j;
	char c;
	int x, x1, y, y1, to, tb, w, ans;
	freopen("D:/3.txt","w",stdout);
	scanf ("%d",&cas);
	for (i = 0; i < cas; i++)
	{
		scanf ("%d",&n);
		to = 0; tb = 0; x = 1; y = 1;
		getchar();
		scanf ("%c%d",&c,&w);
		if(c == 'O')
		{
			x = w;
			to = w;
		}
		if(c == 'B')
		{
			y = w;
			tb = w;
		}
		ans = w;
		for (j = 1 ;j < n;j ++)
		{
			getchar();
			scanf ("%c%d",&c,&w);
			if (c=='O')
			{
				x1 = w;
				if(abs( x1 - x ) <= tb)
				{
					ans += 1;
					to += 1;
				}
				else
				{
					ans = ans + abs( x1 - x ) + 1 - tb ;
					to += abs( x1 - x ) - tb + 1;
				}
				tb = 0;
				x = x1;
			}
			if(c == 'B')
			{
				y1 = w;
				if(abs(y1 - y)  <= to)
				{
					tb += 1;
					ans += 1;
				}
				else
				{
					ans = ans + abs(y1 - y) - to + 1;			
					tb += abs(y1 - y) + 1 - to ;
				}
				to = 0;
				y = y1;
			}
		}
		printf("Case #%d: %d\n",i+1, ans);
	}
	return 0;
}
