#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<int(b);++i)
#define SZ(v) ((int)v.size())
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define ALL(v) (v).begin(),(v).end()
#define SS stringstream
#define VI vector<int>
#define VS vector<string>
#define PB push_back

#define TOA 0
#define TOB 1

int T;
int NA,NB;
int N;
vector <pair<int,int> > AtoB;
vector <pair<int,int> > BtoA;

int decode(string s)
{
	SS ss(s);
	int hour;
	ss>>hour;
	int min;
	char c;
	ss>>c;
	ss>>min;
	return hour*60+min;
}

int myfind(const vector<pair<int,int> >&v,int dep)
{
	int i;
	for(i=0;i<SZ(v);i++)
		if(v[i].first>=dep)
			break;
	return i;
}

void go(int dir,int dep)
{
	int k;
	if(dir==TOB)
	{
		if((k=myfind(BtoA,dep))==BtoA.size())
			return;
		
		int dp=BtoA[k].second+T;
		BtoA.erase(BtoA.begin()+k);
		go(TOA,dp);
		return;
	}
	else
	{
		if((k=myfind(AtoB,dep))==AtoB.size())
			return;
		int dp=AtoB[k].second+T;
		AtoB.erase(AtoB.begin()+k);
		go(TOB,dp);
		return;
	}
}


int main()
{
freopen ("B-large.in","r",stdin);
freopen ("out.txt","w",stdout);
	
	cin>>N;
	FOR(kk,0,N)
	{
		
		cin>>T;
		
		cin>>NA>>NB;
		
		AtoB.clear();
		BtoA.clear();

		FOR(i,0,NA)
		{
			string s;
			cin>>s;
			int departure=decode(s);
			cin>>s;
			int arrival=decode(s);
			AtoB.PB(make_pair(departure,arrival));
		}

		FOR(i,0,NB)
		{
			string s;
			cin>>s;
			int departure=decode(s);
			cin>>s;
			int arrival=decode(s);
			BtoA.PB(make_pair(departure,arrival));
		}
		sort(ALL(AtoB));
		sort(ALL(BtoA));

		int fromA=0,fromB=0;
		while(AtoB.size()!=0||BtoA.size()!=0)
		{
			if(AtoB.size()==0)
			{
				fromB+=BtoA.size();
				break;
			}
			if(BtoA.size()==0)
			{
				fromA+=AtoB.size();
				break;
			}
			if(AtoB[0].first<=BtoA[0].first)
			{
				fromA++;			
				go(TOB,AtoB[0].second+T);
				AtoB.erase(AtoB.begin());
			}
			else
			{
				fromB++;
				go(TOA,BtoA[0].second+T);
				BtoA.erase(BtoA.begin());
			}

		}




		cout<<"Case #"<<kk+1<<": "<<fromA<<" "<<fromB<<endl;    


	}
	return 0;
}

