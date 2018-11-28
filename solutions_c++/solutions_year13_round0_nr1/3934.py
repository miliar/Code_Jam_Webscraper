#include "stdio.h"
#include "stdlib.h"
#include "string.h"

void SolveCase(char arr[4][5], int caseNum)
{
	// Check row wise
	char prevChar;
	bool gameover = true;
	for(int i = 0; i<4; i++)
	{
		prevChar = 'I';		// some invalid character
		int j;
		for(j = 0; j<4; j++)
		{
			if(arr[i][j] == '.')
			{
				gameover = false;
				break;
			}

			if(prevChar == 'I' && arr[i][j] != 'T')
			{
				prevChar = arr[i][j];
				continue;
			}

			if(arr[i][j] == prevChar || arr[i][j] == 'T')
				continue;
			else 
				break;
		}

		if(j == 4)	// we didnt break out prematurely
		{
			printf("Case #%d: %c won\n", caseNum, prevChar);
			return;
		}
	}

	// Check columns
	for(int j = 0; j<4; j++)
	{
		prevChar = 'I';		// some invalid character
		int i;
		for(i = 0; i<4; i++)
		{
			if(arr[i][j] == '.')
			{
				gameover = false;
				break;
			}

			if(prevChar == 'I' && arr[i][j] != 'T')
			{
				prevChar = arr[i][j];
				continue;
			}

			if(arr[i][j] == prevChar || arr[i][j] == 'T')
				continue;
			else 
				break;
		}

		if(i == 4)	// we didnt break out prematurely
		{
			printf("Case #%d: %c won\n", caseNum, prevChar);
			return;
		}
	}

	// check diagonals..
	char firstChar = arr[0][0] == 'T' ? arr[1][1]: arr[0][0];
	if((arr[1][1] == firstChar || arr[1][1] == 'T') && 
		(arr[2][2] == firstChar || arr[2][2] == 'T') && 
		(arr[3][3] == firstChar || arr[3][3] == 'T') && firstChar != '.')
	{
		printf("Case #%d: %c won\n", caseNum, firstChar);
		return;
	}

	firstChar = arr[0][3] == 'T' ? arr[1][2]: arr[0][3];
	if((arr[1][2] == firstChar || arr[1][2] == 'T') && 
		(arr[2][1] == firstChar || arr[2][1] == 'T') && 
		(arr[3][0] == firstChar || arr[3][0] == 'T') && firstChar != '.')
	{
		printf("Case #%d: %c won\n", caseNum, firstChar);
		return;
	}

	if(!gameover)
		printf("Case #%d: Game has not completed\n", caseNum);
	else
		printf("Case #%d: Draw\n", caseNum);	
}

// ---------------------------------------------------------------------------------
// Main Function
// ---------------------------------------------------------------------------------

void main ()
{
   int T;
   scanf("%d", &T);

   for(int k = 1; k<=T; k++)
   {
	   char arr[4][5];
	   for(int i = 0; i<4; i++)
	   {
		   scanf("%s", &arr[i]);
	   }

	   
	   SolveCase(arr, k);
	   scanf("%c", &arr[0][0]); // for the extra newline
   }
}
