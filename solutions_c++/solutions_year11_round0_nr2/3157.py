// Problem_2_QR.cpp : Defines the entry point for the console application.
//

#include <Windows.h>
#include <stdio.h>

static CHAR g_chBaseElements[10] = {'A', '\0', 'W', 'D', 'E', 'F', 'Q', 'R', 'S', '\0'};
#define GetIndex(ch) (((ch) - 'A') % 10)

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
			UINT32 iNumOfCombine		= 0;
			UINT32 iNumOfOpposed		= 0;
			UINT32 iNumOfInvokes		= 0;
			UINT32 iPairIndex			= 0;
			UINT32 iInvokeIndex			= 0;
			UINT32 iElemIndex			= 0;

			CHAR	chCombineMatrix[10][10] = {0};
			CHAR	chOpposedMatrix[10][10] = {0};

			CHAR	chElements[100]		= {0};
			UINT32	chBaseElements[10]	= {0};

			CHAR	chElemA, chElemB, chCombineElem;

			memset(chCombineMatrix, 0, 100);
			memset(chOpposedMatrix, 0, 100);

			memset(chElements, 0, 100);
			memset(chBaseElements, 0, 10*sizeof(UINT32));

			fscanf(pInputFile, "%d", &iNumOfCombine);
			//printf("Got %d combinations in test case #%d...\n", iNumOfCombine, iTestCaseIndex + 1);

			for (iPairIndex=0; iPairIndex<iNumOfCombine; ++iPairIndex)
			{
				fscanf(pInputFile, " %c%c%c", &chElemA, &chElemB, &chCombineElem);
				//printf("Got (%c,%c)=>%c combination ...\n", chElemA, chElemB, chCombineElem);

				chCombineMatrix[GetIndex(chElemA)][GetIndex(chElemB)] = chCombineElem;
				chCombineMatrix[GetIndex(chElemB)][GetIndex(chElemA)] = chCombineElem;
			}

			fscanf(pInputFile, " %d", &iNumOfOpposed);
			//printf("Got %d opposes in test case #%d...\n", iNumOfOpposed, iTestCaseIndex + 1);

			for (iPairIndex=0; iPairIndex<iNumOfOpposed; ++iPairIndex)
			{
				fscanf(pInputFile, " %c%c", &chElemA, &chElemB);
				//printf("Got (%c,%c) Opposed ...\n", chElemA, chElemB);

				chOpposedMatrix[GetIndex(chElemA)][GetIndex(chElemB)] = 1;
				chOpposedMatrix[GetIndex(chElemB)][GetIndex(chElemA)] = 1;
			}

			fscanf(pInputFile, " %d ", &iNumOfInvokes);
			//printf("Got %d invokes in test case #%d...\n", iNumOfInvokes, iTestCaseIndex + 1);

			for (iInvokeIndex=0; iInvokeIndex<iNumOfInvokes; ++iInvokeIndex)
			{
				fscanf(pInputFile, "%c", &chElemA);
				
				chElements[iElemIndex] = chElemA;
				chBaseElements[GetIndex(chElemA)] += 1;

				if (iElemIndex)
				{
					if (chCombineMatrix[GetIndex(chElements[iElemIndex])][GetIndex(chElements[iElemIndex-1])])
					{
						if(g_chBaseElements[GetIndex(chElements[iElemIndex-1])] == chElements[iElemIndex-1])
						{
							chBaseElements[GetIndex(chElements[iElemIndex])]	-= 1;
							chBaseElements[GetIndex(chElements[iElemIndex-1])]	-= 1;

							chElements[iElemIndex-1] = chCombineMatrix[GetIndex(chElements[iElemIndex])][GetIndex(chElements[iElemIndex-1])];
						}
						else
						{
							++iElemIndex;
						}

					} 
					else
					{
						UINT32 iIndex = 0;

						++iElemIndex;

						for (iIndex=0; iIndex<10; ++iIndex)
						{
							if ((chOpposedMatrix[GetIndex(chElements[iElemIndex-1])][iIndex]) && chBaseElements[iIndex])
							{
								memset(chElements, 0, 100);
								memset(chBaseElements, 0, 10*sizeof(UINT32));
								iElemIndex = 0;
							}
						}
					}
				}
				else
				{
					++iElemIndex;
				}
			}

			printf("Case #%d: [", iTestCaseIndex+1);

			for (iInvokeIndex=0; iInvokeIndex<iElemIndex; ++iInvokeIndex)
			{
				if (iInvokeIndex)
				{
					printf(", %c", chElements[iInvokeIndex]);
				}
				else
				{
					printf("%c", chElements[iInvokeIndex]);
				}
			}

			printf("]\n");

			fscanf(pInputFile, "\n");

			//printf("Case #%d: %d\n", iTestCaseIndex+1, currentTime);

		}


	} while (FALSE);

	//printf("Done !!!\n");

	if (pInputFile)
	{
		fclose(pInputFile);
	}

	return 0;
}

