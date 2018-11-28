// Snapper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <sstream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	//Number of test cases
	int cases = 0;

	ifstream file;
	file.open("C-small0.in");
	ofstream outfile;
	outfile.open("answer.txt");
	string output = "";

	string line = "";
	getline(file,line);
	cases = atoi(line.c_str());
	
	int numRides = 0;
	int maxPeople = 0;
	int numGroups = 0;

	vector<int> list1;
	vector<int> list2;
	stringstream ss;
	
	for(int i=1; i<=cases; i++)
	{		
		ss.str("");
		list1.clear();
		list2.clear();
		output += "Case #";
		ss << i;		
		output += ss.str();
		output += ": ";
		
		getline(file, line, ' ');
		numRides = atoi(line.c_str());
		getline(file,line,' ');
		maxPeople = atoi(line.c_str());
		getline(file,line,'\n');
		numGroups = atoi(line.c_str());

		for(int x=0; x<numGroups-1; x++)
		{
			getline(file,line,' ');
			list1.push_back(atoi(line.c_str()));
		}
		getline(file,line,'\n');
		list1.push_back(atoi(line.c_str()));
		

		int totalEarned = 0;
		int earnedThisRide = 0;
		bool full = false;
		for(int j=0; j<numRides; j++)
		{	
			full = false;
			while(!full)
			{
				if(!list1.empty() && earnedThisRide + list1[0] <= maxPeople)
				{
					earnedThisRide += list1[0];
					list2.push_back(list1[0]);
					list1.erase(list1.begin());
				}
				else
				{
					full = true;
					totalEarned += earnedThisRide;
					earnedThisRide = 0;
					while(!list2.empty())
					{
						list1.push_back(list2[0]);
						list2.erase(list2.begin());
					}
				}			
			}
			
		}		
		
		ss.str("");
		ss << totalEarned;
		output += ss.str();
		output += '\n';
	}
	file.close();
	outfile.write(output.c_str(),output.length());
		
	return 0;
}

