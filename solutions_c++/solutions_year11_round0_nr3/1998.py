// Patrick's addition method is actually XOR
// Consequence: any split has the same result !
// If a solution exist, the better one is:
// - 1st pile with the smallest candy
// - 2nd pile with all other candies

#include "stdafx.h"
#include <iostream>
#include <cstdlib>
using namespace std;

// Usage: CandySplitting < input.in
// TODO: checking file validity

int main(int argc, char* argv[])
{
	int T; // Number of test cases
	cin >> T;
	
	// For each test case / line in file
	for(int t=0; t<T; t++)
	{
		int N; // Number of candies
		cin >> N;
		int xor = 0; // XORs of all candies' values
		int sum = 0; // Sum of all candies' values
		int min = INT_MAX; // Minimum candy value
		for(int i=0; i<N; i++)
		{
			int C;  // Candy value
			cin >> C;
			xor ^= C;
			sum += C;
			if(min > C) min = C;
		}

		if(xor != 0)
		{
			// Impossible
			cout << "Case #" << t+1 << ": NO" << endl;
		}
		else
		{
			cout << "Case #" << t+1 << ": " << sum-min << endl;
		}
	}

	return 0;
}
