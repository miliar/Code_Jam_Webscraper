/************************/
/*	GCJ 2008		     */
/*	Matthew D Sandy       */
/************************/

#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

int engineID(string* engines, string query);

int main(int argc, char **argv)
{
	ifstream inFile;
	inFile.open(argv[1]);
	if(inFile.is_open()) cout<<"Opened \""<<argv[1]<<"\" for read...\n";
	else {cout<<"Error opening \""<<argv[1]<<"\" for read...\n"; return 1;}
	ofstream outFile;
	outFile.open(argv[2]);
	if(inFile.is_open()) cout<<"Opened \""<<argv[2]<<"\" for read...\n";
	else {cout<<"Error opening \""<<argv[2]<<"\" for write...\n"; return 1;}
	
	//////////////////////BEGIN CODE//////////////////////
	/*Saving the Universe
	For each test case, initialize the number of switches required to zero, and look at the query list.
	Starting at the beginning, look at each query, noting which terms are searched for.
	Once a query is hit such that all engines have been queried once, that query should be the engine that
	all previous queries in this loop should use.  eg: g,m,y searching for g,m,m,g,y,g,y,m; the 5th search 'y' is
	the last search engine queried, so start searching with 'y' engine.  When this situation is encountered,
	increment the switch number, and begin this loop again starting at the switch location, until all queries
	are processed. */
	
	int numCases;
	inFile >> numCases;
	
	for(int i=1;i<=numCases;i++)
	{	//for each test case...
		cout<<"Now processing case #"<<i<<"\n";
		int numEngines;
		inFile >> numEngines;
		inFile.ignore(5,'\n');	//next line (unix endline format)
		cout<<"Reading "<<numEngines<<" engine names...\n";
		string engines[numEngines];
		for(int j=0;j<numEngines;j++)
		{	//read in engine names
			getline(inFile,engines[j]);
			cout<<"\t"<<j<<": "<<engines[j]<<"\n";
		}
		int numQueries;
		inFile >> numQueries;
		inFile.ignore(5,'\n');	//next line
		cout<<"Reading "<<numQueries<<" queries...\n";
		int queries[numQueries];
		string query;
		for(int j=0;j<numQueries;j++)
		{	//read in queries
			getline(inFile,query);
			queries[j] = engineID(engines,query);
			cout<<"\t"<<query<<": "<<queries[j]<<"\n";
		}
		
		//we now have this test case loaded into memory; begin solution procedure...
		int numSwitches = 0;	//initialize switch count
		bool searched[numEngines];
		for(int j=0;j<numEngines;j++) searched[j] = 0;	//initialized the boolean 'searched' array
		int numSearched = 0;
		for(int q=0;q<numQueries;q++)
		{	//for each query
			if(!searched[queries[q]])	//if this query has not yet been searched for
			{
				searched[queries[q]] = 1;	//set it to searched
				numSearched++;	//and increment the number used
			}
			if(numSearched == numEngines)	//if this query exhausted the engine list
			{
				numSwitches++;	//then we require a switch at this point
				numSearched = 1;	//we're going to have already searched this query, so set to 1
				for(int j=0;j<numEngines;j++) searched[j] = 0;	//initialize the used array
				searched[queries[q]] = 1;	//we're searching this query now
			}
		}
		
		//once we're done looping through the queries, write the output:
		outFile<<"Case #"<<i<<": "<<numSwitches<<"\n";
	}
	
	//////////////////////END CODE//////////////////////
	
	inFile.close();
	outFile.close();
}

int engineID(string* engines, string query)
{	//returns the engine ID for a given query string
	int i=0;
	while(1)
	{
		if(engines[i]==query) return i;
		i++;
	}
}
