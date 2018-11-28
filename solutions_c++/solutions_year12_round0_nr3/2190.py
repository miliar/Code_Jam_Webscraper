
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
			UINT32	uA				= 0;
			UINT32	uB				= 0;
			UINT32	uNumOfRecycles	= 0;

			fscanf_s(pInputFile, "%d %d", &uA, &uB);

			for (jIndex=uA; jIndex<=uB; ++jIndex)
			{
				UINT32			uCurrentNum		= jIndex;
				UINT32			uDigits[7]		= {0};
				UINT32			uNumOfDigits	= 0;
				
				for (uNumOfDigits=0; uCurrentNum && (uNumOfDigits<7); ++uNumOfDigits)
				{
					uDigits[uNumOfDigits] = uCurrentNum % 10;
					uCurrentNum /= 10;
				}
				
				UINT32			kIndex					= 0;
				UINT32			uRecyclesNumbers[7]		= {0};
				UINT32			uCurrentIndex			= 0;
				for (kIndex=1; kIndex<uNumOfDigits; ++kIndex)
				{
					UINT32 rIndex		= 0;
					UINT32 uSecondNum	= 0;
					UINT32 u			= 1;

					for (rIndex=0; rIndex<uNumOfDigits; ++rIndex)
					{
						uSecondNum += uDigits[(kIndex + rIndex)%uNumOfDigits] * u;
						u *= 10;
					}

					if ((uB >= uSecondNum) && (uSecondNum > jIndex))
					{
						BOOL bFound = FALSE;
						for (rIndex=0; rIndex<uNumOfDigits; ++rIndex)
						{
							bFound = bFound || (uRecyclesNumbers[rIndex] == uSecondNum);
						}

						if (!bFound)
						{
							uRecyclesNumbers[uCurrentIndex++] = uSecondNum;
							//printf("(%d,%d)\n", jIndex, uSecondNum);
						}
					}
				}

				uNumOfRecycles += uCurrentIndex;

			}

			printf("Case #%d: %d\n", iIndex+1, uNumOfRecycles);
		}

	} while (FALSE);

	if (pInputFile)
	{
		fclose(pInputFile);
		pInputFile = NULL;
	}

	return 0;
}

