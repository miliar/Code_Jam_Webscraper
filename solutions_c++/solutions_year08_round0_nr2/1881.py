// TrainTimetable.cpp : Defines the entry point for the console application.
//

/*
Case #1: 0 2
Case #2: 1 0
Case #3: 2 0
Case #4: 4 2
Case #5: 2 2
Case #6: 2 3
Case #7: 4 4
Case #8: 2 9
Case #9: 13 1
Case #10: 9 5
Case #11: 7 7
Case #12: 1 1
Case #13: 2 0
Case #14: 2 5
Case #15: 14 0
Case #16: 1 9
Case #17: 6 10
Case #18: 2 2
Case #19: 4 3
Case #20: 3 8
*/

#include "stdafx.h"
#include <fstream>
#include <iostream>

//#define	FILENAME_IN	"example.in"
//#define FILENAME_OUT "example.out"

//#define	FILENAME_IN	"B-small-attempt0.in"
//#define FILENAME_OUT "B-small-attempt0.out"

#define	FILENAME_IN	"B-small-attempt1.in"
#define FILENAME_OUT "B-small-attempt1.out"

typedef unsigned char BYTE;

using namespace std;

enum TripTo
{
	TT_ToB,
	TT_ToA,
	TT_NotDefined = -1
};

struct Ticket
{
	Ticket()
	{
		to = TT_NotDefined;
		s = -1;
		e = -1;
		processed = false;
	}

	Ticket( TripTo to, int s, int e )
	{
		this->to = to;
		this->s = s;
		this->e = e;
		processed = false;
	}

	TripTo to;
	int s;
	int e;
	bool processed;
};

void sortTickets( Ticket* t, int n )
{
	for ( int i=1; i<n; i++ )
	{
		for ( int j=i+1; j<=n; j++ )
		{
			if ( t[i].e > t[j].e )
			{
				Ticket tmp = t[j];
				t[j] = t[i];
				t[i] = tmp;
			}
			else if ( t[i].e == t[j].e && t[i].s > t[j].s )
			{
				Ticket tmp = t[j];
				t[j] = t[i];
				t[i] = tmp;
			}
		}
	}
}

void sortTickets2( Ticket* t, int n )
{
	for ( int i=1; i<n; i++ )
	{
		for ( int j=i+1; j<=n; j++ )
		{
			if ( t[i].s > t[j].s )
			{
				Ticket tmp = t[j];
				t[j] = t[i];
				t[i] = tmp;
			}
			else if ( t[i].s == t[j].s && t[i].e > t[j].e )
			{
				Ticket tmp = t[j];
				t[j] = t[i];
				t[i] = tmp;
			}
		}
	}
}

void go( Ticket* tickets, int t, int n, int s )
{
	int nextStartTime = tickets[s].e + t;
	tickets[s].processed = true;
	TripTo to = tickets[s].to;

#ifdef _DEBUG
	cout << tickets[s].e << " ";
#endif

	// sorting
	sortTickets2( tickets, n );

	for ( int i=1; i<=n; i++ )
	{
		if ( tickets[i].s >= nextStartTime 
			&& tickets[i].to != to 
			&& tickets[i].processed == false )
		{
			go( tickets, t, n, i );
			break;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile( FILENAME_IN );
	ofstream outfile( FILENAME_OUT );

	int n;
	infile >> n;

	for ( int c=1; c<=n; c++ )
	{
		int t;
		infile >> t;

		int na, nb;
		infile >> na >> nb;

		char szTmp[128];
		infile.getline( szTmp, 127 );
		Ticket tickets[256];
		int iTmp, iTmp2;
		TripTo ttTmp;
		for ( int i=1; i<=na + nb; i++ )
		{
			infile.getline( szTmp, 127, ':' );
			iTmp = atoi( szTmp ) * 60;	// min
			infile.getline( szTmp, 127, ' ' );
			iTmp += atoi( szTmp );		// sec

			infile.getline( szTmp, 127, ':' );
			iTmp2 = atoi( szTmp ) * 60;	// min
			infile.getline( szTmp, 127 );
			iTmp2 += atoi( szTmp );		// sec

			if ( i <= na ) ttTmp = TT_ToB;
			else ttTmp = TT_ToA;

			tickets[i] = Ticket( ttTmp, iTmp, iTmp2 );
		}

		// go
		int iFromA = 0, iFromB = 0;
		for ( int i=1; i<=na + nb; i++ )
		{
			// sorting
			sortTickets( tickets, na + nb );

			if ( tickets[i].processed == false )
			{
				if ( tickets[i].to == TT_ToB )	iFromA++;
				else							iFromB++;

				go( tickets, t, na + nb, i );
#ifdef _DEBUG
				cout << "  " << iFromA << " " << iFromB << endl;
#endif
			}
		}
#ifdef _DEBUG
		cout << endl;
#endif
		// print results
		outfile << "Case #" << c << ": " << iFromA << " " << iFromB << endl;
	}

	outfile.close();
	infile.close();

	return 0;
}

