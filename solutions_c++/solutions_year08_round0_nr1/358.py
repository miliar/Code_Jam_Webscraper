// GCJ08.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

typedef vector<string>::iterator VI;
typedef vector<int>::iterator II;
int EnginesNum;
vector<string> Engines;
int QueriesNum;
vector<string> Queries;
vector<int> Queries_;

int SwitchCount;
II Ii;
void CountSwitch()
{
	while(Ii!=Queries_.end())
	{
		vector<int> switches;
		for(int i=0;i<EnginesNum;++i)
		{
			II nextsw=find(Ii,Queries_.end(),i);
			int longest=nextsw-Ii;
			if(nextsw==Queries_.end())
				return;
			else
				switches.push_back(longest);
		}
		II m=max_element(switches.begin(),switches.end());
		Ii+=*m;
		SwitchCount++;
	}
}

int _tmain(int argc, char* argv[])
{
	int N;
	cin>>N;
	for(int i=1;i<=N;++i)
	{
		Engines.clear();
		Queries.clear();
		Queries_.clear();
		cin>>EnginesNum;
		for(int j=0;j<EnginesNum;j++)
		{
			string engine;
			do{getline(cin,engine);}while(engine=="");
			Engines.push_back(engine);
		}
		cin>>QueriesNum;
		for(int j=0;j<QueriesNum;j++)
		{
			string querie;
			do{getline(cin,querie);}while(querie=="");
			Queries.push_back(querie);
			VI found=find(Engines.begin(),Engines.end(),querie);
			if(found!=Engines.end())
			{
				int index=found-Engines.begin();
				Queries_.push_back(index);
			}
			else
				Queries_.push_back(-1);
		}
		SwitchCount=0;
		Ii=Queries_.begin();
		CountSwitch();
		cout<<"Case #"<<i<<": "<<SwitchCount<<"\n";
	}
	return 0;
}

