#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<iostream>
#include<fstream>
#include<cstring>
#include<string.h>
using namespace std;
long N1[801],N2[801];
int cmp(const void* a,const void *b) 
	{ 
    long *x=(long*)a; 
    long *y=(long*)b; 
    return *x-*y;  //如果a>b返回正数,如果a<b,返回负数,相等返回0; 
	}      
int main()
	{
	fstream fin,fout;
	fin.open("a.in",ios::in);
	fout.open("a.out",ios::out);
	//qsort(a,n,sizeof(long),comp);
	long casen;
	fin>>casen;
	for(long casei=1;casei<=casen;casei++)
		{
		long n;
		fin>>n;
		for(long i=1;i<=n;i++)
			fin>>N1[i-1];
		for(long i=1;i<=n;i++)
			fin>>N2[i-1];
		qsort((void *)N1,n,sizeof(long),cmp);
		qsort((void *)N2,n,sizeof(long),cmp);
		long sum=0;
		for(int i=0;i<n;i++)
			{
			int j=n-1-i;
			sum+=N1[i]*N2[j];
			}
		fout<<"Case #"<<casei<<": "<<sum<<endl;
		}
	fin.close();
	fout.close();
	return 0;
	}

