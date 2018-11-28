#include <string>
#include <map>

#include "stdio.h"
#include <stdlib.h>

using namespace std;

map<string, int> searchEngines;
int Queries[1001];

void main()
{
	FILE *pFile = fopen ("c:\\A-large.in", "r" );
	FILE *outFile = fopen("c:\\out", "w");
	
	int numberOfCases = 0;

	

	int numberOfSearchEngines = 0;
	int numberOfQueries = 0;

	char cnumberOfCases[6];
	fgets(cnumberOfCases,5,pFile);
	numberOfCases = atoi(cnumberOfCases);

	string output;
	char SearchEngineName[101], QueryName[101];

	int numberOfSwitches = 0;

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		char cnumberOfSearchEngines[6] = {0};
		char cnumberOfQueries[6] = {0};
		searchEngines.clear();	
		numberOfSwitches = 0 ;

		fgets(cnumberOfSearchEngines,5,pFile) ;
		numberOfSearchEngines = atoi(cnumberOfSearchEngines);

		for(int SearchEngine = 0; SearchEngine < numberOfSearchEngines ; SearchEngine++)
		{
			fgets(SearchEngineName,100,pFile) ;
			printf("\n SearchEngine : %s", SearchEngineName);
		
			if( SearchEngineName[0] == 10 )
			{
				SearchEngine--;
				continue;
			}

			searchEngines.insert(make_pair(SearchEngineName, SearchEngine));
		}

		fgets(cnumberOfQueries,5,pFile) ;
		numberOfQueries = atoi(cnumberOfQueries);

		int QueryNumber;

		for(QueryNumber = 0; QueryNumber < numberOfQueries ; QueryNumber++)
		{
			int ii;
			fgets(QueryName,100,pFile) ;
			if( QueryName[0] == 10 )
			{
				QueryNumber--;
				continue;
			}
			printf("\n Query : %s", QueryName);

			std::map<string, int>::iterator it = searchEngines.find(QueryName);
			
			if(it != searchEngines.end())
				Queries[QueryNumber] = it->second ;
			else
			{
				int i =0;
				i=i;
			}
		}		

		int CurrentSearchEngine = 0;
		int PreviousSearchEngine = 0;

		int maxPosition = 0;

		for(int SearchEngine = 0; SearchEngine < numberOfSearchEngines ; SearchEngine++)
		{
			int q ;

			for(q = 0; q < numberOfQueries ; q++)
			{
				if(Queries[q] == SearchEngine)
					break;
			}

			if(q == numberOfQueries)
			{
				CurrentSearchEngine = SearchEngine;
				break;
			}

			if(q > maxPosition)
			{
				maxPosition = q;
				CurrentSearchEngine = SearchEngine;
			}
		}

		for(QueryNumber = 0; QueryNumber < numberOfQueries ; QueryNumber++)
		{
			if(Queries[QueryNumber] == CurrentSearchEngine)
			{
				// Switch to the optimal Search Engine

				int maxPosition = 0;
				int BestSearchEngine = 0;

				for(int SearchEngine = 0; SearchEngine < numberOfSearchEngines ; SearchEngine++)
				{
					if(SearchEngine != CurrentSearchEngine)
					{
						int q ;

						for(q = QueryNumber; q < numberOfQueries ; q++)
						{
							if(Queries[q] == SearchEngine)
								break;
						}

						if(q == numberOfQueries)
						{
							BestSearchEngine = SearchEngine;
							break;
						}

						if(q > maxPosition)
						{
							maxPosition = q;
							BestSearchEngine = SearchEngine;
						}
					}
				}

				if(BestSearchEngine != CurrentSearchEngine)
				{
					numberOfSwitches++;
					CurrentSearchEngine = BestSearchEngine;
				}
			}
		}

		fprintf(outFile, "Case #%d: %d\n", caseNumber, numberOfSwitches);
	}

	fclose(pFile);
	fclose(outFile);
}