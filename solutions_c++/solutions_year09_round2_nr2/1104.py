//#include "stdafx.h"
#include "iostream"
#include <fstream>
#include <math.h>
using namespace std;

char ar[25];
int call(int a)
{
	char s1[25];
	char min;
	int len=strlen(ar);
	int f=0,i,j;
	for(j=a+1;j<len && ar[j] <=ar[a];j++);
	if(j==len)	return -1;
	min=ar[j];f=j;
	for(;j<len;j++)
	{
		if(ar[j]<min && ar[j] > ar[a])
		{	min=ar[j];f=j;}
	}
	return f;		
}
void call1(char *s)
{
	int len=strlen(s);int i,j;char tmp;
	for(i=0;i<len;i++)
	{
		for(j=i+1;j<len;j++)
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
	int ncase,i1=1;
	int i,j,len,f;
	char tmp;
	fin>>ncase;
	while(i1<=ncase)
	{
		fin>>ar;
		len=strlen(ar);f=0;
		if(len==1)
		{	fout<<"Case #"<<i1<<": "<<ar<<"0"<<endl;f=1;i1++;continue;}
		for(i=len-2;i>=0;i--)
		{
			j=call(i);
			if(j==-1)
			{
		//		continue;
			}
			else
			{
				tmp=ar[j];
				ar[j]=ar[i];
				ar[i]=tmp;
				call1(ar+i+1);
				f=1;
				fout<<"Case #"<<i1<<": "<<ar<<endl;
				break;
			}
		}
		i=90;
		if(f!=1)
		{
			call1(ar);
			for(i=0;ar[i]=='0';i++);
			fout<<"Case #"<<i1<<": ";
			fout<<ar[i];
			for(j=0;j<i;j++)
				fout<<"0";
			fout<<"0";
			fout<<(ar+i+1)<<endl;
		}
		i1++;

	}

	return 0;
}

