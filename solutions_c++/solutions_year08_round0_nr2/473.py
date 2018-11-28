#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

////////////////////////////////////////////////////////////////////////////////////
//

#define INFINITY	10000000

struct TripInfo
{
	TripInfo() : timeDep_( 0 ), timeArr_( 0 ) { }
	TripInfo( int td, int ta ) : timeDep_( td ), timeArr_( ta ) { }
	int timeDep_;
	int timeArr_;
};

struct TrainCount
{
	TrainCount() : count_( 0 ) { }
	char count_;
};

typedef vector< TripInfo >		TripInfoVec;
typedef map< int, TrainCount >	StatusMap;

void calcTrains( const int& na, const int& nb, TripInfoVec& fromA, TripInfoVec& fromB, int& resFromA, int& resFromB )
{
	StatusMap statA, statB;

	for ( int i = 0; i < na; ++i ) {
		statA[ fromA[ i ].timeDep_ ].count_++;
		statB[ fromA[ i ].timeArr_ ].count_--;
	}

	for ( int i = 0; i < nb; ++i ) {
		statB[ fromB[ i ].timeDep_ ].count_++;
		statA[ fromB[ i ].timeArr_ ].count_--;
	}

	resFromA = 0;
	for ( int i = 0, count = statA.size(), needCount = 0; i < count; ++i ) {
		int min = INFINITY;
		StatusMap::iterator minIter = statA.end();

		for ( StatusMap::iterator iter = statA.begin(); iter != statA.end(); ++iter ) {
			if ( iter->first < min ) {
				min = iter->first;
				minIter = iter;
			}
		}

		needCount += minIter->second.count_;
		statA.erase( minIter );

		if ( needCount > resFromA ) resFromA = needCount;
	}

	resFromB = 0;
	for ( int i = 0, count = statB.size(), needCount = 0; i < count; ++i ) {
		int min = INFINITY;
		StatusMap::iterator minIter = statB.end();

		for ( StatusMap::iterator iter = statB.begin(); iter != statB.end(); ++iter ) {
			if ( iter->first < min ) {
				min = iter->first;
				minIter = iter;
			}
		}

		needCount += minIter->second.count_;
		statB.erase( minIter );

		if ( needCount > resFromB ) resFromB = needCount;
	}
}

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("test.in");
//#define cin fin

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		TripInfoVec fromA;
		TripInfoVec fromB;
		TripInfo info;

		int turnAround;
		cin >> turnAround;

		int na, nb;
		cin >> na >> nb;

		string dep, arr;
		for ( int j = 0; j < na; ++j ) {
			cin >> dep >> arr;
			dep[ 2 ] = 0;
			arr[ 2 ] = 0;
			info.timeDep_ = atoi( dep.c_str() ) * 60 + atoi( dep.c_str() + 3 );
			info.timeArr_ = atoi( arr.c_str() ) * 60 + atoi( arr.c_str() + 3 ) + turnAround;

			fromA.push_back( info );
		}
		for ( int j = 0; j < nb; ++j ) {
			cin >> dep >> arr;
			dep[ 2 ] = 0;
			arr[ 2 ] = 0;
			info.timeDep_ = atoi( dep.c_str() ) * 60 + atoi( dep.c_str() + 3 );
			info.timeArr_ = atoi( arr.c_str() ) * 60 + atoi( arr.c_str() + 3 ) + turnAround;

			fromB.push_back( info );
		}

		int resFromA, resFromB;
		calcTrains( na, nb, fromA, fromB, resFromA, resFromB );
		cout << "Case #" << i << ": " << resFromA << " " << resFromB << endl;
	}

	return 0;
}
