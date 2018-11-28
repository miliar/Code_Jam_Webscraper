// Practice.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include "fstream"
#include "iostream"
using namespace std;
int snapperChain(unsigned long N, unsigned long K)
{
	unsigned long t = 1, b;
	for(int i = 0; i < N; i++)
	{
		b = (K & t);
		if ( b == 0 )
		{
			//Light is off
			return 0;
		}
		t = t << 1;			
	}
	//Light is on
	return 1;
}


int _tmain(int argc, _TCHAR* argv[])
{
	if(argc < 2)
	{
		cout<<"Provide the input file name";
		return 0;
	}
	ifstream fin(argv[1]);
	unsigned long N,K,T;
	fin>>T;

	for ( int i=1; i<=T; i++)
	{
		fin>>N>>K;
		cout<<"Case #"<<i<<": "<<((snapperChain(N,K) == 0)? "OFF" : "ON")<<endl;
	}
	return 0;
}

