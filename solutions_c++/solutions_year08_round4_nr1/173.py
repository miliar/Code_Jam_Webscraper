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

int g[50000][2],a[50000][2];

void process(int num)
{
	int M,V;
	cin>>M>>V;
	int n=(M-1)/2,m=(M+1)/2;

	for(int i=1;i<=n;i++) cin>>g[i][0]>>g[i][1];
	for(int i=0;i<m;i++)
	{
		int val;
		cin>>val;
		a[n+1+i][val]=0;
		a[n+1+i][1-val]=100000;
	}

	for(int i=n;i>=1;i--)
	{
		int l=2*i,r=2*i+1;
		int nand=(g[i][0]==1?0:(g[i][1]==1?1:100000));
		int nor=(g[i][0]==0?0:(g[i][1]==1?1:100000));

		a[i][0]=a[i][1]=100000;
		if(nand!=-1)
		{
			int n0,n1;
			n1=a[l][1]+a[r][1]+nand;
			if(n1<a[i][1]) a[i][1]=n1;
			n0=a[l][0]+a[r][1]+nand;
			if(n0<a[i][0]) a[i][0]=n0;
			n0=a[l][1]+a[r][0]+nand;
			if(n0<a[i][0]) a[i][0]=n0;
			n0=a[l][0]+a[r][0]+nand;
			if(n0<a[i][0]) a[i][0]=n0;
		}
		if(nor!=-1)
		{
			int n0,n1;
			n1=a[l][1]+a[r][1]+nor;
			if(n1<a[i][1]) a[i][1]=n1;
			n1=a[l][0]+a[r][1]+nor;
			if(n1<a[i][1]) a[i][1]=n1;
			n1=a[l][1]+a[r][0]+nor;
			if(n1<a[i][1]) a[i][1]=n1;
			n0=a[l][0]+a[r][0]+nor;
			if(n0<a[i][0]) a[i][0]=n0;
		}
	}

	if(a[1][V]<100000)
		cout<<"Case #"<<num<<": "<<a[1][V]<<endl;
	else
		cout<<"Case #"<<num<<": "<<"IMPOSSIBLE"<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}