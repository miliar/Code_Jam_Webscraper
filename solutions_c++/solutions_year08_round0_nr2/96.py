// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <functional>
#include <algorithm>





int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream ifile( "input.txt" );
	std::ofstream ofile( "output.txt" );

	int N;
	ifile >> N;

	for( int test_case = 0; test_case < N; test_case++ )
	{
		int T;
		ifile >> T;

		int NA, NB;
		ifile >> NA >> NB;

		typedef std::pair< int, int > TimeType;

		TimeType timesA[ 200 ];
		TimeType timesB[ 200 ];

		int i;
		for( i = 0; i < NA; i++ )
		{
			TimeType time;

			int hh, mm;
			char c;
			ifile >> hh >> c >> mm;

			time.first = hh * 60 + mm;

			ifile >> hh >> c >> mm;

			time.second = hh * 60 + mm;

			timesA[ i ] = time;
		}

		for( i = 0; i < NB; i++ )
		{
			TimeType time;

			int hh, mm;
			char c;
			ifile >> hh >> c >> mm;

			time.first = hh * 60 + mm;

			ifile >> hh >> c >> mm;

			time.second = hh * 60 + mm;

			timesB[ i ] = time;
		}

		std::vector< std::pair< int, bool > > time_events[ 2 ];
		int need_trains[ 2 ];
		int available_trains[ 2 ];

		for( i = 0; i < NA; i++ )
			time_events[ 0 ].push_back( std::make_pair( timesA[ i ].first, true ) );

		for( i = 0; i < NB; i++ )
			time_events[ 0 ].push_back( std::make_pair( timesB[ i ].second + T, false ) );

		for( i = 0; i < NB; i++ )
			time_events[ 1 ].push_back( std::make_pair( timesB[ i ].first, true ) );

		for( i = 0; i < NA; i++ )
			time_events[ 1 ].push_back( std::make_pair( timesA[ i ].second + T, false ) );

		struct sort_pred : public std::binary_function< std::pair< int, bool >, std::pair< int, bool >, bool >
		{
			bool operator( )	( const std::pair< int, bool >& _left, const std::pair< int, bool >& _right ) const
			{
				return _left.first < _right.first || _left.first == _right.first && _left.second == false;
			};
		};

		std::sort( time_events[ 0 ].begin( ), time_events[ 0 ].end( ), sort_pred( ) );
		std::sort( time_events[ 1 ].begin( ), time_events[ 1 ].end( ), sort_pred( ) );

		for( i = 0; i < 2; i++ )
		{
			available_trains[ i ] = 0;
			need_trains[ i ] = 0;
			for( size_t ev = 0, max_ev = time_events[ i ].size( ); ev < max_ev; ev++ )
			{
				const std::pair< int, bool >& tevent = time_events[ i ][ ev ];

				if( tevent.second )
				{
					// trans must start
					if( available_trains[ i ] )
						available_trains[ i ]--;
					else
						need_trains[ i ]++;
				}
				else
				{
					// train has arrived and ready
					available_trains[ i ]++;
				}
			}
		}

		ofile << "Case #" << test_case + 1 << ": " << need_trains[ 0 ] << " " << need_trains[ 1 ] << std::endl;
	}

	return 0;
}

