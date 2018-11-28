#include <fstream>
#include <string>
#include "stdlib.h"

using namespace std;

//PROBLEM LIMITS
#define LIMIT_C 36
#define LIMIT_D 28
#define LIMIT_N 100

string cutNext (string line, int& start, string delimiter);

int main (void)
{
	//make input/output streams
	fstream input ("B-large.in");
	fstream output ("output.out");

	//make string to hold the contents of each line
	string line;

	//get the number of cases
	getline (input, line);
	int cases = atoi (line.c_str());
	
	//go through each case
	for (int caseno = 1; caseno <= cases; caseno++)
	{
		int startPos = 0;//used for cutNext()
		getline (input, line);
		string v;
		//get number of combinations C
		v = cutNext (line, startPos, " ");
		int C = atoi (v.c_str());

		//store all possible combinations
		char combos[3][LIMIT_C];
		for (int i = 0; i < C; i++)
		{
			v = cutNext (line, startPos, " ");
			combos[0][i] = v[0];
			combos[1][i] = v[1];
			combos[2][i] = v[2];
		}

		//get number of opposing elements
		v = cutNext (line, startPos, " ");
		int D = atoi (v.c_str());

		//store all possible oppositions
		char opposes [2][LIMIT_D];
		for (int i = 0; i < D; i++)
		{
			v = cutNext (line, startPos, " ");
			opposes[0][i] = v[0];
			opposes[1][i] = v[1];
		}

		//get number of invoked elements
		v = cutNext (line, startPos, " ");
		int N = atoi (v.c_str());

		//store the list of invoked elements
		char elements [LIMIT_N];
		v = cutNext (line, startPos, " ");
		for (int i = 0; i < v.length(); i++)
		{
			elements[i] = v[i];
		}

		//invoke each element sequentially
		for (int i = 0; i < N; i++)
		{
			char combine = '.';
			bool oppose = false;
			//COMBINATIONS
			if (i != N-1)//if not the last element
			{
				//check if the element combines with the one before it
				char x = elements[i];
				char y = elements[i+1];

				//run through all given combinations and look for a match
				for (int ii = 0; ii < C; ii++)
				{
					//if match
					if ( (combos[0][ii] == x && combos[1][ii] == y) || (combos[0][ii] == y && combos[1][ii] == x) )
					{
						combine = combos[2][ii];
						break;
					}
				}
			}

			//OPPOSITIONS
			if (i != 0)//if not the first element
			{
				char x = elements[i];

				//run through previous elements and look for an opposition
				for (int ii = 0; ii < i; ii++)
				{
					char y = elements[ii];

					for (int iii = 0; iii < D; iii++)
					{
						//check for a match
						if ( (opposes[0][iii] == x && opposes[1][iii] == y) || (opposes[0][iii] == y && opposes[1][iii] == x))
						{
							oppose = true;
							break;
						}
					}
				}
			}

			if (combine != '.' && !oppose)
			{
				elements[i+1] = combine;//replace with the combined product
				elements[i] = '.';//delete other element and replace with a .
			}
			if (oppose)
			{
				//delete all elements so far
				for (int j = 0; j <= i; j++)
					elements[j] = '.';
			}

		}
		
		output << "Case #" << caseno << ": [" ;
		for (int i = 0; i < N; i++)
		{
			if (elements[i] != '.')
			{
				output << elements[i];
				if (i == N-1)
					output << "]" << endl;
				else
					output << ", ";
			}
			else if (i == N-1)
				output << "]" << endl;
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