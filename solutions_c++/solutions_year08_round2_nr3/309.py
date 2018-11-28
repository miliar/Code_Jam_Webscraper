#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

using std::fixed;

#define MAX(a,b)	((a) > (b) ? (a) : (b))
#define MIN(a,b)	((a) < (b) ? (a) : (b))

int pullCard(int* deck, int pos, int deckSize)
{
	do 
    {
		pos++;
		if (pos >= deckSize)
		{
			pos -= deckSize;
		}
	} 
	while (deck[pos] != 0);

	return pos;
}



// ****************************************************************************

int main(int argc, const char* argv[])	// Arguments to executed program should be 1) input file and 2) output file
{
	assert(argc == 3);

	ofstream output(argv[2]);
	ifstream input(argv[1], std::ifstream::in);

	assert(output.good());
	assert(input.good());
		
	// Process all cases
	int numCases_;
	input >> numCases_;
	for (int case_ = 1; case_ <= numCases_; case_++)
	{
		int numCards;
		int total;
		int index;

		input >> numCards;

		int* deck = new int[numCards];
		for (int i = 0; i < numCards; i++)
			deck[i] = 0;

		int sum = 0;
		for (int i = 1; i <= numCards; i++)
		{
			for (int q = 0; q < i; q++)
			{
				sum = pullCard(deck, sum - 1, numCards) + 1;
			}

			deck[sum-1] = i;
		}

		for (int i = 0; i < numCards; i++)	// 1 4 2 3
			cout << deck[i] << " ";  // 1 3 2 5 4

		// Get Input
		input >> total;

		// Output Result
		output << "Case #" << case_ << ": ";// << datum << std::endl;

		for (int i = 0; i < total; i++)
		{
			input >> index;
			output << deck[index-1] << " "; 			
		}

		output << endl;

//		index = (number+number-1+number-2+... % numCards)


		// Process Input







		// Clean Up
		delete[] deck;
	}

	// Clean Up
	input.close();
	output.close();

	return 0;
}


