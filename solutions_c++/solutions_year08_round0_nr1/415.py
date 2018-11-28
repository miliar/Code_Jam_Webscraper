// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <limits>
#include <stdexcept>

using namespace std;

class QA
{
public:
	static void go(string inputFilePath, string outputFilePath);
};

void QA::go(string inputFilePath, string outputFilePath)
{
	fstream inpf(inputFilePath.c_str(), ios_base::in);
	fstream outf(outputFilePath.c_str(), ios_base::out);

	if (!inpf.good() || !outf.good())
	{
		throw(std::invalid_argument("Can't open input or output file!"));
	}

	int N;
	inpf >> N;

	for (int n = 0; n < N; ++n)
	{
		int S;
		inpf >> S >> ws;
		
		map<string, int> engines;
		for (int s = 0; s < S; ++s)
		{
			string curEngine;
			getline(inpf, curEngine);
			engines[curEngine] = s;
		}

		int Q;
		inpf >> Q >> ws;
		vector<int> queries;
		for (int q = 0; q < Q; ++q)
		{
			string curQuery;
			getline(inpf, curQuery);
			queries.push_back(engines[curQuery]);
		}	

		vector<int> statesDP(S, 0);

		for (int q = 0; q < Q; ++q)
		{
			vector<int> statesDPnext(S, numeric_limits<int>::max());
			for (int s = 0; s < S; ++s)
			{
				if (statesDP[s] < numeric_limits<int>::max())
				{
					if (queries[q] != s)
					{
						statesDPnext[s] = min(statesDPnext[s], statesDP[s]);
					}
					else
					{
						for (int sn = 0; sn < S; ++sn)
						{
							if (sn != s)
							{
								statesDPnext[sn] = min(statesDPnext[sn], statesDP[s] + 1);
							}
						}
					}
				}
			}
			statesDP = statesDPnext;
		}

		int minChanges = numeric_limits<int>::max();
		for (int s = 0; s < S; ++s)
		{
			minChanges = min(minChanges, statesDP[s]);
		}
		if (minChanges == numeric_limits<int>::max())
			minChanges = -1;

		outf << "Case #" << n + 1 << ": " << minChanges << endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	QA::go("input.txt", "output.txt");

	cout << endl;
	getchar();
	return 0;
}

