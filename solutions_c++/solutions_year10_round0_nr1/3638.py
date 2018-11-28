/* ****************************************
	snapper.cpp - Greg Tourville
*/


#include <iostream>
#include <fstream>
#include <assert.h>
#include <string>

using namespace std;

//std::ofstream* out;
std::ifstream* in;

int exp(int a, int b)
{
	int p = 1;
	while (b--)
		p *= a;
	return p;
}

// ****************************************************************************

int main(int argc, const char* argv[])	// Arguments to executed program should be 1) input file and 2) output file
{
	assert(argc == 3);

	ofstream output(argv[2]);
	ifstream input(argv[1], std::ifstream::in);
	//out = &output;
	//in = &input;

	assert(output.good());
	assert(input.good());

	// Process all cases
	int cases;
	input >> cases;

	for (int k = 1; k <= cases; k++)
	{	
		int N, K;
		input >> N;
		input >> K;

		bool on = ((K % exp(2,N)) == exp(2,N)-1);

		output << "Case #" << k << ": ";
		if (on)
			output << "ON" << std::endl;
		else
			output << "OFF" << std::endl;
	}

	// Clean up
	input.close();
	output.close();

	return 0;
}
