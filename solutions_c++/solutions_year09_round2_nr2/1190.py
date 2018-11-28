// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <assert.h>
using namespace std;

//const char* inFileName="B-small-attempt0.in";
//const char* outFileName("B-small-attempt0.out");

const char* inFileName="B-large.in";
const char* outFileName("B-large.out");


int num(char c) {return c-'0';}
char chr(int i) {return i+'0';}

void microsort(ostream &out,char *s)
{
	//out<<"*";
	int count[10]={0,0,0,0,0,0,0,0,0,0};//0x10times
	char *cur=s;
	while(*cur)
	{
		++count[num(*cur)];
		++cur;
	}
	
	int new_first_numb=-1;;
	for (int i=num(s[0])+1;i<=9;++i)
		if (count[i]>0)
		{
			new_first_numb=i;
			break;
		}
	assert(new_first_numb!=-1);
	
	out<<new_first_numb;
	--count[new_first_numb];
	
	int i=0;
	while(i<=9)
	{
		if (count[i]==0)
			++i;
		else
		{
			out<<i;
			--count[i];
		}
	}
}

void print_next(ostream &out,char *s,int len)
{
	for (int i=len-1;i>=1;--i)
	{
		assert(s[i]>='0' && s[i]<='9');
		if (s[i]>s[i-1])
		{
			char t=s[i-1];
			s[i-1]=0;out<<s;
			s[i-1]=t;microsort(out,s+i-1);
			return;
		}
	}

	if (true)//if we are here
	{
		int n0=0;
		//char *cur=s+len-1;
		while (*(s+len-1-n0)=='0') 
			++n0;
		++n0;//it's new 0
		out<<s[len-n0];
		for (int i0=0;i0<n0;++i0)
			out<<'0';
		for (int i=len-n0-1;i>=0;--i)
			out<<s[i];
	}
}

int main()
{
	ifstream fin(inFileName);
	ofstream fout(outFileName);
	//ostream &fout=cout;
	int T;
	fin>>T;
	assert(fin.good());

	char buf[30+1];int len;
	fin.getline(buf,1);assert(buf[0]==0);
	for (int t=1;t<=T;++t)
	{
		cout<<"dbg:case="<<t<<'\n';
		fin.getline(buf,30);
		len=strlen(buf);
		assert(len<=21);
		fout<<"Case #"<<t<<": ";
		print_next(fout,buf,len);
		fout<<'\n';
	}
	
	cout<<"\7\7\7";
	fout.close();
	int k;cin>>k;
	return 0;
}

