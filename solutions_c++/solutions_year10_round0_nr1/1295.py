// google-A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int t,c,n,bl;
	long k;
	ifstream fin("A-large.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);

	fin>>t;
	for(c=1;c<=t;c++)
	{
		fin>>n>>k;
		bl=1;
		while(n>0)
		{
			if (k%2==1)
			{
				n--;
				k=k/2;
			}
			else 
			{
				bl=0;
				break;
			}
		}
		if (bl==0)
		{
			fout<<"Case #"<<c<<": OFF"<<endl;
		}
		if (bl==1)
		{
			fout<<"Case #"<<c<<": ON"<<endl;
		}
	}
	return 0;
}

