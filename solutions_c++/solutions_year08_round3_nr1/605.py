// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <functional>
#include <algorithm>
#include <set>
#include <list>





int _tmain(int argc, _TCHAR* argv[])
{
	int N;

	std::ifstream ifile( "input.txt" );
	std::ofstream ofile( "output.txt" );

	ifile >> N;

	for( int test_case = 0; test_case < N; test_case++ )
	{
		int result = 0;
		int p, k, l;

		ifile >> p >> k >> l;

		std::list< int > freq;
		for( int i = 0; i < l; i++ )
		{
			int f;
			ifile >> f;

			freq.push_back( f );
		}

		std::list< int > keys;
		keys.assign( k, 0 );

		std::list< int >::iterator max_freq = std::max_element( freq.begin( ), freq.end( ) );
		std::list< int >::iterator min_keys;

		while( max_freq != freq.end( ) && *max_freq > 0 )
		{
			do
			{
				min_keys = std::min_element( keys.begin( ), keys.end( ) );

				if( min_keys == keys.end( ) )
					break;

				if( *min_keys > p )
				{
					keys.erase( min_keys );
					continue;
				}
			}
			while( false );

			if( min_keys == keys.end( ) )
				break;

			(*min_keys)++;
			result += *min_keys * *max_freq;

			freq.erase( max_freq );
			max_freq = std::max_element( freq.begin( ), freq.end( ) );
		}

		if( min_keys == keys.end( ) && max_freq != freq.end( ) )
			ofile << "Case #" << test_case + 1 << ": " << "Impossible" << std::endl;
		else
			ofile << "Case #" << test_case + 1 << ": " << result << std::endl;
	}

	return 0;
}

