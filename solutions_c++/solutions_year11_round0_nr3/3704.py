#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define INFILE "C-large.in"
#define OUTFILE "C-large.out"

int main()
{
	int i,j,k;
	int testnum, bagnum, candynum;
	int bin[30];
	int sum,min;
	FILE *fin, *fout;

	fin = fopen(INFILE,"r");
	if (fin == NULL) return -1;

	fout = fopen(OUTFILE,"w+");
	if (fout == NULL) return -1;

	fscanf(fin,"%d",&testnum);
	for (i=0; i<testnum; i++)
	{
		for (j=0; j<30; j++) bin[j] = 0;
		fscanf(fin,"%d",&bagnum);
		sum=0;
		min=99999999;
		for (j=0; j<bagnum; j++)
		{
			fscanf(fin,"%d",&candynum);	
			sum+=candynum;
			if (min > candynum) min=candynum;
			k=0;
			while(candynum)
			{
				bin[k]+=candynum%2;
				candynum/=2;
				k++;
			}
		}
		for (j=0; j<30; j++)
		{
			if (bin[j]%2)
			{
				fprintf(fout, "Case #%d: NO\n",i+1);
				break;
			}
		}
		if (j==30) fprintf(fout, "Case #%d: %d\n",i+1,sum-min);
	}


	fclose(fin);
	fclose(fout);

	return 0;
}