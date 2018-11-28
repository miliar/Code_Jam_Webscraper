// TopCoder.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

struct saveuniverse
{
	std::string query;
	int numberofoccurance;
	int lastoccurance;
	int crossedcount;

public:
	saveuniverse()
	{
		this->query = "";
		this->numberofoccurance = 0;
		this->lastoccurance = 0;
	}

	saveuniverse(string query_, int numberofoccurance_, int lastoccurance_)
	{
		this->query = query_;
		this->numberofoccurance = numberofoccurance_;
		this->lastoccurance = lastoccurance_;
	}
};


bool operator <(const saveuniverse &left,const saveuniverse &right)
{
	if(left.numberofoccurance == right.numberofoccurance)
	{
		if(left.lastoccurance < right.lastoccurance)
			return true;
		else
			return false;
	}
	else 
		if(left.numberofoccurance < right.numberofoccurance)
			return true;
		else
			return false;
}


int _tmain(int argc, _TCHAR* argv[])
{
	fstream inputfile;
	inputfile.open("A-small-attempt5.in", fstream::in);

	//read number of inputs
	int numberofinputs;
	int i, j, k;

	inputfile>>numberofinputs;

	for(i=0; i< numberofinputs;i++)
	{
		int numberofsearchengines;
		std::map<std::string, saveuniverse> searchengines;
		
		// read number of search engines
		inputfile>>numberofsearchengines;

		std::string searchengine;
		std::getline(inputfile, searchengine, '\n');

		for(j=0;j<numberofsearchengines;j++)
		{
			saveuniverse temp;

			std::getline(inputfile, searchengine, '\n');

			temp.query = searchengine;
			temp.lastoccurance = 0;
			temp.numberofoccurance = 0;

			searchengines.insert(pair<std::string, saveuniverse>(searchengine, temp));
		}

		int numberofqueries;
		std::vector<std::string> queries;
		std::vector<int>		queryoccurance;
		std::vector<int>		lastoccurance;
	
		//read number of queries
		inputfile>>numberofqueries;
		std::string query;

		std::getline(inputfile, query, '\n');
		for(j=0;j<numberofqueries;j++)
		{
			std::getline(inputfile, query, '\n');
			queries.push_back(query);

			map<std::string, saveuniverse>::iterator it;
			it = searchengines.find(query);
			if(it != searchengines.end())
			{
				it->second.numberofoccurance++;
				it->second.lastoccurance = j;
			}
			
		}

		vector<saveuniverse> vecsearchengines;

		//
		// Find
		for( map<string,saveuniverse>::iterator ii=searchengines.begin(); ii!=searchengines.end(); ++ii)
			vecsearchengines.push_back((*ii).second);

		sort(vecsearchengines.begin(), vecsearchengines.end()); 

		//for(k=0;k<vecsearchengines.size();k++)
		//	cout << vecsearchengines[k].query << ": " << vecsearchengines[k].numberofoccurance << " - " << vecsearchengines[k].lastoccurance << endl;

		//cout<<endl;
		
		//
		// Start checking for combinations

		bool runloop = true;
		int numberofswitches=0;
		int searchengineposition=0;
		bool queryfound=false;
		std::string currentsearchengine;
		std::string currentusingsearchengine;
		currentsearchengine = vecsearchengines[0].query;
		int currentsearchposition;

		for(j=searchengineposition;j<queries.size();j++)
		{
			if(queries[j] == vecsearchengines[0].query)
			{
				queryfound = true;
				break;
			}
		}
		if(queryfound)
			currentsearchposition = j;



		if(vecsearchengines[0].numberofoccurance == 0)
		{
			cout<< "Case #" << i+1 << ": " << numberofswitches << endl;
				continue;
		}

		while(runloop)
		{
			for(k=0;k<vecsearchengines.size();k++)
			{
				if(currentusingsearchengine != vecsearchengines[k].query)
				{
					vector<std::string>::iterator it;

					bool queryfound=false;
					for(j=searchengineposition+1;j<queries.size();j++)
					{
						if(queries[j] == vecsearchengines[k].query)
						{
							queryfound = true;
							break;
						}
					}
					if(queryfound)
					{
						if(currentsearchposition < j)
						{
							currentsearchposition = j;
							currentsearchengine = vecsearchengines[k].query;
						}
					}
					else
					{
						// No more switch need
						cout<< "Case #" << i+1 << ": " << numberofswitches << endl;
						runloop=false;
						break;
					}
				}
			}

			if(searchengineposition+1 > queries.size())
			{
				cout<< "Case #" << i+1 << ": " << numberofswitches << endl;
				break;
			}
			else
			{
				searchengineposition = currentsearchposition;
				currentusingsearchengine = currentsearchengine;
				++numberofswitches;
			}
		}
		//cout<<endl;
	}

	inputfile.close();
	return 0;
}