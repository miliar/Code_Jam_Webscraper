// SavingTheUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

//#define	FILENAME_IN	"example.in"
//#define FILENAME_OUT "example.out"

//#define	FILENAME_IN	"A-small-attempt0.in"
//#define FILENAME_OUT "A-small-attempt0.out"

//#define	FILENAME_IN	"A-small-attempt1.in"
//#define FILENAME_OUT "A-small-attempt1.out"

#define	FILENAME_IN	"A-large.in"
#define FILENAME_OUT "A-large.out"

typedef unsigned char BYTE;

using namespace std;


//////////////////////////////////////////////////////////////////////////
int searching( int numOfSearchEngines, int numOfQueries, BYTE q[] )
{
#ifdef _DEBUG
	cout << "start" << endl;
#endif
	int numOfSwitches = 0;
	int s = 0;

	int startIdx = 1;

	while ( startIdx <= numOfQueries )
	{
		numOfSwitches++;

		bool flag[128] = { 0, };
		int cnt = 0;
		int bestSearchEngine = 0;
		int i;
		for ( i=startIdx; i<=numOfQueries; i++ )
		{
#ifdef _DEBUG
			cout << (int)q[i] << endl;
#endif

			if ( flag[ q[i] ] == false )
			{
				flag[ q[i] ] = true;
				cnt++;

				if ( cnt == numOfSearchEngines )
				{
					bestSearchEngine = q[i];
#ifdef _DEBUG
					cout << "-- " << bestSearchEngine << endl;
#endif
					break;
				}
			}
		}

		startIdx = i;

		if ( bestSearchEngine == 0 )
		{
#ifdef _DEBUG
			for ( int i=1; i<numOfSearchEngines; i++ )
			{
				if ( flag[i] == false )
				{

					bestSearchEngine = i;
					cout << "-- " << bestSearchEngine << endl;
					break;
				}
			}
#endif
			break;
		}
	}

	return numOfSwitches-1;
}


//////////////////////////////////////////////////////////////////////////
int _tmain(int argc, _TCHAR* argv[])
{
	int n;	// number of cases

	ofstream outfile(FILENAME_OUT);

	ifstream infile(FILENAME_IN);
	infile >> n;

	for ( int i=1; i<=n; i++ )
	{
		int s;	// number of search engines
		infile >> s;

		char searchEngines[128][128];
		infile.getline( searchEngines[0], 127 );
		for ( int j=1; j<=s; j++ )
		{
			infile.getline( searchEngines[j], 127 );

			/*for ( int k=1; k<j; k++ )
			{
				if ( strcmp(searchEngines[j], searchEngines[k]) == 0 )
				{
					j--;
					s--;
				}
			}*/
		}

		int q;	// number of queries
		infile >> q;

		char queries[1024][128];
		BYTE byQueries[1024];
		infile.getline( queries[0], 127 );
		for ( int j=1; j<=q; j++ )
		{
			infile.getline( queries[j], 127 );

			for ( int k=1; k<=s; k++ )
			{
				if ( strcmp(queries[j], searchEngines[k]) == 0 )
				{
					byQueries[j] = k;
					break;
				}
			}
		}

		// get result
		int res = searching( s, q, byQueries );
		if ( res < 0 ) res = 0;
		outfile << "Case #" << i << ": " << res << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}

