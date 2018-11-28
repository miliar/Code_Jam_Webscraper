#include <iostream.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

#define INFILE	"A-large.in"
#define OUTFILE	"A-large.out"

bool Compare(char ASquare, char BSquare)
{
	bool blEqual = false;
	
	if ('.' == ASquare) return false;
	if ('.' == BSquare) return false;
	if ('T' == ASquare) return true;
	if ('T' == BSquare) return true;

	return (ASquare == BSquare);
}

char WinnerIs(char pSquares[16])
{
	char Winner = 'd';
	int Pos[10][4];
	int i = 0, j = 0;
	bool blCompare = false;
	
	for (i=0; i<4; i++) {
		for (j=0; j<4; j++) {
			Pos[i][j] = j + (4 * i);
		}
	}
	for (i=4; i<8; i++) {
		for (j=0; j<4; j++) {
			Pos[i][j] = i - 4 + (4 * j);
		}
	}
	for (j=0; j<4; j++) {
		Pos[8][j] = j * 5;
		Pos[9][j] = 3 * (j + 1);
	}

	for (i=0; i<10; i++) {
		/* Check each row */
		if ('T' != pSquares[Pos[i][0]]) {
			for (j=1; j<4; j++) {
				blCompare = Compare(pSquares[Pos[i][0]], pSquares[Pos[i][j]]);
				if (false == blCompare) break;
			}
		} else {
			for (j=0; j<3; j++) {
				blCompare = Compare(pSquares[Pos[i][3]], pSquares[Pos[i][j]]);
				if (false == blCompare) break;
			}
		}
		if (true == blCompare) {
			return ('T' == pSquares[Pos[i][0]]) ? 
				   pSquares[Pos[i][1]] : pSquares[Pos[i][0]];
		}
	}
	
	for (i=0; i<16; i++) {
		if ('.' == pSquares[i]) return 'n';
	}

	return Winner;
}

int main(int argc, char *argv[])
{
	FILE *infile, *outfile;
	int i = 0, j = 0, k = 0;
	int NumOfGame = 0;
	char CurChar;
	char Winner;
	char pSquares[16];

	if ( (infile = fopen(INFILE, "r")) == NULL ) {
		printf("can't open input file\n");
		return -1;
	} else if( (outfile = fopen(OUTFILE, "w+")) == NULL ) {
		printf("can't open output file\n");
		return -1;
	}

	while ((EOF != (CurChar = fgetc(infile))) && 
		   ('\n' != CurChar)) {
		NumOfGame = NumOfGame * 10 + (CurChar - '0');
 	}
 	printf("NumOfGame : %d\n", NumOfGame);
 	
 	/* Read Game by Game */
 	for (i=0; i<NumOfGame; i++) {
		/* Read a single game, Case #(i+1) */
		k = 0;
		for (j=0; j<21; j++) {
			if ((EOF != (CurChar = fgetc(infile))) &&
				('\n' != CurChar)) {
				pSquares[k] = CurChar;
				k++;
			}
		}
		
		/* Find the winner */
		Winner = WinnerIs(pSquares);

		if (('X' == Winner) || ('O' == Winner)) {
			fprintf(outfile, "Case #%d: %c won", i+1, Winner);
		} else if ('d' == Winner) {
			fprintf(outfile, "Case #%d: Draw", i+1);
		} else if ('n' == Winner) {
			fprintf(outfile, "Case #%d: Game has not completed", i+1);
		} else {
			fprintf(outfile, "Case #%d: Unknown error!!!!!!!!!!! [%c]", i+1, Winner);
		}
		if (999 != i) {
			fprintf(outfile, "\n");
		}
	}

    fclose(infile);
    fclose(outfile);
    
	return 0;
}
