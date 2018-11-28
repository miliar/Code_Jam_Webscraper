#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
using namespace std;
int N,S,P;
int table[10000];
int main()
{
	int t;
	ifstream fin("./in");
	ofstream fout("./out");
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>N>>S>>P;
		int so=0;
		int result=0;
		for(int j=0;j<N;j++)
		{
			fin>>table[j];
		}
		for(int j=0;j<N;j++)
		{
			if(table[j]%3==0)
			{
				if(table[j]/3>=P)
					result++;
				else if(table[j]>2&&(table[j]-3)/3>=P-2)
					so++;
			}
			if(table[j]%3==1)
			{
				if(table[j]/3>=P-1)
					result++;
			}
			if(table[j]%3==2)
			{
				if((table[j]-2)/3>=P-1)
					result++;
				else if((table[j]-2)/3>=P-2)
					so++;
			}
			
		}
		so=so>S? S:so;
		fout<<"Case #"<<i+1<<": "<<result+so<<endl;

	}
	return 1;
}
