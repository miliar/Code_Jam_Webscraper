// Saving.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#define MAX_TEST 20
#define MAX_S 100
#define MAX_Q 1000

typedef struct search 
{
	char nm[100];
	int cnt;
}SEARCH;
int main(int argc, char* argv[])
{
	printf("Hello World!\n");
	FILE *fpin, *fpout  = NULL;
	unsigned int num_tst = 0;
	int ii, jj, kk = 0;
	int num_s, num_q = 0;
	SEARCH sev[MAX_S];
	SEARCH que[MAX_Q];
	int minser = 0;
	int ret = 0;
	int isfull = 0;
	int no_seach = 0;


	fpin = fopen("A-large.in.txt", "r");
	if(NULL == fpin)
	{
		printf("Open file ERR!\n");
		return -1;
	}
	fpout = fopen("A-large.out.txt", "w");
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
			memset(sev, 0, MAX_S*sizeof(SEARCH));
			memset(que, 0, MAX_Q*sizeof(SEARCH));
			fscanf(fpin, "%d\n", &num_s);
			for (jj =0; jj <num_s; jj++)
			{
				char ch = 0;
				int chcnt = 0;
				fscanf(fpin, "%c", &ch);
				while(ch != '\n')
				{
					sev[jj].nm[chcnt] = ch;
					chcnt++;
					fscanf(fpin, "%c", &ch);
				} 				
			}
			fscanf(fpin, "%d\n", &num_q);
			ret = 0;
			for (jj =0; jj <num_q; jj++)
			{
				char ch = 0;
				int chcnt = 0;
				fscanf(fpin, "%c", &ch);
				while(ch != '\n')
				{
					que[jj].nm[chcnt] = ch;
					chcnt++;
					fscanf(fpin, "%c", &ch);
				}

				no_seach = 0;
				for (kk =0; kk <num_s; kk++)
				{
					if (0 == strcmp(que[jj].nm, sev[kk].nm))
					{
						sev[kk].cnt++;
						no_seach = kk;
					}
				}
				isfull = 1;
				for (kk =0; kk <num_s; kk++)
				{
					if (0 == sev[kk].cnt)
					{
						isfull = 0;
						break;
					}
				}
				if (1 == isfull)
				{
					ret++;
					for (kk =0; kk <num_s; kk++)
					{
						if (kk != no_seach)
						{
							sev[kk].cnt=0;
						}
					}
				}
			}
			fprintf(fpout, "Case #%d: %d\n", ii+1, ret);
		}
	}

	fclose(fpin);
	fclose(fpout);
	return 0;
}


