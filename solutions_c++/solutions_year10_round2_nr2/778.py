// google R1 B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;


struct chick
{
	long l;
	long s,bl;
};
int _tmain(int argc, _TCHAR* argv[])
{
	long c,cc,i,n,k,t,swap,zc,time;
	long b;
	ifstream fin("B-large.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);
	chick a[100];
	fin >> c;
	for (cc=1;cc<=c;cc++)
	{
		fin>>n>>k>>b>>t;
		for (i=1;i<=n;i++)
		{
			fin>>a[n-i].l;
		}
		for (i=1;i<=n;i++)
		{
			fin>>a[n-i].s;
			time=(b-a[n-i].l)/a[n-i].s;
			if ((b-a[n-i].l)%a[n-i].s>0) time++;
			if (time<=t) a[n-i].bl=1;
			else a[n-i].bl=0;
		}
		zc=0; swap=0;
		for (i=0;i<n;i++)
		{
			if (a[i].bl==1)
			{
				k--;
				swap+=zc;
				if (k==0) break;
			}
			if (a[i].bl==0) zc++;
		}
		fout<<"Case #"<<cc<<": ";
		if (k==0) fout<<swap<<endl;
		else fout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}