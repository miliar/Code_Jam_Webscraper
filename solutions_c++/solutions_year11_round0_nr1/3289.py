// Problem_1_QR.cpp : Defines the entry point for the console application.
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
			UINT32 iNumOfMoves			= 0;
			UINT32 iMoveIndex			= 0;

			UINT32	currentTime			= 0;

			UINT32	blackLastMoveTime	= 0;
			UINT32	orangeLastMoveTime	= 0;

			UINT32	blackLastMovePos	= 1;
			UINT32	orangeLastMovePos	= 1;

			fscanf(pInputFile, "%d", &iNumOfMoves);
			//printf("Got %d moves in test case #%d...\n", iNumOfMoves, iTestCaseIndex + 1);

			for (iMoveIndex=0; iMoveIndex<iNumOfMoves; ++iMoveIndex)
			{
				CHAR	chRobotInitial		= '0';
				INT32	iButtonNumber		= 0;

				INT32	iCurrentMoveTime	= 0;
				INT32	stallTime			= 0;

				fscanf(pInputFile, " %c %d", &chRobotInitial, &iButtonNumber);
				//printf("Robot %c needs to push button #%d...\n", chRobotInitial, iButtonNumber);

				if ((chRobotInitial == 'O') || (chRobotInitial == 'o'))
				{
					iCurrentMoveTime	= abs(orangeLastMovePos - iButtonNumber) + 1;
					stallTime			= currentTime - (orangeLastMoveTime + iCurrentMoveTime) + 1;
					stallTime			= (0 < stallTime) ? stallTime : 0;

					currentTime			= orangeLastMoveTime + iCurrentMoveTime + stallTime;

					orangeLastMoveTime	= currentTime;
					orangeLastMovePos	= iButtonNumber;
				} 
				else
				{
					iCurrentMoveTime	= abs(blackLastMovePos - iButtonNumber) + 1;
					stallTime			= currentTime - (blackLastMoveTime + iCurrentMoveTime) + 1;
					stallTime			= (0 < stallTime) ? stallTime : 0;

					currentTime			= blackLastMoveTime + iCurrentMoveTime + stallTime;

					blackLastMoveTime	= currentTime;
					blackLastMovePos	= iButtonNumber;
				}
			}

			fscanf(pInputFile, "\n");

			printf("Case #%d: %d\n", iTestCaseIndex+1, currentTime);

			currentTime			= 0;
			blackLastMoveTime	= 0;
			orangeLastMoveTime	= 0;
			blackLastMovePos	= 1;
			orangeLastMovePos	= 1;
		}


	} while (FALSE);

	//printf("Done !!!\n");

	if (pInputFile)
	{
		fclose(pInputFile);
	}
	
	return 0;
}

