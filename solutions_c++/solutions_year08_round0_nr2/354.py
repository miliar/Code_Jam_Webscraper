// GCJ08b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream> 

using namespace std;


int nA;
int nB;

int tT;
int NumA;
int NumB;

typedef vector<int>::iterator II;
vector<int> startA;
vector<int> canstartB;
vector<int> startB;
vector<int> canstartA;


void ReadTimes(int& aStart, int& aArrives)
{
		string line; 
        do 
        { 
                getline(cin,line); 
        } 
        while(line==""); 
		stringstream linestream; 
        linestream<<line; 
		string time;
		while(!linestream.eof()) 
        { 
                linestream>>time; 
                int pos=time.find(':'); 
				int hh,mm;
				sscanf(time.substr(0,pos).c_str(),"%d",&hh); 
				sscanf(time.substr(pos+1).c_str(),"%d",&mm); 
				aStart=60*hh+mm;

				linestream>>time; 
				pos=time.find(':');
				sscanf(time.substr(0,pos).c_str(),"%d",&hh); 
				sscanf(time.substr(pos+1).c_str(),"%d",&mm); 
				aArrives=60*hh+mm;
				return;
		}
}

void Calculate()
{
	int inA=0;
	int inB=0;
	for(int i=0;i<3600;++i)
	{
		pair<II,II> ca=equal_range(canstartA.begin(),canstartA.end(),i);
		pair<II,II> s=equal_range(startA.begin(),startA.end(),i);
		inA+=ca.second-ca.first;
		inA-=s.second-s.first;
		if(inA<0)
		{
			nA-=inA;//add abs(inA), the trains we need to start
			inA=0;
		}
	}
	for(int i=0;i<3600;++i)
	{
		pair<II,II> ca=equal_range(canstartB.begin(),canstartB.end(),i);
		pair<II,II> s=equal_range(startB.begin(),startB.end(),i);
		inB+=ca.second-ca.first;
		inB-=s.second-s.first;
		if(inB<0)
		{
			nB-=inB;//add abs(inA), the trains we need to start
			inB=0;
		}
	}

}

int _tmain(int argc, char* argv[])
{
	int N;
	cin>>N;
	for(int i=1;i<=N;++i)
	{
		startA.clear();
		canstartB.clear();
		startB.clear();
		canstartA.clear();
		nA=nB=0;

		cin>>tT;
		cin>>NumA>>NumB;
		for(int j=0;j<NumA;++j)
		{
		int s,a;
		ReadTimes(s,a);
		a+=tT;
		startA.push_back(s);
		canstartB.push_back(a);//mod3600?
		}
		sort(startA.begin(),startA.end());
		sort(canstartB.begin(),canstartB.end());
		for(int j=0;j<NumB;++j)
		{
		int s,a;
		ReadTimes(s,a);
		a+=tT;
		startB.push_back(s);
		canstartA.push_back(a);//mod3600?
		}
		sort(startB.begin(),startB.end());
		sort(canstartA.begin(),canstartA.end());
		Calculate();
		cout<<"Case #"<<i<<": "<<nA<<" "<<nB<<"\n";
	}
	return 0;
}

