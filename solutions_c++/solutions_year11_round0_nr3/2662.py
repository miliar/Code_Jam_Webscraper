// GJam.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <assert.h>
using namespace std;

const int abc_size = ('Z' - 'A') + 1;

int main(int argc, char* argv[])
{

	assert(argc > 1);
	FILE * output =  0; 
	if (argc > 2)
	{
#ifndef _DEBUG
		output = freopen(argv[2], "w", stdout);
#endif
	}
	FILE * input = fopen(argv[1], "r");

	char combines[abc_size][abc_size];
	multimap<char, char> eliminates;
	int count;
	fscanf(input, "%d", &count);

	for (int i=0; i< count; ++i)
	{
		cout << "Case #" << (i+1) << ": ";
		int candies;
		fscanf(input, "\n%d\n", &candies);
		int xor = 0;
		int min_val = 10*10*10*10*10*10 + 1;
		int sum_val = 0;
		int candie;
		for (int j = 0; j < candies; j++)
		{
			fscanf(input, "%d ", &candie);
			xor ^= candie;
			min_val = min(min_val, candie);
			sum_val += candie;
		}
		if (xor)
		{
			cout << "NO\n";
		}
		else
		{
			cout << (sum_val - min_val) << "\n";
		}
	}

	if (output)
		fclose(output);
	if (input)
		fclose(input);
	return 0;
}

