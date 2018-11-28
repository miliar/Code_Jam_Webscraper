// A.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

typedef unsigned long long ull;

std::ifstream in("A.in");
std::ofstream out("A.out");

std::vector< std::string > queries, engines;

void getQueries(unsigned int n)
{
	queries.clear();
	queries.reserve(n);
	for (int i = 0; i < n; ++i)
	{
		char buf[1000];

		in.getline(buf, 1000, '\n');
		queries.push_back(std::string(buf));
	}
}

void getEngines(unsigned int n)
{
	engines.clear();
	engines.reserve(n);
	for (int i = 0; i < n; ++i)
	{
		char buf[1000];

		in.getline(buf, 1000, '\n');

		engines.push_back(std::string(buf));
	}
}

void printVector(std::vector< std::string > &v)
{
	out << "************************************\n";
	for (int i = 0; i < v.size(); ++i)
		out << v[i] << "\n";
	out << "************************************\n";
}

unsigned int countMaxNumberProcessedQueries(unsigned int engine, unsigned int queryStart)
{
	unsigned int result = 0;
	for (; queryStart < queries.size(); ++queryStart)
	{
		if (engines[engine] == queries[queryStart])
			return result;

		++result;
	}

	return result;
}

unsigned int solve()
{
	unsigned int processedQueries = 0;
	unsigned int result = 0;

	if (queries.size() <= 1)
		return 0;
	
	for (; queries.size() != processedQueries;)
	{
		unsigned int p = 0;
		for (unsigned int i = 0; i < engines.size(); ++i)
			p = std::max(p, countMaxNumberProcessedQueries(i, processedQueries));

		processedQueries += p;
		++result;
	}

	return result - 1;
}

int main()
{
	unsigned int n;
	in >> n;
	for (unsigned int i = 0; i < n; ++i)
	{
		unsigned int s;
		in >> s;
		in.get();
		getEngines(s);
		//printVector(engines);

		unsigned int q;
		in >> q;
		in.get();
		getQueries(q);
		//printVector(queries);

		out << "Case #" << (i + 1) << ": " << solve() << "\n";
	}
	return 0;
}

