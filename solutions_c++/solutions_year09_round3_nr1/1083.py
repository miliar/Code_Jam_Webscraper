// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <assert.h>
#include <cmath>
using namespace std;

//const char* inFileName="A-0small.in";
//const char* outFileName("A-0small.out");
const char* inFileName="A-small-attempt2.in";
const char* outFileName("A-small-attempt2.out");
//const char* inFileName="A-large.in";
//const char* outFileName="A-large.out";

int main()
{
	ifstream fin(inFileName);
	ofstream fout(outFileName);

	int T;
	fin>>T;
	char buf[65];
	fin.getline(buf,65);
	assert(fin.good());


	for (int t=1;t<=T;++t)
	{
		int symbol[256]; 
		fin.getline(buf,65);
		
		//calc base
		char *cur=buf;
		int base=0;
		for (int i=0;i<256;++i) symbol[i]=0;
		while(*cur)
		{
			if (symbol[*cur]==0) 
				++base;
			++symbol[*cur];
			++cur;
		}
		if (base<2) base=2;
		
		//calc Symb
		for (int i=0;i<256;++i) symbol[i]=-1;
		symbol[*buf]=1;
		if (buf[1]!=0)
		{
			char *cur=buf+1;
			int v=0;
			while(*cur)
			{
				if (symbol[*cur]==-1)
					symbol[*cur]=v++;
				if (v==1) 
					v=2;//skip 1
				++cur;
			}
		}
		//calc val
		cur=buf; while(*cur) ++cur;--cur;//cur is last
		long long mult=1;
		long long S=0;
		while(cur>=buf)
		{
			S+=symbol[*cur]*mult;
			mult*=base;

			--cur;
		}

		fout<<"Case #"<<t<<": "<<S<<'\n';

	}
	
	fout.close();
	cout<<"\7\7\7Done";
	
	int k;cin>>k;
	return 0;
}

