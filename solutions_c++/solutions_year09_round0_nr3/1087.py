/* ****************************************
	c.cpp - Greg Tourville - September 2nd - Google Code Jam - Problem C
*/


#include <iostream>
#include <fstream>
#include <assert.h>

const int MAX_CHARACTERS = 501;
const int NUM_DIGITS = 4;
const char* TARGET_PHRASE = "welcome to code jam";
//const int PHRASE_LEN = strlen(TARGET_PHRASE);
const int PHRASE_LEN = 19;


char*	testPhrase;

typedef __int64 BIG;


BIG Clip(BIG n)
{
	return n%10000;
}

/*
int GetDigit(BIG n, int digits)
{
	if (n == 0)
		return 0;

	int a = 1;
	for (int i = 0; i < digits; digits++)
		a *= 10;
	return (n%a/(a/10));
}*/

BIG FindNum(const char* target, const char* phrase, BIG t[MAX_CHARACTERS][PHRASE_LEN])
{
	BIG* lookup = &(t[phrase - testPhrase][target - TARGET_PHRASE]);
	if (*lookup != -1)
		return *lookup;

	BIG r = 0;
	char c = target[0];
	if (c == '\0')
		return 1;
	int idx = 0;
	while (phrase[idx] != '\0')
	{
		if (phrase[idx] == c)
			r += FindNum(&target[1], &phrase[idx], t);
		idx++;
	}
	*lookup = Clip(r);
	return *lookup;
}

void ClearTable(BIG t[MAX_CHARACTERS][PHRASE_LEN])
{
	for (int i = 0; i < MAX_CHARACTERS; i++)
		for (int j = 0; j < PHRASE_LEN; j++)
			t[i][j] = -1;
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
	input.ignore(1, '\n');
	for (int i = 1; i <= cases; i++)
	{
		char phrase[MAX_CHARACTERS+1];
		testPhrase = &phrase[0];
		input.getline(phrase, MAX_CHARACTERS, '\n');

		BIG num = 0;
		BIG	table[MAX_CHARACTERS][PHRASE_LEN];
		ClearTable(table);

		if (strlen(phrase) >= strlen(TARGET_PHRASE))
			num = Clip(FindNum(TARGET_PHRASE, phrase, table));	
		
		// compute and output
		
		output << "Case #" << i << ": ";

		BIG fact = num;
		for (int i = 0; i < 4; i++)
		{
			if (fact)
				fact /= 10;
			else
				output << 0;
		}
		if (num)
			output << num;
		output << std::endl;
	}

	// Clean up
	input.close();
	output.close();

	return 0;
}
