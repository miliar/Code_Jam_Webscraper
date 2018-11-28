#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cassert>

using namespace std;

typedef priority_queue<int, vector<int>, std::greater<int> > pqueue ;

/*
Oh the blood and the treasure, and the losing it all, 
the time that we wasted and the place where we fall. 
Will we wake in the morning and know what it was all for? 
Up in our bedroom, after the war?
 */

int main(int argc, char *argv[])
{
	assert(argc > 1);
	ifstream ifile(argv[1]);
	
	int cases=0;
	ifile >> cases;
	for(int caseno=1; caseno <= cases; caseno++)
	{
		int S=0;
		ifile >> S;
		ifile.ignore();
		set<string> engines;
		for(int i=0; i<S; i++)
		{
			string engine;
			getline(ifile, engine);
			engines.insert(engine);
		}
		int Q=0;
		ifile >> Q;
		ifile.ignore();
		map<string, pqueue > occurences;
		for(int i=0; i<Q; i++)
		{
			string query;
			getline(ifile, query);
			for(set<string>::iterator it = engines.begin(); it != engines.end(); it++)
			{
				if(*it == query)
					occurences[query].push(i);
			}
		}
	
		int switches=0;
		while(true)
		{
			int stepidx=-1;
			string stepstring;
			for(set<string>::iterator it = engines.begin(); it != engines.end(); it++)
			{
				if(occurences[*it].empty())
				{
					stepidx = -1;
					break;
				}
				else if(occurences[*it].top() > stepidx)
				{
					stepidx = occurences[*it].top();
					stepstring = *it;
				}
			}
			if(stepidx == -1)
				break;
			switches++;
			for(set<string>::iterator it = engines.begin(); it != engines.end(); it++)
			{
				while(!occurences[*it].empty() && occurences[*it].top() < stepidx)
					occurences[*it].pop();
			}
		}
		cout << "Case #" << caseno << ": " << switches << endl;
	}
}