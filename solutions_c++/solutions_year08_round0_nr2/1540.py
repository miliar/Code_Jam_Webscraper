// TrainTimetable.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

void getTimesFromStream( std::ifstream& in, int& time1, int& time2 )
{
	const int TIMES_STRING_SIZE = 20;
	char curStr[ TIMES_STRING_SIZE ];		
	char smallStr[ 3 ];

	in.getline( curStr, TIMES_STRING_SIZE );
	smallStr[ 0 ] = curStr[ 0 ];
	smallStr[ 1 ] = curStr[ 1 ];
	smallStr[ 2 ] = 0;
	time1 = atoi( smallStr )*60;

	smallStr[ 0 ] = curStr[ 3 ];
	smallStr[ 1 ] = curStr[ 4 ];
	time1 += atoi( smallStr );

	smallStr[ 0 ] = curStr[ 6 ];
	smallStr[ 1 ] = curStr[ 7 ];
	smallStr[ 2 ] = 0;
	time2 = atoi( smallStr )*60;

	smallStr[ 0 ] = curStr[ 9 ];
	smallStr[ 1 ] = curStr[ 10 ];
	time2 += atoi( smallStr );
}

void getNumTrips( std::ifstream& in, int& a, int& b )
{
	int turnaroundTime;
	int NA;
	int NB;
	in >> turnaroundTime >> NA >> NB;

	std::vector<int> arrivalTimesToA;
	std::vector<int> arrivalTimesToB;
	std::vector<int> departureTimesFromA;
	std::vector<int> departureTimesFromB;
	arrivalTimesToA.reserve( NB );
	arrivalTimesToB.reserve( NA );
	departureTimesFromA.reserve( NA );
	departureTimesFromB.reserve( NB );
	
	const int TMP_STR_SIZE = 20;
	char curStr[ TMP_STR_SIZE ];
	in.getline( curStr, TMP_STR_SIZE );

	for( int i = 0; i < NA; ++i )
	{
		int dTA;
		int aTTB;
		getTimesFromStream( in, dTA, aTTB );
		arrivalTimesToB.push_back( aTTB );
		departureTimesFromA.push_back( dTA );
	}

	for( int i = 0; i < NB; ++i )
	{
		int dTB;
		int aTTA;
		getTimesFromStream( in, dTB, aTTA );
		arrivalTimesToA.push_back( aTTA );
		departureTimesFromB.push_back( dTB );
	}

	sort( arrivalTimesToA.begin( ), arrivalTimesToA.end( ) );
	sort( arrivalTimesToB.begin( ), arrivalTimesToB.end( ) );
	sort( departureTimesFromA.begin( ), departureTimesFromA.end( ) );
	sort( departureTimesFromB.begin( ), departureTimesFromB.end( ) );

	a = 0;
	std::vector<int>::iterator arrivalIterator;
	std::vector<int>::iterator departureIterator = departureTimesFromA.begin( );
	for( ; departureIterator != departureTimesFromA.end( ); departureIterator++ )
	{
		bool incA = true;
		arrivalIterator = arrivalTimesToA.begin( );
		for( ; arrivalIterator != arrivalTimesToA.end( ); arrivalIterator++ )
		{
			if( *departureIterator >= *arrivalIterator + turnaroundTime )
			{
				arrivalTimesToA.erase( arrivalIterator );
				incA = false;
				break;
			}
		}

		if( incA )
			++a;
	}	

	b = 0;	
	departureIterator = departureTimesFromB.begin( );
	for( ; departureIterator != departureTimesFromB.end( ); departureIterator++ )
	{
		bool incB = true;
		arrivalIterator = arrivalTimesToB.begin( );
		for( ; arrivalIterator != arrivalTimesToB.end( ); arrivalIterator++ )
		{			
			if( (*departureIterator) >= (*arrivalIterator) + turnaroundTime )
			{
				arrivalTimesToB.erase( arrivalIterator );
				incB = false;
				break;
			}
		}

		if( incB )
			++b;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "B-large.in" );

	int numCases;
	in >> numCases;

	std::fstream out;
	out.open( "B-large.out", std::ios_base::out );		
	
	for( int i = 0; i < numCases; ++i )
	{
		int val1;
		int val2;
		getNumTrips( in, val1, val2 );
		out << "Case #" << i + 1 << ": " << val1 << " " <<val2 << std::endl;

	}

	out.close( );

	return 0;
}

