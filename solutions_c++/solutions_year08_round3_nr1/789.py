// Tmo.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <string.h>
#define MAX_N 100
#define MAX_NUM_BITS  100

int main(int argc, char* argv[])
{
	printf("Hello World!\n");
	FILE *fpin, *fpout  = NULL;
	unsigned long lineno = 0;
	unsigned long Pno, Kno, Lno = 0;
	int ii, jj, kk = 0;
    int alpt[MAX_NUM_BITS] = {0};
	unsigned long ret = 0;
	
	fpin = fopen("A-small.in.txt", "r");
	if(NULL == fpin)
	{
		printf("Open file ERR!\n");
		return -1;
	}
	fpout = fopen("A-small.out.txt", "w");
	if(NULL == fpout)
	{
		printf("Open file ERR!\n");
		fclose(fpin);
		return -1;
	}
	
    fscanf(fpin,"%ld",&lineno);
	if ((lineno > 0) && (lineno <= MAX_N))
    {
		ii = 0;
		while(ii++ < lineno)
		{
			fscanf(fpin,"%ld ",&Pno);
			fscanf(fpin,"%ld ",&Kno);
			fscanf(fpin,"%ld\n",&Lno);
			if (Lno > 1)
			{
				for (jj = 0; jj < Lno-1; jj++)
				{
					fscanf(fpin,"%ld ",&alpt[jj]);
				}
			}
			fscanf(fpin,"%ld\n",&alpt[jj]);

			for (jj = 0; jj < Lno; jj++)
			{
				for (kk = jj+1; kk < Lno; kk++)
				{
					unsigned long tmp = alpt[jj];
					if (alpt[jj] < alpt[kk])
					{
						alpt[jj] = alpt[kk];
						alpt[kk] = tmp;
					}
				}
			}

			unsigned long mut = 1;
			ret = 0;
			for (jj = 0; jj < Lno; jj++)
			{
				ret +=alpt[jj]*mut;
				if ((jj+1) % Kno == 0)
				{
					mut++;
				}
				if ((mut > Pno) && (jj+1 < Lno))
				{
					printf("ERR:%d\n", ii);
				}
			}
           
			fprintf(fpout, "Case #%d: %d\n", ii, ret);
			fflush(fpout);
		}
	}
	
    fclose(fpin);
	fclose(fpout);
	return 0;
}

