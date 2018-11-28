#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

const int MAXN = 106;

struct sTrip
{
	int Start, Finish;
	bool IsFromAToB;
};

bool operator <( const sTrip &trip1, const sTrip &trip2 )
{
	return trip1.Start < trip2.Start;
}

void ReadDirection( sTrip *trip, int count, bool is_from_a_to_b )
{
	int i;
	for( i = 0; i < count; ++i )
	{
		int start_hour, start_minute, finish_hour, finish_minute;
		scanf( "%d:%d%d:%d", &start_hour, &start_minute, &finish_hour, &finish_minute );
		trip[ i ].Start = start_hour * 60 + start_minute;
		trip[ i ].Finish = finish_hour * 60 + finish_minute;
		trip[ i ].IsFromAToB = is_from_a_to_b;
	}
}

int T;
int Count;
sTrip Trip[ MAXN * 2 ];

void Read()
{
	int na, nb;
	scanf( "%d", &T );
	scanf( "%d%d", &na, &nb );
	Count = na + nb;
	ReadDirection( Trip, na, true );
	ReadDirection( Trip + na, nb, false );
}

map< int, int > A, B;
int ACount, BCount;

void Work()
{
	int i;
	sort( Trip, Trip + Count );
	A.clear();
	B.clear();
	ACount = 0;
	BCount = 0;
	for( i = 0; i < Count; ++i )
	{
		if( Trip[ i ].IsFromAToB )
		{
			if( A.upper_bound( Trip[ i ].Start ) == A.begin() )
				++ACount;
			else if( A.begin()->second == 1 )
				A.erase( A.begin() );
			else
				--A.begin()->second;
			map< int, int >::iterator b_iterator = B.find( Trip[ i ].Finish + T );
			if( b_iterator == B.end() )
				B.insert( make_pair( Trip[ i ].Finish + T, 1 ) );
			else
				++b_iterator->second;
		}
		else
		{
			if( B.upper_bound( Trip[ i ].Start ) == B.begin() )
				++BCount;
			else if( B.begin()->second == 1 )
				B.erase( B.begin() );
			else
				--B.begin()->second;
			map< int, int >::iterator a_iterator = A.find( Trip[ i ].Finish + T );
			if( a_iterator == A.end() )
				A.insert( make_pair( Trip[ i ].Finish + T, 1 ) );
			else
				++a_iterator->second;
		}
	}
}

void Write( int i )
{
	printf( "Case #%d: %d %d\n", i, ACount, BCount );
}

int main()
{
	int i, n;
	scanf( "%d", &n );
	for( i = 1; i <= n; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
