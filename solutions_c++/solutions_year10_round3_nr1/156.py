// google A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	ifstream fin("A-large.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);

	int c,cc;
	long i,j,n,count;
	int a[1001][2];

	fin>>c;
	for (cc=1;cc<=c;cc++)
	{
		fin>>n;
		count=0;
		for (i=0;i<n;i++)
		{
			fin>>a[i][0]>>a[i][1];
			for (j=i-1;j>=0;j--)
				if ((a[i][0]-a[j][0])*(a[i][1]-a[j][1])<0) count++;
		}
		fout<<"Case #"<<cc<<": ";
		fout<<count<<endl;
	}
	return 0;
}

