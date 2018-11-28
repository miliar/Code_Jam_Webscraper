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
		__int64 result = 0;

		enum Types
		{
			NONE,
			PLUS,
			MINUS,
		};

		std::string snumber;

		ifile >> snumber;

		std::vector< char > digits;
		std::vector< Types > signs;

		std::copy( snumber.begin( ), snumber.end( ), std::back_inserter( digits ) );

		signs.assign( digits.size( ) - 1, NONE );

		while( true )
		{
			// compute number

			__int64 sum = 0;
			__int64 add = digits[ 0 ] - '0';
			Types last_sign = NONE;

			int i;
			for( i = 0; i < static_cast< int >( signs.size( ) ); i++ )
			{
				switch( signs[ i ] )
				{
				case NONE:
					add = add * 10 + digits[ i + 1 ] - '0';
					break;

				default:
					if( last_sign == MINUS )
						sum -= add;
					else
						sum += add;
					add = digits[ i + 1 ] - '0';
					last_sign = signs[ i ];
				}
			}

			if( last_sign == MINUS )
				sum -= add;
			else
				sum += add;

			if( sum == 0 || sum % 2 == 0 || sum % 3 == 0 || sum % 5 == 0 || sum % 7 == 0 )
				result++;

			i = static_cast< int >( signs.size( ) ) - 1;
			while( i >= 0 )
			{
				if( signs[ i ] == MINUS )
				{
					signs[ i ] = NONE;
					i--;
				}
				else
				{
					signs[ i ] = static_cast< Types >( signs[ i ] + 1 );
					break;
				}
			}

			if( i < 0 )
				break;
		}

		ofile << "Case #" << test_case + 1 << ": " << result << std::endl;
	}

	return 0;
}

