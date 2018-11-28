// Google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "search.H"
#include<iostream>
#include <string>
#include <vector>
using namespace std;
 struct tagsnaper
{
	int lightcoming;
	int state;
};
int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin=freopen("d:\\a.in","rt",stdin);
	FILE* fout=freopen("d:\\a.out","wt",stdout);
	int tests,snapers;
	tagsnaper snaper[35];
	memset(snaper,0,sizeof(snaper));
	snaper[0].lightcoming=1;
	snaper[0].state=1;
	snaper[1].lightcoming=1;

	long clicks;

	cin>>tests;


	for (int i=0;i<tests;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		cin>>snapers >> clicks;

	memset(snaper,0,sizeof(snaper));
	snaper[0].lightcoming=1;
	snaper[0].state=1;
	snaper[1].lightcoming=1;
		for (long l=0;l<clicks;++l)
		{
			for ( int s=1;s<=snapers; ++s )
			{
				if ( snaper[s].lightcoming )
					snaper[s].state = !(snaper[s].state );
				else
					break;

			}

			for ( int s=1;s<=snapers; ++s )
			{
				if ( snaper[s-1].lightcoming && snaper[s-1].state)
					snaper[s].lightcoming=1;
				else
				{
					snaper[s].lightcoming=0;
					break;
				}
			}

		}

		bool lightbroken=true;
		for ( int s=1;s<=snapers; ++s )
		{
			if (snaper[s].lightcoming==0 || snaper[s].state==0 )
			{
				cout<<"OFF "<<endl;
				lightbroken=true;
				break;
			}
			else
				lightbroken=false;
		}

		if (lightbroken==false)
			cout<<"ON "<<endl;

	}

	return 0;
}

 