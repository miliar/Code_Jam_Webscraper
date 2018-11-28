// 3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<string>
#include<iostream>
#include<fstream>
using namespace std;
void find(string p,string s,int startp,int starts,int &r)
{
	if(startp==0)
	{
		r++;
	}
	else
	for(int i=starts;i>=0;--i)
	{
		char a=s[i-1];
		char b=p[startp-1];
		if(a==b)
		{
			find(p,s,startp-1,i-1,r);
		}
	}
}
int main(int argc, char* argv[])
{
	string p="welcome to code jam";
	int num;
	ifstream in("C-small-attempt6.in.txt");
	ofstream out("out.txt");
	in>>num;
	string s;
	getline(in,s);
	for(int i=0;i<num;++i)
	{
	getline(in,s);
	cout<<s<<endl;
	int lenp=p.length();
	int lens=s.length();
	int r=0;
	find(p,s,lenp,lens,r);
	if(r>10000)
		r=r%10000;
	char str[10];
	for(int j=0;j<4;++j)
		str[j]='0';
	itoa(r,str,10);
	out<<"Case #"<<i+1<<": ";
    for(int k=0;k<4-strlen(str);++k)
		out<<'0';
	out<<str;

	out<<endl;
	}


	return 0;
}

