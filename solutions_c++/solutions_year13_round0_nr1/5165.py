#include <stdio.h>

#define BUFF_LEN	10

#define BOARD_SIZE	4

#define STATE_INIT	0
#define STATE_X		1
#define STATE_O		2
#define STATE_NONE	3

#define TILE_EMPTY	0
#define TILE_X		1
#define TILE_O		2
#define TILE_WILD	3

#define CHAR_TILE_EMPTY		'.'
#define CHAR_TILE_X			'X'
#define CHAR_TILE_O			'O'
#define CHAR_TILE_WILD		'T'



FILE *fin, *fout;
int lins[BOARD_SIZE], cols[BOARD_SIZE], pDiag, sDiag;

int Trans[4][4] = {	// Transition[STATE][TILE]
		{STATE_NONE, STATE_X,	 STATE_O, 	 STATE_INIT},
		{STATE_NONE, STATE_X,	 STATE_NONE, STATE_X},
		{STATE_NONE, STATE_NONE, STATE_O,	 STATE_O},
		{STATE_NONE, STATE_NONE, STATE_NONE, STATE_NONE}
	};


	
int char_to_tile (char c)
{
	int res = -1;
	
	if (c == CHAR_TILE_EMPTY)
		res = TILE_EMPTY;
	else if (c == CHAR_TILE_X)
		res = TILE_X;
	else if (c == CHAR_TILE_O)
		res = TILE_O;
	else if (c == CHAR_TILE_WILD)
		res = TILE_WILD;
	
	return res;
}

void solve ()
{
	int itest,ntests;
	int i,j,tile,outcome;
	bool incomp;
	const char *res;
	char str[BUFF_LEN];
	
	fgets (str,BUFF_LEN,fin);
	sscanf (str,"%d",&ntests);	
	for (itest = 1; itest <= ntests; itest++)
	{
		// housekeeping
		for (i = 0; i < BOARD_SIZE; i++)
		{
			lins[i] = STATE_INIT;
			cols[i] = STATE_INIT;
		}
		pDiag = STATE_INIT;
		sDiag = STATE_INIT;
		incomp = false;
		res = NULL;
		outcome = STATE_NONE;
	
		// read and solve
		for (i = 0; i < BOARD_SIZE; i++)
		{
			fgets (str,10,fin);
			for (j = 0; j < BOARD_SIZE; j++)
			{
				tile = char_to_tile(str[j]);
				if (tile == TILE_EMPTY)
					incomp = true;
				
				lins[i] = Trans[lins[i]][tile];
				cols[j] = Trans[cols[j]][tile];
				if (i == j) 				// principal diag
					pDiag = Trans[pDiag][tile];
				if (i+j == BOARD_SIZE-1)	// secondary diag
					sDiag = Trans[sDiag][tile];
			}
		}
		fgets (str,10,fin);
		// determine outcome
		for (i=0; i<BOARD_SIZE; i++)
		{
			if (lins[i] == STATE_X || cols[i] == STATE_X)
				outcome = STATE_X;
			if (lins[i] == STATE_O || cols[i] == STATE_O)
				outcome = STATE_O;
		}
		if (sDiag == STATE_X || pDiag == STATE_X)
			outcome = STATE_X;
		if (sDiag == STATE_O || pDiag == STATE_O)
			outcome = STATE_O;
		
		if (outcome == STATE_X)
			res = "X won";
		else if (outcome == STATE_O)
			res = "O won";
		else if (incomp)
			res = "Game has not completed";
		else
			res = "Draw";
		
		// report
		fprintf (fout,"Case #%d: %s\n",itest,res);
	}
}

int main (int argc, char **args)
{
	if (argc != 3)
	{
		printf ("Usage:\n\t%s <file_in> <file_out>\n",args[0]);
		return 1;
	}
	
	fin = fopen (args[1],"r");
	fout = fopen (args[2],"w");
	
	if (fin == NULL || fout == NULL)
	{
		printf ("Something's wrong with the in/out files!\n");
		return 1;
	}
	
	solve();
	
	fclose(fin);
	fclose(fout);
	return 0;
}

