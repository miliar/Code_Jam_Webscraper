// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;

void solveMap(char* map, FILE* fout, int index)
{
	bool Xwon = false;
	bool Owon = false;

	int totalUnFinished = 0;

	// COLUMNS
	for (int x = 0; x < 4; x++)
	{
		int nNumX = 0;
		int nNumO = 0;

		for (int y = 0; y < 4; y++)
		{
			switch (map[y*4+x])
			{
			case 'X':
				nNumX++;
				break;
			case 'O':
				nNumO++;
				break;
			case 'T':
				nNumX++;
				nNumO++;
				break;
			case '.':
				totalUnFinished++;
				break;
			}
		}

		if (nNumX == 4)
			Xwon = true;
		else if (nNumO == 4)
			Owon = true;
	}

	// LINES
	for (int y = 0; y < 4; y++)
	{
		int nNumX = 0;
		int nNumO = 0;

		for (int x = 0; x < 4; x++)
		{
			switch (map[y*4+x])
			{
			case 'X':
				nNumX++;
				break;
			case 'O':
				nNumO++;
				break;
			case 'T':
				nNumX++;
				nNumO++;
				break;
			case '.':
				break;
			}
		}

		if (nNumX == 4)
			Xwon = true;
		else if (nNumO == 4)
			Owon = true;
	}

	// DIAGONALS

	int nNumX = 0;
	int nNumO = 0;

	for (int i = 0; i < 4; i++)
	{
		switch (map[i*4+i])
		{
		case 'X':
			nNumX++;
			break;
		case 'O':
			nNumO++;
			break;
		case 'T':
			nNumX++;
			nNumO++;
			break;
		case '.':
			break;
		}
	}

	if (nNumX == 4)
		Xwon = true;
	else if (nNumO == 4)
		Owon = true;

	// LAST DIAGONAL
	nNumX = 0;
	nNumO = 0;

	for (int i = 0; i < 4; i++)
	{
		switch (map[i*4+(3-i)])
		{
		case 'X':
			nNumX++;
			break;
		case 'O':
			nNumO++;
			break;
		case 'T':
			nNumX++;
			nNumO++;
			break;
		case '.':
			break;
		}
	}

	if (nNumX == 4)
		Xwon = true;
	else if (nNumO == 4)
		Owon = true;

	// OUTPUT

	if (Xwon)
		fprintf(fout, "Case #%d: X won\n", index);
	else if (Owon)
		fprintf(fout, "Case #%d: O won\n", index);
	else if (totalUnFinished != 0)
		fprintf(fout, "Case #%d: Game has not completed\n", index);
	else
		fprintf(fout, "Case #%d: Draw\n", index);
}

int _tmain(int argc, _TCHAR* argv[])
{
	char buff[1024];
	string fileToOpen = "input.txt";
	string fileToWrite = "output.txt";

	FILE* fp = fopen (fileToOpen.c_str(), "rb");
	if (!fp)
    {
		printf("Error: could not open file '%s'!\n", fileToOpen.c_str());
		return 0;
    }
	FILE* fout = fopen (fileToWrite.c_str(), "w");

	int numberOfTestCases;

	fgets(buff, sizeof (buff), fp);
	sscanf(buff, "%d", &numberOfTestCases);

	int index = 1;

	while (numberOfTestCases > 0)
	{
		char map[16];

		for (int i = 0; i < 4; i++)
		{
			fgets(buff, sizeof (buff), fp);
			sscanf(buff, "%c%c%c%c", &map[0 + i*4], &map[1 + i*4], &map[2 + i*4], &map[3 + i*4]);
		}

		// We have the map, we solve it

		solveMap(map, fout, index);

		// Ugly get rid of line jump
		fgets(buff, sizeof (buff), fp);
		sscanf(buff, "%c", &map[1]);

		numberOfTestCases--;
		index++;
	}
}

