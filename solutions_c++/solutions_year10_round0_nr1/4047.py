// gcj_snap.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	
	ifstream inf("A-large(4).in");
	ofstream ouf("A.out");

	int n,k,t,b;

	inf>>t;
	for(int i=0;i<t;i++)
	{
		inf>>n>>k;
		b = ( k % (int)(pow(2.0,n)) )==(int)pow(2.0,n)-1;
		ouf<<"Case #"<<(i+1)<<": "<<(b?"ON":"OFF")<<endl;
	}

	return 0;
}

