// Google1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;
long long nums=0;
long long posit;
long long mas[100];
long long sum(int i,int j)
{
	long long s=mas[i];
	for (int i1=i+1;i1<=j;i1++)
	{
		s=s*10+mas[i1];
	}
	return s;
}
bool ugly(long long kol)
{
	if (kol==0)
		return true;
	if (kol%2==0)
		return true;
	if (kol%3==0)
		return true;
	if (kol%5==0)
		return true;
	if (kol%7==0)
		return true;
	return false;
}
void run(long long kol,long long pos)
{
	//cout<<kol<<pos<<endl;
	if (pos==posit)
	{
		if(ugly(kol))
			nums++;
		return;
	}
	long long k=kol;
	for (int i=pos;i<posit;i++)
	{
		run(kol+sum(pos,i),i+1);
		run(kol-sum(pos,i),i+1);
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int num;
	in>>num;
	for (int isd=0;isd<num;isd++)
	{
		string s;
		in>>s;
		for (int i=0;i<s.length();i++)
		{
			mas[i]=s[i]-'0';
		}
		posit=s.length();
		nums=0;
		for (int i=0;i<posit;i++)
		{
			//cout<<sum(0,i)<<i+1<<endl;
			run(sum(0,i),i+1);
		}
		out<<"Case #"<<isd+1<<": "<<nums<<endl;
	}
	return 0;
}

