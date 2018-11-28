#include <stdio.h>
#include <math.h>
int main()
{
	FILE *fin = fopen("INP.in","r");
	FILE *fout = fopen("OUT.out","w");
	int t;
	fscanf(fin,"%d",&t);
	for(int x = 1; x <= t;x++)
	{
		int n,k;
		fscanf(fin,"%d %d",&n,&k);
		long long min = 0;
		for(int i = 0; i < n ;i ++)
			min += pow(2.0,i);
		int found = 0;
		int current = min;
		while(current < 100000000 && current <= k)
		{
			if (current == k)
			{
				found = 1;
				break;
			}
			current ++;
			current += min;
		}
		if (found == 1)
			fprintf(fout,"Case #%d: ON\n",x);
		else
			fprintf(fout,"Case #%d: OFF\n",x);
	}
}
