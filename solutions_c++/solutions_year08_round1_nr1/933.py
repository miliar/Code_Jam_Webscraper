// MiniSP.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <math.h>
#include <string.h>
#define MAX_T 1000
#define MAX_N 800
#define MAX_NUM_BITS  100

int main(int argc, char* argv[])
{
	printf("Hello World!\n");
	FILE *fpin, *fpout  = NULL;
	unsigned long lineno = 0;
	unsigned long nno = 0;
	int ii, jj, kk = 0;
    int vx[MAX_N], vy[MAX_N] = {0};
	long ret;
	
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
	if ((lineno > 0) && (lineno <= MAX_T))
    {
		ii = 0;
		while(ii++ < lineno)
		{
			fscanf(fpin,"%d\n",&nno);
			jj = 0;
			if (nno > 1)
			{
				
				do
				{
					fscanf(fpin, "%ld ",&vx[jj]);
				}while(++jj < nno-1);
			}
			fscanf(fpin, "%ld\n",&vx[jj]);
			
			jj = 0;
			if (nno > 1)
			{
				do
				{
					fscanf(fpin, "%ld ",&vy[jj]);
				}while(++jj < nno-1);
			}
			fscanf(fpin, "%ld\n",&vy[jj]);

			for (jj = 0; jj < nno; jj++)
			{				
				for (kk = jj+1; kk < nno; kk++)
				{
					if (vx[jj] > vx[kk])
					{
						int tmp = vx[kk];
						vx[kk] = vx[jj];
						vx[jj] = tmp;
					}
				}
			}

			for (jj = 0; jj < nno; jj++)
			{				
				for (kk = jj+1; kk < nno; kk++)
				{
					if (vy[jj] < vy[kk])
					{
						int tmp = vy[kk];
						vy[kk] = vy[jj];
						vy[jj] = tmp;
					}
				}
			}
			ret = 0;
			for (jj = 0; jj < nno; jj++)
			{	
				ret+= vx[jj]*vy[jj];
			}            
			fprintf(fpout, "Case #%d: %d\n", ii, ret);
			fflush(fpout);
		}
	}

    fclose(fpin);
	fclose(fpout);
	return 0;
}

