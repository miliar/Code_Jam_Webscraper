// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <iostream>

using std::cin;
using std::cout;

#include <string.h>
#include <algorithm>

int Process()
{
	int num_candies;
	std::cin >> num_candies;

	int patrick_sum = 0;
	int sum = 0;

	int smallest_seen = -1;
	for( int i = 0; i < num_candies; ++i )
	{
		int value;
		std::cin >> value;

		patrick_sum ^= value;
		sum += value;

		if( smallest_seen < 0 || value < smallest_seen )
			smallest_seen = value;
	}

	// If the XOR of the values is non-zero, it cannot be divided into two 'equal' piles
	if( patrick_sum != 0 )
		return 0;

	// Sean can give the smallest value candy to Patrick, and keep the remainder
	return sum - smallest_seen;
}

int main(int argc, char* argv[])
{
	int num_tests;
	cin >> num_tests;

	for( int i = 0; i < num_tests; ++ i )
	{
		int res = Process();
		printf( "Case #%d: ", i+1 );
		if( res == 0 )
			printf( "NO\n" );
		else
			printf( "%d\n", res );
	}

	return 0;
}

