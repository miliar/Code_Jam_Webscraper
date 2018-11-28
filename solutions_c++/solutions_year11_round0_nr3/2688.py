#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <math.h>
#include <cmath>
using namespace std;

int main ()
{
	int a[100];
	int t, n, i, j, sum, temp, max, x, cas, k;
	freopen("D:/1.txt","w",stdout);
scanf ("%d",&t) ;
	{
		cas = 0;
		for (k = 0;k < t;k ++)
		{
			cas ++;
			scanf ("%d", &n);
			sum = 0;
			for (j = 0;j < n;j ++)
			{
				scanf ("%d",&a[j]);
				sum += a[j];
			}
			x = ( a[0] ^ a[1] );
			for (i = 2;i < n;i ++)
			{
				x ^= a[i];
			}
			max = 0;
			for (i = 0; i < n;i ++)
			{
				if( ( x ^ a[i] ) == a[i] )
				{
					temp = sum - a[i];
					if( temp > max )
					{max = temp;}
				}
			}
			if (max == 0)
			{printf("Case #%d: NO\n",cas);}
			else
			{printf("Case #%d: %d\n",cas,max);}
		}
	}
	return 0;
}