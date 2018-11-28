// tri.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <math.h>
#include <string.h>
using namespace std;

int n,s,q;
char S[100][100];
char Q[1000][100];

int end(int eng,int start)
{
	int count = 0;
	while(start<q)
	{
		if( !strcmp(S[eng],Q[start]) )
			break;
		count++;
		start++;	
	}
	return start;
}

int value(int eng,int start)
{
	int count = 0;
	while(start<q)
	{
		if( !strcmp(S[eng],Q[start]) )
			break;
		count++;
		start++;	
	}
	return count;
}
int maxvalue(int start)
{
	int max = 0,v=-1;
	
	for(int i=0;i<s;i++)
	{
		int a = value(i,start);
		if(a >= max)
		{
			max = a;
			v = i;		
		}	
	}
	return v;

}
int _tmain(int argc, _TCHAR* argv[])
{
	
	char temp[100];
	ifstream obj1("A-small.in");
	ofstream obj2("A-small.out");
	obj1.getline(temp,100);
	n = atoi(temp);		
	
	int count = 1;
	while(n--)
	{
		
		obj2<<"Case #"<<count++<<": ";
		obj1.getline(temp,100);
		s = atoi(temp);		
		for(int i=0;i<s;i++)
		{
			obj1.getline(S[i],100);
		}
		obj1.getline(temp,100);
		q = atoi(temp);				
		for(int i=0;i<q;i++)
		{
			obj1.getline(Q[i],100);			
		}
		int sw = 0,e = 0,start=0;

		int max	= maxvalue(start);
		start = end(max,start);

		while(start!=q)
		{
			sw++;
			max	= maxvalue(start);
			start = end(max,start);		
		}
		obj2<<sw<<"\n";


	}

	return 0;
}

