// jam1-tictactoe.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//------------------------------------------------------------------------------------------------
enum eBoardResult {
	BR_X_WON,
	BR_O_WON,
	BR_DRAW,
	BR_IN_PROGRESS
};

//------------------------------------------------------------------------------------------------
char solveBoard( char _board[4][4] )
{
	bool bFull = true;

	for(int i=0;i<4;i++)
	{
		//-- row
		{
			char candidateColor = 'T';
			int j=0;
			while(j<4)
			{
				char elem = _board[i][j];
				if      ( elem == '.' )				{	bFull = false;	break;			}
				else if ( candidateColor == 'T'  )	{   candidateColor = elem;			}
				else if ( elem == 'T'            )  {   /* keeps with same candidate */ }
				else if ( elem != candidateColor )  {   break;							}
				j++;
			}
			if( j == 4 ) 
				return candidateColor;
		}
		//-- column
		{
			char candidateColor = 'T';
			int j=0;
			while(j<4)
			{
				char elem = _board[j][i];
				if      ( elem == '.' )				{	bFull = false;	break;			}
				else if ( candidateColor == 'T'  )	{   candidateColor = elem;			}
				else if ( elem == 'T'            )  {   /* keeps with same candidate */ }
				else if ( elem != candidateColor )  {   break;							}
				j++;
			}
			if( j == 4 ) 
				return candidateColor;
		}
	}
	for(int i=0;i<2;i++) 
	{
		//-- diag
		{
			char curColor = _board[0][i];
			char candidateColor = 'T';
			int j=0;
			while(j<4)
			{
				char elem = i==0 ? _board[j][j] : _board[3-j][j];
				if      ( elem == '.' )				{	bFull = false;	break;			}
				else if ( candidateColor == 'T'  )	{   candidateColor = elem;			}
				else if ( elem == 'T'            )  {   /* keeps with same candidate */ }
				else if ( elem != candidateColor )  {   break;							}
				j++;
			}
			if( j == 4 ) 
				return candidateColor;
		}
	}

	return bFull ? 'T' : '.';
}

//------------------------------------------------------------------------------------------------
int main(int argc, char* argv[])
{
	FILE *in = argc>1 ? fopen(argv[1],"r") : stdin;
	FILE *out= argc>2 ? fopen(argv[2],"w")  : stdout;

	if(in==NULL || out==NULL)
	{
		printf("Error in params");
		return 0;
	}

	//-- read solutions
	int nSolutions = 0;	
	int parse= fscanf(in,"%d\n",&nSolutions);
	{
		for(int s=0;s<nSolutions;s++)
		{
			//-- read board
			char board[4][4];
			for(int i=0;i<4;i++)
				fscanf(in,"%c%c%c%c\n",&(board[i][0]),&(board[i][1]),&(board[i][2]),&(board[i][3]));
			fscanf(in,"\n");

			//-- process board
			char res=solveBoard(board);

			//-- register output
			fprintf(out,"Case #%d: %s\n",s+1, (res == 'X') ? "X won" :
											(res == 'O') ? "O won" :
											(res == 'T') ? "Draw"  : "Game has not completed" );
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}

