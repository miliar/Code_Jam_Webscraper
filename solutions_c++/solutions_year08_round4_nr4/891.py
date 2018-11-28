// D.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

std::ifstream in("D.in");
std::ofstream out("D.out");

std::string applyPerm(std::string &str, std::vector< int > &perm)
{
	std::string result("");

	for (int i = 0; i < str.size()/perm.size(); ++i)
	{
		for (int j = 0; j < perm.size(); ++j)
			result += str[i*perm.size() + perm[j]];
	}

	return result;
}

int compressedSize(std::string &str)
{
	int result = 1;

	for (int i = 0; i + 1 < str.size(); ++i)
	{
		if (str[i] != str[i + 1])
			++result;
	}

	return result;
}

int solve(int k, std::string &str)
{
	int result = compressedSize(str);
	std::vector< int > perm;

	for (int i = 0; i < k; ++i)
		perm.push_back(i);

	while (std::next_permutation(perm.begin(), perm.end()))
	{
		int r = compressedSize(applyPerm(str, perm));

        if (r < result)
			result = r;
	}

	return result;		 
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;

	in >> T;

	for (int i = 0; i < T; ++i)
	{
		int k;
		std::string str;
		in >> k;
		in.get();
		in >> str;

		out << "Case #" << (i + 1) << ": " << solve(k, str) << "\n";
	}
	return 0;
}

