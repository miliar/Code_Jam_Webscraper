#include<stdio.h>
int main(void)
{
	long totalcase, i, j, n, k;
	FILE *fin = fopen("A-large.in","r");
	FILE *fout = fopen("A-large.out","w");

	fscanf(fin,"%ld",&totalcase);
	for(i = 0;i < totalcase;i++)
	{
		fscanf(fin,"%ld%ld",&n, &k);
		for (j = 0; j < n; j++)
		{
			if ((1<<j) & (k + 1))
				break;
		}
		if (j == n)
		{
			fprintf(fout,"Case #%ld: ON\n",i + 1);
		}
		else
		{
			fprintf(fout,"Case #%ld: OFF\n",i + 1);
		}
		
	}
	return 0;
}