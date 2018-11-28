#include<iostream>
#include<stdio.h>

using namespace std;

int ar[20];

void cas(int t)
{
	int n, i, j;
	
	scanf("%d", &n);
	
	int xr = 0;
	int sum = 0, min = 0x7fffffff;
	
	for (i = 0; i < n; i++) 
	{
		scanf("%d", &ar[i]);
		sum += ar[i];
		if (ar[i] < min) min = ar[i];
		xr ^= ar[i];
	}

	if (xr) 
	{
		printf("Case #%d: NO\n", t);
		return;
	}
	printf("Case #%d: %d\n", t, sum-min);
	return;
}

int main()
{
	int t, i;
	
	scanf("%d", &t);

	for (i = 1; i <= t; i++)
	{
		cas(i);
	}
	return 0;
}
