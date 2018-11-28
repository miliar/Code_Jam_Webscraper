#include "stdafx.h"
#include <iostream>
#include<fstream>
using namespace std;
int rot(int,int);
void main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int re_cycle(int,int);
	
	int t,a,b,cnt;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>a>>b;
		cnt = 0;
		do
		{
			cnt += re_cycle(a,b);
			a++;
		}
		while(a<=b);
		fout<<"Case #"<<i+1<<": ";
		fout<<cnt<<'\n';
	}
	
}
int re_cycle(int a, int b)
{
	int temp,len,cnt,spl[20],flag=0;
	
	if(a<10)
		return 0;
	temp=a;
	len = 0;
	cnt = 0;
	while(temp>0)
	{
		temp=temp/10;
		len++;
	}
	temp = a;
	
	for(int i =0;i<(len-1);i++)
	{
		spl[i]=temp;
		temp = rot(temp,len);
		for(int k=0;k<=i;k++)
		{
			if(spl[k]==temp)
				flag=1;
		}
		if(flag==1)
			continue;
		if(temp<=b && temp>a)
		{
			cnt++;
		}
	}
	return cnt;
}
int rot(int a,int len)
{
	int x,mul;
	mul=1;
	for(int i=0;i<len-1;i++)
		mul=mul*10;
	x = a%10;
	a = a/10;
	x = x*mul;
	x = x+a;
	return x;
}

