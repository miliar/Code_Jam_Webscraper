#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define INFILE "A-large.in"
#define OUTFILE "A-large.out"

int main()
{
	int i,j,temp1,temp2;
	int locO,locB,timeO,timeB;
	int testnum, movenum, locnum;
	char robot;
	FILE *fin, *fout;

	fin = fopen(INFILE,"r");
	if (fin == NULL) return -1;

	fout = fopen(OUTFILE,"w+");
	if (fout == NULL) return -1;

	fscanf(fin,"%d",&testnum);
	for (i=0; i<testnum; i++)
	{		
		fscanf(fin,"%d",&movenum);
		locO = locB = 1;
		timeO = timeB = 0;

		for (j=0; j<movenum; j++)
		{
			fscanf(fin," %c %d", &robot,&locnum);
			if (robot == 'O')
			{
				temp1 = timeO + abs(locnum - locO);
				if (temp1 > timeB) timeO = temp1 + 1;
				else timeO = timeB + 1;
				locO = locnum;
			}
			else
			{
				temp1 = timeB + abs(locnum - locB);
				if (temp1 > timeO) timeB = temp1 + 1;
				else timeB = timeO + 1;
				locB = locnum;
			}
		}

		if (timeB > timeO) fprintf(fout, "Case #%d: %d\n",i+1,timeB);
		else fprintf(fout, "Case #%d: %d\n",i+1,timeO);


	}


	fclose(fin);
	fclose(fout);

	return 0;
}