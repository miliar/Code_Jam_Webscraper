// A.cpp : Defines the entry point for the console application.
//

#pragma warning(disable:4786)
#include <stdafx.h>
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

int f(int id,int n,vector<vector<int> > &v)
{
	int cnt=0;
	vector<int> bs;

	for(int i=0;i<v[id].size();i++)
	{
		if(v[id][i]!=-1)
		{
			int now=f(v[id][i],n,v);
			bs.push_back(now);
			cnt++;
		}
	}
	
	sort(bs.begin(),bs.end(),greater<int>());
	int ans=0,lft=0;
	for(int i=0;i<bs.size();i++)
	{
		if(lft>=bs[i])
		{
			lft--;
		}
		else
		{
			ans+=bs[i]-lft;
			lft=bs[i]-1;
		}
	}
	if(lft==0) ans++;
	return ans;
}

void process(int num)
{
	int n;
	vector<string> sv[2000];
	string nm[2000];
	vector<vector<int> > v(2000,vector<int>());

	cin>>n;
	for(int i=0;i<n;i++)
	{
		int m;
		cin>>nm[i]>>m;
		for(int j=0;j<m;j++)
		{
			string tt;
			cin>>tt;
			sv[i].push_back(tt);
		}
	}

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<sv[i].size();j++)
		{
			int k;
			for(k=0;k<n;k++)
				if(nm[k]==sv[i][j])
				{
					v[i].push_back(k);
					break;
				}
			if(k==n) v[i].push_back(-1);
		}
	}

	cout<<"Case #"<<num<<": "<<f(0,n,v)<<endl;
}

int main(void)
{
	int num;
	cin>>num;
	for(int i=1;i<=num;i++) process(i);
	return 0;
}
