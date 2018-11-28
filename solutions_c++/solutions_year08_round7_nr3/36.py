// C.cpp : Defines the entry point for the console application.
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

double s[1000000];

void process(int num)
{
	double a[10][4];
	int m,q;
	cin>>m>>q;

	for(int i=0;i<q;i++)
		for(int j=0;j<4;j++) 
			cin>>a[i][j];

	for(int i=0;i<(1<<(q*2));i++)
	{
		int now=i;
		double val=1.0;
		for(int j=0;j<q;j++)
		{
			int id=(now&3);
			val*=a[j][id];
			now=now>>2;
		}
		s[i]=val;
	}

	sort(s,s+(1<<(q*2)),greater<double>());
	double ans=0.0;
	if(m>(1<<(q*2))) m=(1<<(q*2));
	for(int i=0;i<m;i++) ans+=s[i];
	cout<<"Case #"<<num<<": "<<ans<<endl;
}

int main(void)
{
	int num;
	cin>>num;
	for(int i=1;i<=num;i++) process(i);
	return 0;
}
