/* ****************************************
	universe.cpp - Greg Tourville - July 17th - Google Code Jam - Problem B
*/


#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

int FindSoonest(int tokens[], int size, int start, int symbol);


int FewestSwitches(int tokens[], int size, int numbers)
{
	int numSwitches = 0;
	int pos = 0;

	while (pos < size)
	{
		int newPos = pos;
		for (int i = 0; i < numbers; i++)
		{
			int soonest = FindSoonest(tokens, size, pos, i);	// Find the symbol that allows for the longest stretch without switching
			if (soonest > newPos)
				newPos = soonest;
		}
		if (newPos != size)
			numSwitches++;	// Increment the number of switches
		pos = newPos;
	}

	return numSwitches;
}


int FindSoonest(int tokens[], int size, int start, int symbol)
{
	int q = start;
	while (q < size && tokens[q] != symbol)
		q++;
	return q;
}



// ****************************************************************************

int main(int argc, const char* argv[])	// Arguments to executed program should be 1) input file and 2) output file
{
	assert(argc == 3);

	std::ofstream output(argv[2]);
	std::ifstream input(argv[1], std::ifstream::in);

	assert(output.good());
	assert(input.good());
		

	// Process all cases
	int cases;
	input >> cases;
	for (int i = 1; i <= cases; i++)
	{
		int numSearchEngines;
		input >> numSearchEngines;
		
		// read in the search engines
		string* engines = new string[numSearchEngines];

		char name[256];
		input.getline(name, 256);
		for (int j = 0; j < numSearchEngines; j++)
		{
			input.getline(name, 256);
			engines[j] = string(name);
			//input >> engines[j];
		}

		int numSearches;
		input >> numSearches;

		int* tokens = new int[numSearches];
		string engine;

		
		input.getline(name, 256);

		// create an array of #s 0 to numSearchEngiens-1 corresponding to each engine
		for (int j = 0; j < numSearches; j++)
		{
			int tokenNum;
			//input >> engine;
			input.getline(name, 256);
			engine = string(name);

			for (tokenNum = 0; ; tokenNum++)
			{
				assert(tokenNum < numSearchEngines);

				if (engine.compare(engines[tokenNum]) == 0)
					break;
			}

			tokens[j] = tokenNum;
		}
		
		// compute and output
		output << "Case #" << i << ": " << FewestSwitches(tokens, numSearches, numSearchEngines) << std::endl;


		// clean up
		delete[] tokens;
		delete[] engines;
	}

	// Clean up
	input.close();
	output.close();

	return 0;
}


