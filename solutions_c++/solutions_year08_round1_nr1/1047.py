#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fpIn;
	FILE *fpOut;

	fpIn = fopen("A-small-attempt0.in", "r");
	fpOut = fopen("A-small.out", "w");

	
	int nCaseNum;
	fscanf(fpIn, "%d", &nCaseNum);
	//for debug : begin
	//printf("nCaseNum = %d\n", nCaseNum);
	//for debug : end

	for(int nCount1 = 0; nCount1 < nCaseNum; nCount1++)
	{
		int nVectorSize;
		fscanf(fpIn, "%d", &nVectorSize);
		
		//for debug : begin
		//printf("nVectorSize = %d\n", nVectorSize);
		//for debug : end

		long *aVector1, *aVector2;
		aVector1 = (long *)malloc(sizeof(long) * nVectorSize);
		aVector2 = (long *)malloc(sizeof(long) * nVectorSize);

		for(int i = 0; i < nVectorSize; i++)
			fscanf(fpIn, "%ld", &aVector1[i]);

		for(int i = 0; i < nVectorSize; i++)
			fscanf(fpIn, "%ld", &aVector2[i]);
		

		//for debug : begin
		/*
		for(int i = 0; i < nVectorSize; i++)
			printf("%ld  ", aVector1[i]);
		printf("\n");
		for(int i = 0; i < nVectorSize; i++)
			printf("%ld  ", aVector2[i]);*/
		//for debug : end

		for(int i = 0; i < nVectorSize - 1; i++)
		{
			for(int j = 0; j < nVectorSize - 1 - i; j++)
			{
				if(aVector1[j] > aVector1[j + 1])
				{
					long lTemp;
					lTemp = aVector1[j];
					aVector1[j] = aVector1[j + 1];
					aVector1[j + 1] = lTemp;
				}
			}
		}

		for(int i = 0; i < nVectorSize - 1; i++)
		{
			for(int j = 0; j < nVectorSize - 1 - i; j++)
			{
				if(aVector2[j] < aVector2[j + 1])
				{
					long lTemp;
					lTemp = aVector2[j];
					aVector2[j] = aVector2[j + 1];
					aVector2[j + 1] = lTemp;
				}
			}
		}

		long lSum = 0;
		for(int i = 0; i < nVectorSize; i++)
		{
			lSum = lSum + aVector1[i]*aVector2[i];
		}

		fprintf(fpOut, "Case #%d: %ld\n", nCount1 + 1, lSum);

		free(aVector1);
		free(aVector2);

	}

	return 0;
}