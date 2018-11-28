#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
int a[10000];
int main ()
{
	double sum;
	int t, n, i, j, cas;
	freopen("D:/4.txt","w",stdout);
	scanf ("%d",&t);
	{
		cas = 1;
		for (i = 0;i < t; i++)
		{
			scanf ("%d",&n);
			sum = 0;
			for ( j = 0; j < n;j ++)
			{
				scanf ("%d",&a[j]);
				if((a[j] - 1) != j)
				{sum += 1.0;}
			}
			printf("Case #%d: %.6lf\n",cas ++,sum);
		}
	}
	return 0;
}