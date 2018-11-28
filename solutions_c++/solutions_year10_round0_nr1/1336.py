// google-A edit.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;

struct key
{
	long divisor;
	long remainder;
};

int _tmain(int argc, _TCHAR* argv[])
{
	int i,t,c,n;
	key a[31];
	long k;
	ifstream fin("A-large.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);

	a[0].divisor=1;
	a[0].remainder=0;
	for (i=1;i<=30;i++)
	{
		a[i].divisor=a[i-1].divisor*2;
		a[i].remainder=a[i].divisor-1;
	}
	fin>>t;
	for(c=1;c<=t;c++)
	{
		fin>>n>>k;
		if (k%a[n].divisor==a[n].remainder)
		{
			fout<<"Case #"<<c<<": ON"<<endl;
		}
		else
		{
			fout<<"Case #"<<c<<": OFF"<<endl;
		}
	}
	return 0;
}

