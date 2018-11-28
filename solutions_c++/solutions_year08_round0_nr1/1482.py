// searcheng.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;



class CsearchEngine
{
	string m_name;
public:
	void setname(string name)
	{
		m_name = name;
	}

	int numOfQueriesCanProc(vector<string> &queries)
	{
		int num = 0;
		for (vector<string>::iterator itr = queries.begin(); itr!= queries.end(); itr++)
		{
			if(0 == m_name.compare(*itr))
			{
				break;
			}
			num++;
		}
		return num;
	}

};

int MaxQueriesCanProcOnce(vector<CsearchEngine> &engineList, vector<string> &queriesList)
{
	int maxqueries=0, temp=0;
	for (vector<CsearchEngine>::iterator itr = engineList.begin(); itr!= engineList.end(); itr++)
	{
		temp = (*itr).numOfQueriesCanProc(queriesList);
		if(maxqueries < temp)
		{
			maxqueries = temp;
		}
	}
	return maxqueries;
}
int main()
{
	int testcases;
	int engines, queries;
	char str [151];
	CsearchEngine engine;
	FILE * fp = NULL ;
	FILE * fpout = NULL;
	int switches =0;
	int maxqueries =0;
	vector<CsearchEngine> searchEngineList;
	vector<string> queriesList;
	string inputfilename="c:\\A-large.in"; /* provide input file */
	string outputfilename="c:\\output.txt";

	if ((fp = fopen(inputfilename.c_str(), "r")) < 0)
	{
		fprintf(stderr, "cannot create  %s\n",
			inputfilename.c_str());
		return -1;
	}
	
	/* Read # of testcases */
	fgets(str, 151, fp);
	testcases = atoi(str);

	for(int count=0;count<testcases; count++)
	{
		searchEngineList.clear();
		queriesList.clear();

		/* Read # of search engine */
		fgets(str, 151, fp);
		engines = atoi(str);

		/* populate searchEngineList */
		for(int count1=0;count1 <engines; count1++)
		{			  
			fgets(str, 151, fp);
			engine.setname(str); 
			searchEngineList.push_back(engine);
		}

		/* Read # of search queries */
		fgets(str, 151, fp);
		queries = atoi(str);

		/* populate queriesList */
		for(int count1=0;count1 <queries; count1++)
		{			 
			fgets(str, 151, fp);
			queriesList.push_back(str);
		}
		switches = 0;

		/* here searchEngineList has list of engines and queriesList has list of queries to be processed*/
		while(queriesList.size())
		{
			switches++;
			maxqueries = MaxQueriesCanProcOnce(searchEngineList, queriesList);
			queriesList.erase(queriesList.begin(), queriesList.begin()+ maxqueries); 
		}

		if(!fpout)
		{
			if ((fpout = fopen(outputfilename.c_str(), "w+")) < 0)
			{
				fprintf(stderr, "cannot open output file %s\n",
					outputfilename.c_str());
				return -1 ;
			}
		}
		fprintf(fpout, "Case #%d: %d\n",  count+1, switches?switches-1:switches);
		//printf("\n CASE #%d: %d", count+1, switches?switches-1:switches);

	}
	fclose(fpout);
	fclose(fp);
	return 0;
}

