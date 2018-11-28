// Train.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>

#define MAX_TEST 100
#define MAX_NAB 100
#define MAX_T 60

typedef struct tim 
{
	int hh;
	int mm;
	int submm;
}TIM;
typedef struct ntrp 
{
	TIM str;
	TIM end;
	int isre;
}NTRP;

int main(int argc, char* argv[])
{
	printf("Hello World!\n");
	FILE *fpin, *fpout  = NULL;
	unsigned int num_tst = 0;
	int ii, jj, kk = 0;
	int ttim = 0;
	int num_nAb, num_nBa = 0;
	NTRP nAb[MAX_NAB];
	NTRP nBa[MAX_NAB];
	int mst_nAb, mst_nBa = 0;


	fpin = fopen("B-large.in.txt", "r");
	if(NULL == fpin)
	{
		printf("Open file ERR!\n");
		return -1;
	}
	fpout = fopen("B-large.out.txt", "w");
	if(NULL == fpout)
	{
		printf("Open file ERR!\n");
		fclose(fpin);
		return -1;
	}
    fscanf(fpin,"%d\n",&num_tst);
	if ((0 < num_tst) && (num_tst <= MAX_TEST))
	{
		for (ii = 0; ii < num_tst; ii++)
		{
			memset(nAb, 0, MAX_NAB*sizeof(NTRP));
			memset(nBa, 0, MAX_NAB*sizeof(NTRP));
			mst_nAb = 0;
			mst_nBa = 0;

			fscanf(fpin, "%d\n", &ttim);
			fscanf(fpin, "%d ", &num_nAb);
			fscanf(fpin, "%d\n", &num_nBa);
			//printf("%d\n", ttim);
			//printf("%d %d\n", num_nAb, num_nBa);

			mst_nAb = num_nAb;
			mst_nBa = num_nBa;

			if ((0 != num_nAb) && (0 != num_nBa))
			{
				for (jj =0; jj <num_nAb; jj++)
				{
					fscanf(fpin, "%d:%d ", &nAb[jj].str.hh, &nAb[jj].str.mm);
					fscanf(fpin, "%d:%d\n", &nAb[jj].end.hh, &nAb[jj].end.mm);
					//printf("%02d:%02d ", nAb[jj].str.hh, nAb[jj].str.mm);
					//printf("%02d:%02d\n", nAb[jj].end.hh, nAb[jj].end.mm);
					nAb[jj].str.submm = 60*nAb[jj].str.hh + nAb[jj].str.mm;
					nAb[jj].end.submm = 60*nAb[jj].end.hh + nAb[jj].end.mm;
					
				}

				for (jj =0; jj <num_nBa; jj++)
				{
					fscanf(fpin, "%d:%d ", &nBa[jj].str.hh, &nBa[jj].str.mm);
					fscanf(fpin, "%d:%d\n", &nBa[jj].end.hh, &nBa[jj].end.mm);
					//printf("%02d:%02d ", nBa[jj].str.hh, nBa[jj].str.mm);
					//printf("%02d:%02d\n", nBa[jj].end.hh, nBa[jj].end.mm);
					nBa[jj].str.submm = 60*nBa[jj].str.hh + nBa[jj].str.mm;
					nBa[jj].end.submm = 60*nBa[jj].end.hh + nBa[jj].end.mm;

					if ((num_nBa-mst_nBa) == num_nAb)
					{
						continue;
					}

					int min_kk = -1;
					int min_submm = 0;

					for (kk =0; kk <num_nAb; kk++)
					{
						if (1 == nAb[kk].isre)
						{
							continue;
						}
						if (nBa[jj].str.submm >= (nAb[kk].end.submm + ttim))
						{

							if ((0 == min_submm) || (min_submm < (nAb[kk].end.submm + ttim)))
							{
								min_kk = kk;
								min_submm = nAb[kk].end.submm + ttim;
							}
						}
					}
					if (-1 != min_kk)
					{
						mst_nBa--;
						nAb[min_kk].isre = 1;
					}
				}

				for (jj =0; jj <num_nAb; jj++)
				{
					int min_kk = -1;
					int min_submm = 0;

					for (kk =0; kk <num_nBa; kk++)
					{
						if (1 == nBa[kk].isre)
						{
							continue;
						}
						if (nAb[jj].str.submm >= (nBa[kk].end.submm + ttim))
						{
							if ((0 == min_submm) || (min_submm < (nBa[kk].end.submm + ttim)))
							{
								min_kk = kk;
								min_submm = nBa[kk].end.submm + ttim;
							}
						}
					}
					if (-1 != min_kk)
					{
						mst_nAb--;
						nBa[min_kk].isre = 1;
					}
					if ((num_nAb-mst_nAb) == num_nBa)
					{
						break;
					}
				}
			}

			fprintf(fpout, "Case #%d: %d %d\n", ii+1, mst_nAb, mst_nBa);
		}
	}

	fclose(fpin);
	fclose(fpout);
	return 0;
}

