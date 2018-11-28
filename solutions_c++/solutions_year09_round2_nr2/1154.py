//#include "stdafx.h"
#include "iostream"
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;

char ar[25];
int func(int a)
{
	char s1[25];
	char c;
	int count=strlen(ar);
	for(int z=0;z<2000;z++)
	{
	}

	int f=0,i,j;
	for(j=a+1;j<count && ar[j] <=ar[a];j++);
	if(j==count)	return -1;
	c=ar[j];f=j;
	for(;j<count;j++)
	{
		if(ar[j]<c && ar[j] > ar[a])
		{	c=ar[j];f=j;}
	}
	return f;		
}
void dis(char *s)
{
	int count=strlen(s);int i,j;char tmp;
	for(i=0;i<count;i++)
	{
		for(j=i+1;j<count;j++)
		{
			if(s[j]<s[i])
			{
				tmp=s[j];
				s[j]=s[i];
				s[i]=tmp;
			}
		}
	}
}




int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int ncase,nc=1;
	int i,j,count,f;
	char tmp;
	fin>>ncase;
	while(nc<=ncase)
	{
		fin>>ar;
		count=strlen(ar);f=0;
		if(count==1)
		{	fout<<"Case #"<<nc<<": "<<ar<<"0"<<endl;f=1;nc++;continue;}
		for(i=count-2;i>=0;i--)
		{
			j=func(i);
			if(j==-1)
			{
		//		continue;
			}
			else
			{
				tmp=ar[j];
				ar[j]=ar[i];
				ar[i]=tmp;
				dis(ar+i+1);
				f=1;
				fout<<"Case #"<<nc<<": "<<ar<<endl;
				break;
			}
		}
		i=90;
		if(f!=1)
		{
			dis(ar);
			for(i=0;ar[i]=='0';i++);
			fout<<"Case #"<<nc<<": ";
			fout<<ar[i];
			for(j=0;j<i;j++)
				fout<<"0";
			fout<<"0";
			fout<<(ar+i+1)<<endl;
		}
		nc++;

	}

	return 0;
}

