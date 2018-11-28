#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int times[35];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("p1.out","w",stdout);
	int t;
	int i;
	times[1] = 1;
	for (i = 2;i <= 30;i++)
	{
		times[i] = times[i-1]*2+1;
	}
	scanf("%d",&t);
	int n,k;
	for (i = 1;i <= t;i++)
	{
		scanf("%d%d",&n,&k);
		if (k < times[n])
			printf("Case #%d: OFF\n",i);
		else if ((k-times[n])%(times[n]+1) == 0)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}