// codejam2.cpp : 定义控制台应用程序的入口点。
#include "stdafx.h"
#include <bitset>
#include <iostream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int testcase;
	cin>>testcase;
	fstream f("c:\\output4.txt");
	for(int i=0; i<testcase; ++i)
	{
		int n, k;
		cin>>n>>k;
		bitset<30> b(k);
		bool flag=true;
		for(int j=0;j<n;++j)
		{
			if(b[j] == 0)
			{
				flag=false;
				break;
			}

		}
		
		if (flag)
			f<<"Case #"<<i+1<<": ON"<<endl;
		else
			f<<"Case #"<<i+1<<": OFF"<<endl;
	}
	return 0;
}


