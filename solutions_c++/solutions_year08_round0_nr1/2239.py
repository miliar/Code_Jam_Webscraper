// coded by Martin Tillmann for the Google Code Jam 08 contest.

#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
string s;
getline(cin ,s);
int cases;
stringstream(s) >> cases;
for(int casecounter=0;casecounter<cases;casecounter++)
	{
	int erg=0;
	getline(cin,s);
	int numEngines;
	stringstream(s) >> numEngines;
	string Engines[numEngines];
	bool used[numEngines];
	for(int i=0;i<numEngines;i++)
		{
		getline(cin,Engines[i]);
		used[i]=false;
		}
	getline(cin,s);
	int numSearches;
	stringstream(s) >> numSearches;
	for(int i=0;i<numSearches;i++)
		{
		getline(cin,s);
		int h=0;
		for(;h<numEngines;h++)
			{
			if(Engines[h].compare(s)==0) {used[h]=true;break;}
			}
		bool full=true;
		for(int j=0;j<numEngines;j++)
			{
			if(used[j]==false) full=false;
			}
		if(full==true)
			{			
			erg++;
			for(int j=0;j<numEngines;j++)
				{
				used[j]=false;
				}			
			used[h]=true;
			}
		}
	cout << "Case #" << casecounter+1 << ": " << erg << "\n";
	}
return 0;
}
