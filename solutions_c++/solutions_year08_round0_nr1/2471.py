#include <iostream>
#include <map>
#include <string>
#include <stdio.h>

#define SEARCH_ENGINE_LENGTH_MAX 100

using namespace std;

void handleCase(int caseNo,FILE* fp)
{
	// First read no. of search engines.
	map <string, bool> searchEngines;
	map <string, bool>::const_iterator searchEngineIter;
	string query;
	char queryStr[100];

	int nSearchEngines = 0;
	fscanf (fp,"%d",&nSearchEngines);
	fgets (queryStr,10,fp);
	//cout << "case no: " << caseNo << " - " << nSearchEngines << " search Engines." << endl;
	for (int i=0;i<nSearchEngines;i++)
	{
		//searchEngines[fgets(fp)] = false;
		fgets(queryStr,SEARCH_ENGINE_LENGTH_MAX,fp);
	//	cout << "Search engine " << (i+1) << " : " << queryStr << endl;
	}
		
	//cout << "Read ses" << endl;
	int nQueries = 0,nSwitches=0;
	fscanf (fp,"%d",&nQueries);
	fgets (queryStr,10,fp);
	//cout << "Queries: " << nQueries << endl;
	for (int i=0;i<nQueries;i++)
	{
		fgets(queryStr,SEARCH_ENGINE_LENGTH_MAX,fp);
		query = queryStr;
		//cout << "Query for: " << query << endl;
		searchEngines[query] = true;
		if (searchEngines.size() == nSearchEngines)
		{
			//for (searchEngines=searchEngines.begin(); searchEngineIter != searchEngine.end() ; searchEngineIter++)
			searchEngines.clear();		
			searchEngines[query] = true;
			nSwitches++;
		}
	}

	cout << endl << "Case #" << caseNo << ": " << nSwitches;
	return;
}

int main(int argc, char* argv[])
{
	int nTestCases=0;
	FILE* fp = fopen (argv[1],"r");
	fscanf (fp,"%d",&nTestCases);
	//cout << nTestCases << " cases in all.";
	for (int i=0;i<nTestCases;i++)
		handleCase(i,fp);

	fclose(fp);
	return 0;
	
}
