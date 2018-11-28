// Problem_3_QR.cpp : Defines the entry point for the console application.
//

#include <Windows.h>
#include <stdio.h>

int main(int argc, CHAR* argv[])
{

	FILE *	pInputFile		= NULL;
	UINT32	iNumOfTestCases = 0;
	UINT32	iTestCaseIndex	= 0;

	do 
	{
		if (argc != 2)
		{
			printf("Need input file...\n");
			break;
		}

		pInputFile = fopen(argv[1], "r");
		if (!pInputFile)
		{
			printf("Problem opening input file (%s)...\n", argv[1]);
			break;
		}

		fscanf(pInputFile, "%d\n", &iNumOfTestCases);

		//printf("Got %d test cases...\n", iNumOfTestCases);

		for(iTestCaseIndex=0; iTestCaseIndex<iNumOfTestCases; ++iTestCaseIndex)
		{
			UINT32 iNumOfCandies	= 0;
			UINT32 iCandyIndex		= 0;
			UINT32 iCandyValue		= 0;

			UINT32 iMinCandyValue	= -1;
			UINT32 iCandiesValSum	= 0;
			UINT32 iCandiesXor		= 0;


			fscanf(pInputFile, "%d\n", &iNumOfCandies);
			//printf("Got %d candies in test case #%d...\n", iNumOfCandies, iTestCaseIndex + 1);

			for (iCandyIndex=0; iCandyIndex<iNumOfCandies; ++iCandyIndex)
			{
				fscanf(pInputFile, " %d", &iCandyValue);

				iMinCandyValue	= min(iCandyValue, iMinCandyValue);
				iCandiesValSum	+= iCandyValue;
				iCandiesXor		^= iCandyValue;
			}

			if (iCandiesXor)
			{
				printf("Case #%d: NO\n", iTestCaseIndex+1);
			} 
			else
			{
				printf("Case #%d: %d\n", iTestCaseIndex+1, iCandiesValSum - iMinCandyValue);
			}

			fscanf(pInputFile, "\n");

			iNumOfCandies	= 0;
			iCandyIndex		= 0;
			iCandyValue		= 0;
			iMinCandyValue	= -1;
			iCandiesValSum	= 0;
			iCandiesXor		= 0;
			
		}

	} while (FALSE);

	//printf("Done !!!\n");

	if (pInputFile)
	{
		fclose(pInputFile);
	}

	return 0;
}
