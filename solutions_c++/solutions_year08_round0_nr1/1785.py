// Rob Keim
// Google Code Jam - Qualifying Round
// Problem 1 - Saving the Universe

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> searchEngines;	
vector<string> queries;
int numSwitches;
int N, S, Q;
string tmp;
int minS[1000];

void process(int curEngine, int curPos, int curSwitches)
{
	if (curPos == Q)
	{
		if (curSwitches < numSwitches)
		{
			numSwitches = curSwitches;
		}
		return;
	}
	else
	{
		if (curSwitches <= minS[curPos])
		{
			minS[curPos] = curSwitches;
			if (searchEngines.at(curEngine) == queries.at(curPos))
			{
				curSwitches++;
				for (int i = 0; i < S; i++)
				{
					if (i != curEngine)
					{
						process(i, curPos + 1, curSwitches);
					}
				}
			}
			else
			{
				process(curEngine, curPos + 1, curSwitches);
			}
		}
	}
	return;
}

int main()
{
	ifstream fin ("A-large.in");
	ofstream fout ("A.out");

	getline (fin, tmp);
	N = atoi(tmp.c_str());
	for (int i = 1; i <= N; i++)
	{
		// Clear the vectors
		searchEngines.clear();
		queries.clear();
		numSwitches = INT_MAX;
		for (int j = 0; j < 1000; j++)
		{
			minS[j] = INT_MAX;
		}
		
		// Get the search engine information
		getline(fin, tmp);
		S = atoi(tmp.c_str());
		for (int j = 0; j < S; j++)
		{
			getline(fin, tmp);
			searchEngines.push_back(tmp);
		}

		// Get the query information
		getline(fin, tmp);
		Q = atoi(tmp.c_str());
		for (int j = 0; j < Q; j++)
		{
			getline(fin, tmp);
			queries.push_back(tmp);
		}
		for (int j = 0; j < S; j++)
		{
			process(j, 0, 0);
		}
		cout << "Case #" << i << ": " << numSwitches << endl;
		fout << "Case #" << i << ": " << numSwitches << endl;
	}
	return 0;
}
