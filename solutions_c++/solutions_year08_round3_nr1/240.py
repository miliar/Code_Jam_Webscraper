// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <functional>

typedef unsigned long long ull;

std::ifstream in("A.in");
std::ofstream out("A.out");

ull N, P, K, L;

ull freq[1000001];

void input ()
{
	in >> P >> K >> L;

	for (ull i = 0; i < L; ++i)
		in >> freq[i];
}

ull solve()
{
	std::sort(freq, freq + L, std::greater< ull >());

	ull result = 0;
	ull pad = 0;
	ull key = 0;

	for (unsigned i = 0; i < L; ++i)
	{
		if (key % K == 0)
			++pad;
		++key;

		result += pad*freq[i];
	}

    return result;	
}

int _tmain(int argc, _TCHAR* argv[])
{
	ull N;
	in >> N;

	for (ull i = 0; i < N; ++i)
	{
		input();

		out << "Case #" << (i + 1) << ": " << solve() << "\n";

	}
	return 0;
}

