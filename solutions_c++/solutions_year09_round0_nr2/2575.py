#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cctype>

using namespace std;


enum direction {HERE, NORTH, WEST, EAST, SOUTH};

struct data{
	int alt;
	char letter;
	direction dir;
};

void checkNeighbors(vector<vector<data> >& alts, int H, int W)
{
	if(H != 0 && alts[H-1][W].letter == 0 && alts[H-1][W].dir == SOUTH)
	{
		alts[H-1][W].letter = alts[H][W].letter;
		checkNeighbors(alts, H-1, W);
	}
	if(W != 0 && alts[H][W-1].letter == 0 && alts[H][W-1].dir == EAST)
	{
		alts[H][W-1].letter = alts[H][W].letter;
		checkNeighbors(alts, H, W-1);
	}
	if(W+1 != alts[0].size() && alts[H][W+1].letter == 0 && alts[H][W+1].dir == WEST)
	{
		alts[H][W+1].letter = alts[H][W].letter;
		checkNeighbors(alts, H, W+1);
	}
	if(H+1 != alts.size() && alts[H+1][W].letter == 0 && alts[H+1][W].dir == NORTH)
	{
		alts[H+1][W].letter = alts[H][W].letter;
		checkNeighbors(alts, H+1, W);
	}

	switch(alts[H][W].dir)
	{
		case SOUTH:
			if(alts[H+1][W].letter == 0)
			{
				alts[H+1][W].letter = alts[H][W].letter;
				checkNeighbors(alts, H+1, W);
			}
			break;
		case NORTH:
			if(alts[H-1][W].letter == 0)
			{
				alts[H-1][W].letter = alts[H][W].letter;
				checkNeighbors(alts, H-1, W);
			}
			break;
		case WEST:
			if(alts[H][W-1].letter == 0)
			{
				alts[H][W-1].letter = alts[H][W].letter;
				checkNeighbors(alts, H, W-1);
			}
			break;
		case EAST:
			if(alts[H][W+1].letter == 0)
			{
				alts[H][W+1].letter = alts[H][W].letter;
				checkNeighbors(alts, H, W+1);
			}
			break;
		default:
			break;
	}
}


int main()
{
  //Read in the file
  ifstream inTest;
  inTest.open("B-large.in.txt");//"InputFile.txt");
  string line;

	int numTests;

	inTest >> numTests;

  //Open file for output
  ofstream outTest;
  outTest.open("resultNN.txt");

  for(int currTest=1; currTest <= numTests; currTest++) //Each test
  {
		int H, W;
		inTest >> H >> W;

		vector<vector<data> > altitudes(H, vector<data>(W));

		for(int i=0; i< H; i++)
		{
			for(int j=0; j<W; j++)
			{
				inTest >> altitudes[i][j].alt;
				altitudes[i][j].letter = 0;
			}
		}

		for(int i=0; i< H; i++)
		{
			for(int j=0; j<W; j++)
			{
				int minAlt = altitudes[i][j].alt;

				if(i!=0 && minAlt > altitudes[i-1][j].alt)
				{
					altitudes[i][j].dir = NORTH;
					minAlt = altitudes[i-1][j].alt;
				}
				if(j!=0 && minAlt > altitudes[i][j-1].alt)
				{
					altitudes[i][j].dir = WEST;
					minAlt = altitudes[i][j-1].alt;
				}
				if(j+1!=W && minAlt > altitudes[i][j+1].alt)
				{
					altitudes[i][j].dir = EAST;
					minAlt = altitudes[i][j+1].alt;
				}
				if(i+1!=H && minAlt > altitudes[i+1][j].alt)
				{
					altitudes[i][j].dir = SOUTH;
					minAlt = altitudes[i+1][j].alt;
				}
				if(minAlt == altitudes[i][j].alt)
					altitudes[i][j].dir = HERE;
			}
		}

		char currLet = 'a';

		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				if(altitudes[i][j].letter == 0)
				{
					altitudes[i][j].letter = currLet++;

					checkNeighbors(altitudes, i, j);
				}
			}
		}

		outTest << "Case #" << currTest << ": " << endl;
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				outTest << altitudes[i][j].letter << " ";
			}
			outTest << endl;
		}
  }
  return 1;
}


