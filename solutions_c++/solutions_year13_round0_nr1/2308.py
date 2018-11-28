/*******************************************************************************
*	GoogleCodeJamQualificationA
*	Christoper Mayer, aka Quantum Anemone
*******************************************************************************/

/*
Problem


*/

#include	<Windows.h>
#include	<stdio.h>
#include	<conio.h>

FILE	*inputFile;
FILE	*outputFile;

void solve(void)
{
	char	board[4][4], c;
	int		x, y, nO, nX, nT;

	//printf("\n");
	for (x=0; x<4; x++)
	{
		for (y=0; y<4; y++)
		{
			c = fgetc(inputFile);
			board[x][y] = c;
			if ((c != 'X') && (c != 'O') && (c != '.') && (c != 'T'))
				y--;
		}
	}

	//for (int x=0; x<4; x++)
	//{
	//	for (int y=0; y<4; y++)
	//		printf_s("%c", board[x][y]);
	//	printf("\n\n");
	//}

	// check rows
	for (x=0; x<4; x++)
	{
		nX = nO = nT = 0;
		for (y=0; y<4; y++)
		{
			if (board[x][y] == '.')	break;
			else if (board[x][y] == 'X')	nX++;
			else if (board[x][y] == 'O')	nO++;
			else if (board[x][y] == 'T')	nT++;
		}
		if (nX + nT == 4)
		{
			printf_s("X won\n");
			fprintf_s(outputFile, "X won\n");
			return;
		}
		if (nO + nT == 4)
		{
			printf_s("O won\n");
			fprintf_s(outputFile, "O won\n");
			return;
		}
	}
	// check columns
	for (y=0; y<4; y++)
	{
		nX = nO = nT = 0;
		for (x=0; x<4; x++)
		{
			if (board[x][y] == '.')	break;
			else if (board[x][y] == 'X')	nX++;
			else if (board[x][y] == 'O')	nO++;
			else if (board[x][y] == 'T')	nT++;
		}
		if (nX + nT == 4)
		{
			printf_s("X won\n");
			fprintf_s(outputFile, "X won\n");
			return;
		}
		if (nO + nT == 4)
		{
			printf_s("O won\n");
			fprintf_s(outputFile, "O won\n");
			return;
		}
	}
	// check diagonal down
	nX = nO = nT = 0;
	for (x=0; x<4; x++)
	{
		if (board[x][x] == '.')	break;
		else if (board[x][x] == 'X')	nX++;
		else if (board[x][x] == 'O')	nO++;
		else if (board[x][x] == 'T')	nT++;
	}
	if (nX + nT == 4)
	{
		printf_s("X won\n");
		fprintf_s(outputFile, "X won\n");
		return;
	}
	if (nO + nT == 4)
	{
		printf_s("O won\n");
		fprintf_s(outputFile, "O won\n");
		return;
	}
	// check diagonal up
	nX = nO = nT = 0;
	for (x=0; x<4; x++)
	{
		if (board[x][3-x] == '.')	break;
		else if (board[x][3-x] == 'X')	
			nX++;
		else if (board[x][3-x] == 79)	
			nO++;
		else if (board[x][3-x] == 'T')	
			nT++;
	}
	if (nX + nT == 4)
	{
		printf_s("X won\n");
		fprintf_s(outputFile, "X won\n");
		return;
	}
	if (nO + nT == 4)
	{
		printf_s("O won\n");
		fprintf_s(outputFile, "O won\n");
		return;
	}
	// check for draw or completed
	for (x=0; x<4; x++)
	{
		for (y=0; y<4; y++)
		{
			if (board[x][y] == '.')
			{
				printf_s("Game has not completed\n");
				fprintf_s(outputFile, "Game has not completed\n");
				return;
			}
		}
	}
	printf_s("Draw\n");
	fprintf_s(outputFile, "Draw\n");
}

void main(int argc, char *argv[])
{
	unsigned __int64	frequency, t0, t1;

	QueryPerformanceCounter((LARGE_INTEGER *)&t0);

	printf_s("GoogleCodeJamQualificationA\n");
	printf_s("Christoper Mayer, aka Quantum Anemone\n\n");

	// create output file
	char	outputFilename[256];
	sprintf_s(outputFilename, "%s.out", argv[1]);
	fopen_s(&outputFile, outputFilename, "w");
	printf_s("This program may output debug info to the console.\n");
	printf_s("The official output is written to the file %s.\n\n", outputFilename);

	// open input file
	fopen_s(&inputFile, argv[1], "r");

	// how many cases?
	int	nCases;
	fscanf_s(inputFile, "%d", &nCases);

	// solve them!
	for (int i=1; i<=nCases; i++)
	{
		printf_s("Case #%d: ", i);
		fprintf_s(outputFile, "Case #%d: ", i);
		solve();
	}

	// clean up
	fclose(inputFile);
	fclose(outputFile);

	QueryPerformanceCounter((LARGE_INTEGER *)&t1);
	QueryPerformanceFrequency((LARGE_INTEGER *)&frequency);
	printf_s("\nAll finished in %f seconds.\n", (t1-t0)/(float)frequency);
	_getch();
}
