// Template for code jam!
//
#include "stdafx.h"
//#include <math.h>
#include <fstream>
#include <string>
#include <vector>
//#include <map>
//#include <queque>
//#include <stack>
//#include <set>

using namespace std;

typedef vector<int> seMEM;

//other functions may go here!
int getMinNumChanges(vector<string>& searchEngines, vector<string>& queries, int posQueries, vector<seMEM>& memTable)
{
	int minChanges = queries.size()+1;
	int evalChanges;
	int posSearch;
	
	if(posQueries >= queries.size())
		return 0;

	for(int x=0; x<searchEngines.size(); x++)
	{
		if(searchEngines[x] != queries[posQueries])
		{
			if(memTable[x][posQueries] > -1)
				evalChanges = memTable[x][posQueries];
			else
			{
				evalChanges = 0;
				posSearch = posQueries+1;
				while((posSearch < queries.size()) && (queries[posSearch] != searchEngines[x]))
					posSearch++;
				if(posSearch < queries.size())
					evalChanges = getMinNumChanges(searchEngines, queries, posSearch, memTable) + 1;
				memTable[x][posQueries] = evalChanges;
			}
			if(evalChanges < minChanges)
				minChanges = evalChanges;
		}
	}
	return minChanges;
}

//main function!

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("A-large.in");
    ofstream outputFile("A-large.out", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
    {
      //error openning input/output file!
      return 0;
    }

	int numIterations;
	string receive;
	getline(inputFile, receive);
	numIterations = atoi(receive.c_str());
    int numCases = 1;
	vector<string> searchEngines, queries;
	int numEngines, numQueries;
	vector<seMEM> memTable;

	while(numCases <= numIterations)
	{
		//parsing code goes here
		searchEngines.clear();
		queries.clear();
		memTable.clear();
		getline(inputFile, receive);
		numEngines = atoi(receive.c_str());
		for(int x=0; x<numEngines; x++)
		{
			getline(inputFile, receive);
			searchEngines.push_back(receive);
			memTable.push_back(seMEM());
		}
		getline(inputFile, receive);
		numQueries = atoi(receive.c_str());
		for(int x=0; x<numQueries; x++)
		{
			getline(inputFile, receive);
			queries.push_back(receive);
			for(int y=0; y<numEngines; y++)
			{
				memTable[y].push_back(-1);
			}
		}
		
		//problem code goes here
		outputFile << "Case #" << numCases << ": " << getMinNumChanges(searchEngines, queries, 0, memTable) << endl;
		numCases++;
	}
	return 0;
}