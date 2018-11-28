#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *fpIn;
	FILE *fpOut;

	fpIn = fopen("A-small-attempt0.in", "r");
	fpOut = fopen("A-small.out", "w");

	int nCaseNum;
	fscanf(fpIn, "%d", &nCaseNum);

	for(int nCount = 0; nCount < nCaseNum; nCount++)
	{
		int nMaxLetterPerKey;
		int nKeyNum;
		int nLetterNum;
		fscanf(fpIn, "%d %d %d", &nMaxLetterPerKey, &nKeyNum, &nLetterNum);

		int *aRate = (int *)malloc(sizeof(int)*nLetterNum); 
		for(int i = 0; i < nLetterNum; i++)
			fscanf(fpIn, "%d", &aRate[i]);
		for(int i = 0; i < nLetterNum -1; i++)
		{
			for(int j = 0; j < nLetterNum - 1 - i; j++)
			{
				if(aRate[j] < aRate[j+1])
				{
					int nTemp;
					nTemp = aRate[j];
					aRate[j] = aRate[j+1];
					aRate[j+1] = nTemp;
				}
			}
		}

		int nPressNum = 0;
		
		int nTimes = 0;
		for(int i = 0; i < nLetterNum; )
		{
			nTimes++;
			if((nLetterNum - i) < nKeyNum)
			{
				int nSum = 0;
				for(int j = 0; (i+j) < nLetterNum; j++)
				{
					nSum = nSum + aRate[i + j]*nTimes;
				}
				i = nLetterNum;
				nPressNum = nPressNum + nSum;
			}
			else
			{
				int nSum = 0;
				for(int j = 0; j < nKeyNum; j++)
				{
					nSum = nSum + aRate[i + j]*nTimes;
				}
				i = i + nKeyNum;
				nPressNum = nPressNum + nSum;
			}
		}

		fprintf(fpOut, "Case #%d: %d\n", nCount + 1, nPressNum);

		free(aRate);
	}

	fclose(fpIn);
	fclose(fpOut);


	return 0;
}