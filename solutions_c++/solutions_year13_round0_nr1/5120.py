#include "stdio.h"
#include "stdlib.h"

void main()
{
	int i,j,k;
	int TestCases;
	FILE *fInPtr  = NULL;
	FILE *fOutPtr = NULL;
	char Table[4][4];
	char ReadChar;
	int RowCase ,ColCase,DiagCase1,DiagCase2;
	int bFoundMatch = 0;

	fInPtr  = fopen("D:\\Input.txt","rb");
	if(NULL == fInPtr)
	{
		printf("Cannot open Input file\n");
		//return;
	}
	fOutPtr = fopen("D:\\Output.txt","wb");
	if(NULL == fOutPtr)
	{
		printf("Cannot open output file\n");
		//return;
	}

	//Read no of test cases in input file once
	fscanf(fInPtr,"%d\n",&TestCases);


	//Loop for test cases and print output for each
	for(i = 1; i <= TestCases; i++)
	{
		// Reset the Found Match Flag
		bFoundMatch = 0;

		//Read the input for present case and save in Table[][]
		for (j = 0; j < 4; j++)
		{
			for(k = 0; k < 4; k++)
			{
				//Read the char
				fscanf(fInPtr,"%c",&ReadChar);
				Table[j][k]=ReadChar;
			}//k
			fscanf(fInPtr,"\n");
		}//j

		
		//the table is full
		//#####################check for "X won" case START
		RowCase = ColCase = DiagCase1 = DiagCase2= 0;
		for (j = 0; j < 4; j++)
		{
			for(k = 0; k < 4; k++)
			{
				//count for Row
				if(Table[j][k] == 'X' || Table[j][k] == 'T')
					RowCase++;

				//count for Col
				if(Table[k][j] == 'X' || Table[k][j] == 'T')
					ColCase++;

				//count for Diag1
				if( (j == k)  && (Table[j][k] == 'X' || Table[j][k] == 'T') )
					DiagCase1++;

				//count for Diag2
				if( (j == 3-k)  && (Table[j][k] == 'X' || Table[j][k] == 'T') )
					DiagCase2++;

			}//k

			// check if any of the count is 4? if yes then X won
			if( RowCase == 4 || ColCase == 4 || DiagCase1 == 4 || DiagCase2 == 4)
			{
				fprintf(fOutPtr,"Case #%d: X won\n",i);
				bFoundMatch = 1;
				break; //break from the j loop and continue with next test case
			}
			RowCase = ColCase = 0;
		}//j

		// check if bFoundMatch is set. if yes then goto next text case
		if( bFoundMatch == 1)
		{			
			continue; //go for next test case
		}
		//#####################check for "X won" case END

	

		//######################check for "O won" case START
		RowCase = ColCase = DiagCase1 = DiagCase2= 0;
		for (j = 0; j < 4; j++)
		{
			for(k = 0; k < 4; k++)
			{
				//count for Row
				if(Table[j][k] == 'O' || Table[j][k] == 'T')
					RowCase++;

				//count for Col
				if(Table[k][j] == 'O' || Table[k][j] == 'T')
					ColCase++;

				//count for Diag1
				if( (j == k)  && (Table[k][j] == 'O' || Table[k][j] == 'T') )
					DiagCase1++;

				//count for Diag2
				if( (j == 3-k)  && (Table[j][k] == 'O' || Table[j][k] == 'T') )
					DiagCase2++;

			}//k

			// check if any of the count is 4? if yes then X won
			if( RowCase == 4 || ColCase == 4 || DiagCase1 == 4 || DiagCase2 == 4)
			{
				fprintf(fOutPtr,"Case #%d: O won\n",i);
				bFoundMatch = 1;
				break; //break from the j loop and continue with next test case
			}
			RowCase = ColCase = 0;
		}//j

		// check if bFoundMatch is set. if yes then goto next text case
		if( bFoundMatch == 1)
		{			
			continue; //go for next test case
		}
		//######################check for "O won" case END


		//######################check for "Draw" case START
		for (j = 0; j < 4; j++)
		{
			for(k = 0; k < 4; k++)
			{
				if(Table[j][k] == '.')
				{
					bFoundMatch = 1;
					break;
				}
			}//k
			if( bFoundMatch == 1)
			{
				break;// found a '.' whch means game is still on
			}
		}//j
		
		if(bFoundMatch == 0) // all the spaces are filled and no one one so its a draw
		{
            fprintf(fOutPtr,"Case #%d: Draw\n",i);
			continue; //go for next test case
		}
		else
		{
            fprintf(fOutPtr,"Case #%d: Game has not completed\n",i);
		}
		//######################check for "Draw" case END


	}//for(TestCases)


	return;

}