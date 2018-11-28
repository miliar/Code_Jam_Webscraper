// Google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
using namespace std;
struct SnaperADT
{
	int lightcoming;
	int state;
};
int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin=freopen("d:\\A-large.in","rt",stdin);
	FILE* fout=freopen("d:\\a.txt","wt",stdout);
	int tests,snapers;
	long clicks;
	cin>>tests;

	for (int i=0;i<tests;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		cin>>snapers >> clicks;

		bool pass=false;
		int start=1, step=2;
		int snaper=1;
		for ( int c=1 ,start=1; c <= clicks ; ++c )
		{
			int nextone = start + (c-1)*step;
			if ( nextone ==clicks )
			{
				if ( ++snaper > snapers )
				{
					pass=true;
					break;
				}
				c=0;
				start = start*2 +1;
				step *=2;
				pass=true;
				continue;
			}
			else if (nextone > clicks )
			{
				pass=false;
				break;
			}
			
		}
		cout<< (pass ? "ON ":"OFF ")<<endl;

	}

	return 0;
}

 