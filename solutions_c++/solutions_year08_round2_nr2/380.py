// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>

#include <math.h>

using namespace std;

typedef	long long llong;

inline int GetSetNum(int i, vector<int> & sets)
{
	while (sets[i] != i)
		i = sets[i];
	return i;
}

int GetSetCount(llong A, llong B, llong P, vector<int> & primes)
{
	if (A == B)
		return 1;
	vector<int> sets(B-A + 1);
	for (size_t i = 0; i < sets.size(); ++i)
		sets[i] = i;
	for (size_t i = 0; i < primes.size(); ++i)
	{
		int pr = primes[i];
		if (primes[i] < P)
			continue;
		llong n = (A % pr == 0) ? A/pr : A/pr + 1;
		if (n*pr > B)
			continue;
		int	setN = GetSetNum(n*pr - A, sets);
		for (; pr*n <= B; ++n)
			sets[GetSetNum(n*pr - A, sets)] = setN;
	}
	int res = 0;
	for (size_t i = 0; i < sets.size(); ++i)
	{
		if (sets[i] == i)
			res++;
	}
	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream	infile("B-small.in");
	ofstream	outfile("B-small.out");

	vector<int>		primes;
	vector<bool>	isprime(100002, true);

	int N = 100001;

	for (int i = 2; i <= N; ++i)
	{
		if (isprime[i])
			primes.push_back(i);
		for (int j = 2; i*j <= N; ++j)
			isprime[i*j] = false;
	}

	size_t		nCases;

	infile >> nCases;
	for (size_t i = 0; i < nCases; ++i)
	{
		int n;
		llong	A, B, P;
		infile >> A >> B >> P;
		outfile << "Case #" << i+1 << ": " << GetSetCount(A, B, P, primes) << std::endl;
	}

	return 0;
}

