// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

typedef	long long llong;

int GetSwitchCnt(vector<string> & q, vector<string> &se)
{
	size_t	cq = 0;
	int		sc = 0;
	while (cq < q.size())
	{
		std::set<string>	curEng(se.begin(), se.end());
		while (cq < q.size() && !curEng.empty())
		{
			curEng.erase(q[cq]);
			cq++;
		}
		if (curEng.empty())
		{
			sc++;
			cq--;
		}
	}
	return sc;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream	infile("A-large.in");
	ofstream	outfile("A-large.out");

	size_t		nCases;

	infile >> nCases;
	for (size_t i = 0; i < nCases; ++i)
	{
		string		tmps;
		size_t		nS;
		infile >> nS;

		vector<string>	searchEng(nS);
		getline(infile, tmps);
		for (size_t j = 0; j < nS; ++j)
			getline(infile, searchEng[j]);

		size_t		nQ;
		infile >> nQ;

		vector<string>	queries(nQ);
		getline(infile, tmps);
		for (size_t j = 0; j < nQ; ++j)
			getline(infile, queries[j]);

		outfile << "Case #" << i+1 << ": " << GetSwitchCnt(queries, searchEng) << std::endl;
	}

	return 0;
}

