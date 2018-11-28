// gwel.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
int N;

int main()
{
	register int i,j,cnt;
	int i1,len,slen;
	char* str=new char[550],*st;
	int **ar;
	ifstream fin("C-large.in");
	ofstream fout("C-output.txt");
	fin>>N;
	st="maj edoc ot emoclew";slen=strlen(st);
	ar=new int*[19];
	for(i=0;i<19;i++)
		ar[i]=new int[510];
	fin.getline(str,50);
	i1=1;
	while(i1<=N)
	{
		fin.getline(str,550);
		len=strlen(str);
		cnt=0;
		for(i=len-1;i>=0;i--)
		{
			if(str[i]=='m')
				cnt++;
			ar[0][i]=cnt;
		}
		for(j=1;j<19;j++)
		{
			cnt=0;
			for(i=len-1;i>=0;i--)
			{
				if(str[i]==st[j])
				{
					cnt+=ar[j-1][i];
					cnt%=10000;
				}
				ar[j][i]=cnt;
			}
		}
		fout<<"Case #"<<i1<<": ";
		fout.fill('0');
		fout.width(4);		
		fout<<cnt<<endl;
		i1++;
	}
	return 0;
}

