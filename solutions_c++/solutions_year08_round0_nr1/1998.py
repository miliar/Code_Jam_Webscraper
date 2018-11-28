#include <stdio.h>
#include <iostream>
#include <string>
#include <map>

using namespace std;

typedef basic_string<char> charstring;

int main()
{
	map<charstring, char> searchEngines;	// Map of search engine to the index
	int nTestCases=0;						// Number of test cases
	int nSearchEngines=0;					// Number of search engines
	int nQueries;							// Number of queries
	char sengine[256];						// Temp buffer to read the search engine name
	char senginestatus[124];				// Stores the status of search engine found or not.
	int nCnt=0;								// Number of test cases found
	int nSearchEngineSwitches=0;			// Number of swithes happened
	int nSearchEngineIndex=0;				
	char testCasesResult[24];

	//scanf ("%d", &nTestCases);
	cin >> nTestCases;

	for (int i=1; i<=nTestCases; ++i)
	{
		searchEngines.clear();
		nSearchEngines=0;
		//scanf ("%d", &nSearchEngines);
		cin >> nSearchEngines;

		for (int j=1; j<=nSearchEngines; ++j)
		{
			cin.getline(sengine, 256); //. >> sSearchEngine;
			if (sengine[0] == '\0')
			{
				--j;
				continue;
			}

			charstring sSearchEngine(sengine);
			searchEngines.insert(make_pair(sSearchEngine, j));
		}

		// Read the number of queries
		cin >> nQueries;

		// Init
		memset(senginestatus, 0, 124);
		nCnt=0;
		nSearchEngineSwitches=0;

		for (int j=1; j<=nQueries; ++j)
		{
			cin.getline(sengine, 256); //. >> sSearchEngine;
			if (sengine[0] == '\0')
			{
				--j;
				continue;
			}

			charstring sSearchEngine(sengine);

			nSearchEngineIndex = searchEngines[sengine];

			if (senginestatus[nSearchEngineIndex] == 0)
			{
				++nCnt;
				senginestatus[nSearchEngineIndex] = 1;
				if (nCnt == nSearchEngines)
				{
					++nSearchEngineSwitches;
					memset(senginestatus, 0, 124);
					senginestatus[nSearchEngineIndex]=1;
					nCnt=1;
				}
				else
				{
					// Do nothing here
				}
			}
			else
			{
				// Do nothing here.. since same search engine repeats
			}
		}

		testCasesResult[i] = nSearchEngineSwitches;
	}

	for (int i=1; i<=nTestCases;++i)
	{
		cout <<"Case #"<<i<<": "<<(int)testCasesResult[i]<<"\n";
	}


}