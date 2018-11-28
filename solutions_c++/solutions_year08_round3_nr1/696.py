#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<cstring>
#include<cmath>
#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;
int cmp(const void* a,const void *b) 
	{ 
    long *x=(long*)a; 
    long *y=(long*)b; 
    return *y-*x;  //如果a>b返回正数,如果a<b,返回负数,相等返回0; 
	}     
long long sq[101];
int main()
	{
	fstream fin,fout;
	fin.open("a.in",ios::in);
	fout.open("a.out",ios::out);
	int casen;
	fin>>casen;
	for(int casei=1;casei<=casen;casei++)
		{
		long P,K,L;
		fin>>P>>K>>L;
		for(int i=0;i<L;i++)
			fin>>sq[i];
		qsort((void *)sq,L,sizeof(long long),cmp);
		long long sum=0;
		long pos=0;
		for(int i=1;i<=P&&pos<L;i++)
			for(int j=1;j<=K&&pos<L;j++)
				sum+=sq[pos++]*i;
		fout<<"Case #" << casei << ": " << sum << endl;
		}
	fin.close();
	fout.close();
	return 0;
	}
