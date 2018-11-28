// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <vector>
#include <algorithm>
#include <string>


std::ifstream in("B.in");
std::ofstream out("B.out");

typedef unsigned long long ull;
typedef long long ll;

ull cache[41][2*3*5*7 + 1];

ull solve_engine(std::string &str, ull next, ull r, ull modulo)
{
	if (cache[next][r])
		return cache[next][r] - 1;

    if (str.size() == next)
		if (0 == r)
			return 1;
		else
			return 0;

	ll number = str[next] - '0';
	ull result = solve_engine(str, next + 1, (modulo + r - number % modulo) % modulo, modulo);
	
	if (next + 1 != str.size())
		result += solve_engine(str, next + 1, (modulo + number % modulo - r) % modulo, modulo);

	for (ull i = next + 1; i < str.size(); ++i)
	{
		number = 10*number + str[i] - '0';
		result += solve_engine(str, i + 1, (modulo + r - number % modulo) % modulo, modulo);
		
		if (i + 1 != str.size())
			result += solve_engine(str, i + 1, (modulo + number % modulo - r) % modulo, modulo);
	}

	cache[next][r] = result + 1;

	return result;
}

ull solve(std::string &str, ull next, ull r, ull modulo)
{
	memset(cache, 0, sizeof(cache));

	return solve_engine(str, next, r, modulo);
}

int _tmain(int argc, _TCHAR* argv[])
{
	ull N;

	in >> N;

	for (ull i = 0; i < N; ++i)
	{
		std::string str;
		in >> str;

		ull result = solve(str, 0, 0, 2) + solve(str, 0, 0, 3) + solve(str, 0, 0, 5) + solve(str, 0, 0, 7) 
					 - (solve(str, 0, 0, 2*3) + solve(str, 0, 0, 2*5) + solve(str, 0, 0, 2*7) + solve(str, 0, 0, 3*5) + solve(str, 0, 0, 3*7) + solve(str, 0, 0, 5*7))
					 + solve(str, 0, 0, 2*3*5) +  solve(str, 0, 0, 2*3*7) + solve(str, 0, 0, 2*5*7) + solve(str, 0, 0, 3*5*7)
					 - solve(str, 0, 0, 2*3*5*7);
		out << "Case #" << (i + 1) << ": " << result << "\n";
	}
	return 0;
}

