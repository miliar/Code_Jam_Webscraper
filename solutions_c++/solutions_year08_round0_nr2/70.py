// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

class Tline
{
public:
	char type;
	int ts,te;
};

bool compare(Tline &la,Tline &lb)
{
	return la.ts<lb.ts;
}

int calcminu(string s)
{
	return ((s[0]-'0')*10+(s[1]-'0'))*60+((s[3]-'0')*10+(s[4]-'0'));
}

void process(int num)
{
	int na,nb,T;
	int sa[2000],sb[2000];
	Tline ls[500];
	int id=0;

	cin>>T>>na>>nb;
	memset(sa,0,sizeof(sa));
	memset(sb,0,sizeof(sb));
	for(int i=0;i<na;i++)
	{
		string ss,se;
		cin>>ss>>se;
		ls[id].type='A';ls[id].ts=calcminu(ss);ls[id].te=calcminu(se);
		id++;
	}
	for(int i=0;i<nb;i++)
	{
		string ss,se;
		cin>>ss>>se;
		ls[id].type='B';ls[id].ts=calcminu(ss);ls[id].te=calcminu(se);
		id++;
	}
	sort(ls,ls+id,compare);

	int ra=0,rb=0,pa=0,pb=0;
	for(int i=0;i<id;i++)
	{
		if(i>0)
		{
			for(int j=ls[i-1].ts+1;j<=ls[i].ts;j++)
			{
				pa+=sa[j];
				pb+=sb[j];
			}
		}

		if(ls[i].type=='A')
		{
			if(pa>0) pa--;
			else ra++;
			sb[ls[i].te+T]++;
		}

		if(ls[i].type=='B')
		{
			if(pb>0) pb--;
			else rb++;
			sa[ls[i].te+T]++;
		}
	}

	cout<<"Case #"<<num<<": "<<ra<<" "<<rb<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}

