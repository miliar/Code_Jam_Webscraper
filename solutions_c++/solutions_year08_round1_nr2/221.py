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

int a[200][20];

void process(int num)
{
	int n,m,t;
	cin>>n>>m;
	memset(a,0xff,sizeof(a));
	for(int i=0;i<m;i++)
	{
		cin>>t;
		for(int j=0;j<t;j++)
		{
			int x,y;
			cin>>x>>y;
			a[i][x-1]=y;
		}
	}

	bool possible=false;
	int best=1000000,val;
	for(int i=0;i<(1<<n);i++)
	{
		int j;
		for(j=0;j<m;j++)
		{
			int k;
			for(k=0;k<n;k++) if(a[j][k]==((i>>k)&1)) break;
			if(k==n) break;
		}
		if(j==m)
		{
			possible=true;
			int sum=0;
			for(int p=0;p<n;p++) sum+=((i>>p)&1);
			if(sum<best)
			{
				best=sum;
				val=i;
			}
		}
	}

	if(possible==false)
	{
		cout<<"Case #"<<num<<": "<<"IMPOSSIBLE"<<endl;
	}
	else
	{
		cout<<"Case #"<<num<<":";
		for(int p=0;p<n;p++) cout<<" "<<((val>>p)&1);
		cout<<endl;
	}
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}

