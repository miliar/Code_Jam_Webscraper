
#include <Windows.h>
#include <stdio.h>


int main(int argc, char* argv[])
{
	UINT32		numOfTestCases	= 0;
	UINT32		iIndex			= 0;
	FILE *		pInputFile		= NULL;

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

		fscanf_s(pInputFile, "%d", &numOfTestCases);

		for (iIndex=0; iIndex<numOfTestCases; ++iIndex)
		{
			UINT32	jIndex			= 0;
			UINT32	uNumOfScores	= 0;
			UINT32	uSurprising		= 0;
			UINT32	uBestScore		= 0;
			UINT32	uNumOfBestScore	= 0;

			fscanf_s(pInputFile, "%d %d %d", &uNumOfScores, &uSurprising, &uBestScore);

			for (jIndex=0; jIndex<uNumOfScores; ++jIndex)
			{
				UINT32 uCurrentScore = 0;
				fscanf_s(pInputFile, "%d", &uCurrentScore);

				UINT32 uDivider		= (uCurrentScore / 3);
				UINT32 uRemainder	= (uCurrentScore % 3);

				if ((uBestScore <= uDivider) || 
					(uRemainder && (uBestScore <= (uDivider+1))))
				{
					uNumOfBestScore++;
				}
				else if (uSurprising && 
					((1 < uCurrentScore) && (uCurrentScore < 29)) &&
					(((2 == uRemainder) && (uBestScore <= (uDivider+2))) || ((!uRemainder) && (uBestScore <= (uDivider+1))))  )
				{
					uSurprising--;
					uNumOfBestScore++;
				}
			}

			printf("Case #%d: %d\n", iIndex+1, uNumOfBestScore);
		}

	} while (FALSE);

	if (pInputFile)
	{
		fclose(pInputFile);
		pInputFile = NULL;
	}

	return 0;
}

