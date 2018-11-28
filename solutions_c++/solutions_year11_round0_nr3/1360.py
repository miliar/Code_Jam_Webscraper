//============================================================================
// Name        : codejam.cpp
// Author      : Zn
// Version     :
// Copyright   : NULL
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int m,n;
int table[10000];
int cmp(const void *a,const void *b)
{
	return *(int *)a>*(int *)b? -1:1;
}
int main() {
	ifstream fin("test.in");
	ofstream fout("test.out");
	fin>>m;
	for(int i=0;i<m;i++)
	{
		fin>>n;
		int yi=0;
		for(int j=0;j<n;j++)
		{
			fin>>table[j];
		}
		yi=table[0];
		for(int j=1;j<n;j++)
		{
			yi^=table[j];
		}

		if(yi!=0)
		{
			fout<<"Case #"<<i+1<<": NO"<<endl;
			continue;
		}
		qsort(table,n,sizeof(int),cmp);
		for(int i=0;i<n-1;i++)
		{
			yi+=table[i];
			//cout<<table[i];
		}
		fout<<"Case #"<<i+1<<": "<<yi<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}
