#include"stdafx.h"
#include<stdio.h>
 
int main()
{
	FILE *in=fopen("A-large.in", "r"), *out=fopen("A-large.out", "w");
	int n, k, times, power;
	int i, j;
	fscanf(in, "%d", &times);
	for(i=1; i<=times; i++)
	{
		fscanf(in, "%d %d", &n, &k);
		power = 1;
		for(j=0; j<n; j++)
			power *= 2;
		if(k/power != (k+1)/power)
			fprintf(out, "Case #%d: ON\n", i);
		else
			fprintf(out, "Case #%d: OFF\n", i);
	}
	
	return 0;
}