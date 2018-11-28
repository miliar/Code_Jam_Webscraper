#include <fstream>
#include <string>
#include "stdlib.h"
#include <math.h>
#include <iostream>

using namespace std;

//PROBLEM LIMITS
#define LIMIT_R = 6
#define LIMIT_C = 6

string cutNext (string line, int& start, string delimiter);

int main (void)
{
	//make input/output streams
	fstream input ("A-small-attempt0.in");
	fstream output ("output.out");

	//make string to hold the contents of each line
	string line;

	//get the number of cases
	getline (input, line);
	int cases = atoi (line.c_str());
	
	//go through each case
	for (int caseno = 1; caseno <= cases; caseno++)
	{
		getline (input, line);
		int startPos = 0;
		string word = cutNext(line,startPos, " ");
		int R = atoi (word.c_str());

		word = cutNext(line,startPos, " ");
		int C = atoi (word.c_str());

		int tiles[6][6];

		for (int i = 0; i < R; i++)
		{
			getline (input, line);
			for (int ii = 0; ii < C; ii++)
			{
				char colour = line[ii];
				int col;
				switch (colour)
				{
				case '.':
					col = 0;
					break;
				case '#':
					col = 1;
					break;
				}

				tiles[ii][i] = col;
			}
		}
		

		bool possible = true;
		for (int i = 0; i < R; i++)
		{
			for (int ii = 0; ii < C; ii++)
			{
				if (tiles[ii][i] == 0  || tiles[ii][i] == 2 || tiles[ii][i] == 3)
					continue;
				else
				{
					if (tiles[ii+1][i] == 1 && tiles[ii+1][i+1] == 1 && tiles[ii][i+1] == 1)
					{
						tiles[ii][i] = 2;
						tiles[ii+1][i] = 3;
						tiles[ii][i+1] = 3;
						tiles[ii+1][i+1] = 2;
					}

					else
					{
						possible = false;
						break;
					}
				}
			}
		}

		output << "Case #" << caseno <<": " << endl;
		if (!possible)
			output << "Impossible" << endl;
		else
		{
			for (int i = 0; i < R; i++)
			{
				for (int ii = 0; ii < C; ii++)
				{
					switch (tiles[ii][i])
					{
					case 0:
						output << '.';
						break;
					case 2:
						output << '/';
						break;
					case 3:
						output << "\\";
						break;
					}
					
				}
				output << endl;
			}
		}
	}



	//close files and return
	input.close();
	output.close();
	return 0;
}

//returns the next string after the start till the delimiter
string cutNext (string line, int& start, string delimiter)
{
	int pos;

	pos = line.find (delimiter, start);
	string cut = line.substr (start,pos-start);
	start = pos+1;

	return cut;
}