// // code_jam2.cpp : Defines the entry point for the console application.
// //
// 
// #include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int compare_T(const void* a, const void* b)
{
	int ai = *((int*)a), bi = *((int*)b);
	if(ai<bi)
		return 1;
	else if(ai>bi)
		return -1;
	else 
		return 0;
}
int main()
{

	int letterFeq[10000];
//	qsort(temp, 10, sizeof(temp[0]), &compare_T);
	int t =0;
	FILE *fp, *fpwrite;
	fp = fopen("c:\\A-small-attempt0.in", "rt");
	fpwrite = fopen("c:\\output.txt", "wt");
	if(fp==NULL)
	{
		printf("can not open.");
	}
	fscanf(fp, "%d", &t);

	for (int i=0; i<t; i++) // for each case.
	{
		int maxLetterPerKey=0, totalKey, totalLetter;
		fscanf(fp, "%d %d %d", &maxLetterPerKey, &totalKey, &totalLetter);
		for(int j=0; j<totalLetter; j++)
		{
			fscanf(fp, "%d", &letterFeq[j]);
		}
		
		qsort(letterFeq, totalLetter, sizeof(letterFeq[0]), &compare_T);

		int tempAvail = totalKey;
		int keyStrockRequired=1;
		int r = 0;
		for(int j=0; j<totalLetter; j++)
		{
			if(tempAvail<=1)
			{
				r+= (letterFeq[j] * keyStrockRequired);
				tempAvail = totalKey;
				keyStrockRequired++;
			}
			else
			{
				r+=(letterFeq[j] * keyStrockRequired);
				tempAvail --;
			}
		}
		
		fprintf(fpwrite, "Case #%d: %d\n", i+1, r);

	}
	fclose(fp);
	fclose(fpwrite);
	return 0;
}
