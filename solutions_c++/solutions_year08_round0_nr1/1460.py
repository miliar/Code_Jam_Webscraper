// googlecode.cpp : Saving the Universe
/* 
	Problem

	The urban legend goes that if you go to the Google homepage and search for "Google", 
	the universe will implode. We have a secret to share... It is true! Please don't try it, 
	or tell anyone. All right, maybe not. We are just kidding.
	The same is not true for a universe far far away. In that universe, if you search on 
	any search engine for that search engine's name, the universe does implode!
	To combat this, people came up with an interesting solution. All queries are pooled 
	together. They are passed to a central system that decides which query goes to which 
	search engine. The central system sends a series of queries to one search engine, and 
	can switch to another at any time. Queries must be processed in the order they're 
	received. The central system must never send a query to a search engine whose name 
	matches the query. In order to reduce costs, the number of switches should be minimized.
	Your task is to tell us how many times the central system will have to switch between 
	search engines, assuming that we program it optimally.

	Input

	The first line of the input file contains the number of cases, N. N test cases follow.
	Each case starts with the number S -- the number of search engines. The next S lines each 
	contain the name of a search engine. Each search engine name is no more than one hundred 
	characters long and contains only uppercase letters, lowercase letters, spaces, and 
	numbers. There will not be two search engines with the same name.
	The following line contains a number Q -- the number of incoming queries. The next 
	Q lines will each contain a query. Each query will be the name of a search engine 
	in the case.

	Output

	For each input case, you should output:
	Case #X: Y

	where X is the number of the test case and Y is the number of search engine switches. 
	Do not count the initial choice of a search engine as a switch.

	Limits

	0 < N <= 20

	Small dataset

	2 <= S <= 10

	0 <= Q <= 100

	Large dataset

	2 <= S <= 100

	0 <= Q <= 1000 
*/

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

bool value_comparer(const std::pair<std::string, size_t>& lhs,
					const std::pair<std::string, size_t>& rhs);
int SearchCount(vector<string>::iterator &enginesStart, vector<string>::iterator &enginesEnd,
				vector<string>::iterator &inputsStart, vector<string>::iterator &inputsEnd);

int main()
{
	ifstream inputFile ("A-large.in");
	ofstream outputFile ("output.in");
	if(!inputFile.is_open())
		return 0;
	if(!outputFile.is_open())
		return 0;
	int totalCases = 0;
	inputFile >> totalCases;
	for (int i=0; i < totalCases; ++i)  
	{
		int searchEnginesCount = 0;
		int searchInputsCounts = 0;
		vector<string> searchEngines;
		vector<string> searchInputs;
		string line;
		inputFile >> searchEnginesCount;
		getline(inputFile, line);	//Get to next line
		for (int j=0; j < searchEnginesCount; ++j)  
		{
			getline(inputFile, line);
			searchEngines.push_back(line);
		}
		inputFile >> searchInputsCounts;
		getline(inputFile, line);	//Get to next line
		for (int j=0; j < searchInputsCounts; ++j)  
		{
			getline(inputFile, line);
			searchInputs.push_back(line);
		}
		int minSearch = SearchCount(searchEngines.begin(), searchEngines.end(), searchInputs.begin(), searchInputs.end());
		if(minSearch <= 0)
			minSearch = 1;
		outputFile << "Case #" << (i+1) << ": " << (minSearch-1) << endl;
	}
	inputFile.close();
	outputFile.close();
	return 0;
}

int SearchCount(vector<string>::iterator &enginesStart, vector<string>::iterator &enginesEnd,
				vector<string>::iterator &inputsStart, vector<string>::iterator &inputsEnd)
{
	map<string, size_t> maxSearch;
	if(distance(inputsStart, inputsEnd) <= 0)
		return 0;
	for(vector<string>::iterator iter = enginesStart; iter != enginesEnd; ++iter)
	{
		maxSearch[*iter] = distance(inputsStart, find(inputsStart, inputsEnd, *iter));
	}
	map<string, size_t>::const_iterator searchEngine = std::max_element(maxSearch.begin(), maxSearch.end(), value_comparer);
	return 1 + SearchCount(enginesStart, enginesEnd, inputsStart+searchEngine->second, inputsEnd);
}

bool value_comparer(const std::pair<std::string, size_t>& lhs,
					const std::pair<std::string, size_t>& rhs)
{
	return lhs.second < rhs.second;
}
