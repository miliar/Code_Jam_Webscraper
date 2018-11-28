// Universe.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct node
{
	int index;
	int pos;
};

vector<int> query;
vector<string> server;

ofstream of(_T("E:\\out.out"));

void Process(int c)
{
	int switchnum = 0;
	vector<int> v;
	for(int i=0;i<query.size();++i)
	{
		v.push_back(query.size());
	}
	for(int i=0;i<query.size();++i)
	{
		int mins = query.size();
		for(int j=0;j<server.size();++j)
		{
			int k=i;
			while(k>=0 && query[k]!=j) k--;
			if (k==i) continue;
			else if (k>=0 && k<i) 
			{
				if (mins>v[k]+1) mins=v[k]+1;
			}
			else if (k==-1)
			{
				mins=0;
			}
		}
		v[i]=mins;
	}
	if (v.size()) switchnum=v[v.size()-1];
	cout<<"Case #"<<c<<": "<<switchnum<<endl;
	of<<"Case #"<<c<<": "<<switchnum<<endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream file(_T("E:\\A-small-attempt5.in"));
	int n;
	file>>n;
	for(int i=0;i<n;++i)
	{
		int s;
		int q;
		char temp[100];
		server.clear();
		file>>s;
		file.getline(temp,100);
		for(int j=0;j<s;++j)
		{
			file.getline(temp,100);
			server.push_back(temp);
		}
		file>>q;
		file.getline(temp,100);
		query.clear();
		for(int j=0;j<q;++j)
		{
			file.getline(temp,100);
			for(int k=0;k<server.size();++k)
			{
				string t1 = temp;
				string s1 = server[k];
				if (s1.compare(t1)==0)
				{
					query.push_back(k);
					break;
				}
			}
		}
		Process(i+1);
	}
	return 0;
}

