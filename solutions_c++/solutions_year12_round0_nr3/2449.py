// Google Code Jam - Qualification Round 2012 - Problem C. Recycled Numbers

#include "stdafx.h"
#include <iostream>

using namespace std;

int countRecycledPairsWith(int n, int mod, int B)
{
	// Return the number of recycled pairs (n,m)
	int ret = 0;

	int m = n;
	do
	{
		// rotate m
		m = 10*m;
		m = (m%mod) + m/mod;

		if(m <= B && n < m) 
		{
			ret++; // (n,m) is a (unique) recycled pair
		}
	}
	// Stop either if we have rotate all digits, or if n has a repetitive pattern
	// In any case, all numbers have been considered
	while(m != n);

	return ret;
}

int getNextPower(int p, int num)
{
	int ret = p;
	while(ret <= num) ret *= p;
	return ret;
}

int main(int argc, char* argv[])
{
	int T;
	cin >> T;

	for(int i=1; i<=T; i++)
	{
		int A, B;
		cin >> A >> B;

		int mod = getNextPower(10, A);

		int recycledPairs = 0;
		for(int n=A; n<=B; n++)
		{
			recycledPairs += countRecycledPairsWith(n, mod, B);
		}

		cout << "Case #" << i << ": " << recycledPairs << endl;
	}

	return 0;
}

