// Rob Keim
// Google Code Jam - Qualifying Round

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

#define MAX_SIZE 100
#define MAX_BASINS 26

string tmp;
int numCases;
int maxHeight;
int maxWidth;
int curBasin;

bool filledGrid[MAX_SIZE][MAX_SIZE];
int inGrid[MAX_SIZE][MAX_SIZE];
int numGrid[MAX_SIZE][MAX_SIZE];
char dirGrid[MAX_SIZE][MAX_SIZE];
char finalGrid[MAX_SIZE][MAX_SIZE];

char basinTable[MAX_BASINS];

void checkNeighbors(int height, int width)
{	
	if (height - 1 >= 0 && !filledGrid[height - 1][width])
	{
		if (dirGrid[height - 1][width] == 's')
		{
			filledGrid[height - 1][width] = 1;
			numGrid[height - 1][width] = curBasin;
			checkNeighbors(height - 1, width);
		}
	}
	if (width - 1 >= 0 && !filledGrid[height][width - 1])
	{
		if (dirGrid[height][width - 1] == 'e')
		{
			filledGrid[height][width - 1] = 1;
			numGrid[height][width - 1] = curBasin;
			checkNeighbors(height, width - 1);
		}
	}	
	if (width + 1 < maxWidth && !filledGrid[height][width + 1])
	{
		if (dirGrid[height][width + 1] == 'w')
		{
			filledGrid[height][width + 1] = 1;
			numGrid[height][width + 1] = curBasin;
			checkNeighbors(height, width + 1);
		}
	}
	if (height + 1 < maxHeight && !filledGrid[height + 1][width])
	{
		if (dirGrid[height + 1][width] == 'n')
		{
			filledGrid[height + 1][width] = 1;
			numGrid[height + 1][width] = curBasin;
			checkNeighbors(height + 1, width);
		}
	}

	return;
}

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	fin >> numCases;

	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		// Read in dimensions for the grid
		fin >> maxHeight >> maxWidth;
		
		// Read in the grid
		for (int height = 0; height < maxHeight; height++)
		{
			for (int width = 0; width < maxWidth; width++)
			{
				fin >> inGrid[height][width];
				numGrid[height][width] = -1;
				filledGrid[height][width] = 0;
			}
		}
		
		// Determine the direction each grid square is going to flow
		for (int height = 0; height < maxHeight; height++)
		{
			for (int width = 0; width < maxWidth; width++)
			{
				char dir = 'x';
				int min = inGrid[height][width];
				if (height - 1 >= 0 && inGrid[height - 1][width] < min)
				{
					dir = 'n';
					min = inGrid[height - 1][width];
				}
				if (width - 1 >= 0 && inGrid[height][width - 1] < min)
				{
					dir = 'w';
					min = inGrid[height][width - 1];
				}	
				if (width + 1 < maxWidth && inGrid[height][width + 1] < min)
				{
					dir = 'e';
					min = inGrid[height][width + 1];
				}
				if (height + 1 < maxHeight && inGrid[height + 1][width] < min)
				{
					dir = 's';
					min = inGrid[height + 1][width];
				}
				dirGrid[height][width] = dir;
			}
		}
		
		curBasin = 0;

		for (int height = 0; height < maxHeight; height++)
		{
			for (int width = 0; width < maxWidth; width++)
			{
				if (dirGrid[height][width] == 'x')
				{
					numGrid[height][width] = curBasin;
					checkNeighbors(height, width);
					filledGrid[height][width] = 1;
					curBasin++;
				}
			}
		}	

		char curLetter = 'a';
		
		for (int i = 0; i < 26; i++)
		{
			basinTable[i] = ' ';
		}

		//cout << "Case #" << curCase << ":\n";
		fout << "Case #" << curCase << ":\n";
		for (int height = 0; height < maxHeight; height++)
		{
			for (int width = 0; width < maxWidth; width++)
			{
				int curVal = numGrid[height][width];
				if (basinTable[curVal] == ' ')
				{
					basinTable[curVal] = curLetter;
					curLetter++;
				}
				finalGrid[height][width] = basinTable[curVal];
				if (width == 0)
				{
					//cout << finalGrid[height][width];
					fout << finalGrid[height][width];
				}
				else
				{
					//cout << " " << finalGrid[height][width];
					fout << " " << finalGrid[height][width];
				}
			}
			//cout << endl;
			fout << endl;
		}
	}

	return 0;
}

