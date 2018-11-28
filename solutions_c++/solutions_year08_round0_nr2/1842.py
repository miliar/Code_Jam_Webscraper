// Train.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

struct node 
{
	int time;
	int type;
}; 

vector<node> time;

ofstream of(_T("E:\\out.out"));
int t;

bool lesstime(const node& s1, const node& s2)
{
	if (s1.time < s2.time) return true;
	else if (s1.time == s2.time)
	{
		if (s1.type==2 && s2.type==3) return true;
		if (s1.type==4 && s2.type==1) return true;
	}
	return false;
}

void Process(int c)
{
	sort(time.begin(),time.end(),lesstime);
	int needa=0,needb=0;
	int are=0,bre=0;
	for(int i=0;i<time.size();++i)
	{
		if (time[i].type==1)
		{
			if (are==0) needa++;
			else are--;
		}
		else if (time[i].type==2)
		{
			bre++;
		}
		else if (time[i].type==3)
		{
			if (bre==0) needb++;
			else bre--;
		}
		else if (time[i].type==4)
		{
			are++;
		}
	}
	cout<<"Case #"<<c<<": "<<needa<<" "<<needb<<endl;
	of<<"Case #"<<c<<": "<<needa<<" "<<needb<<endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream file(_T("E:\\B-small-attempt1.in"));
	int n;
	file>>n;
	for(int i=0;i<n;++i)
	{
		time.clear();
		file>>t;
		int na,nb;
		file>>na>>nb;
		for(int i=0;i<na;++i)
		{
			char c;
			int hh1,mm1,hh2,mm2;
			file>>hh1;
			file>>c;
			file>>mm1;
			file>>hh2;
			file>>c;
			file>>mm2;
			node temp;
			temp.time = hh1*60+mm1;
			temp.type = 1;
			time.push_back(temp);
			temp.time = hh2*60+mm2+t;
			temp.type = 2;
			time.push_back(temp);
		}
		for(int i=0;i<nb;++i)
		{
			char c;
			int hh1,mm1,hh2,mm2;
			file>>hh1;
			file>>c;
			file>>mm1;
			file>>hh2;
			file>>c;
			file>>mm2;
			node temp;
			temp.time = hh1*60+mm1;
			temp.type = 3;
			time.push_back(temp);
			temp.time = hh2*60+mm2+t;
			temp.type = 4;
			time.push_back(temp);
		}
		Process(i+1);
	}
	return 0;
}