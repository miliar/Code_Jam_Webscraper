// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>





int _tmain(int argc, _TCHAR* argv[])
{
	int N;

	std::ifstream ifile( "input.txt" );
	std::ofstream ofile( "output.txt" );

	ifile >> N;
	_ASSERTE( N <= 20 );

	for( int test_case = 0; test_case < N; test_case++ )
	{
		int S;
		ifile >> S;

		_ASSERTE( S <= 100 && "No, no, no, David Blane!!" );

		std::string engines[ 100 ];
		int catch_count[ 100 ];

		int i;
		char sname[ 100 ];
		ifile.getline( sname, 100 );
		for( i = 0; i < S; i++ )
		{
			ifile.getline( sname, 100 );
			engines[ i ] = sname;
			catch_count[ i ] = 0;
		}

		int Q;
		ifile >> Q;

		int result = 0;
		int current_engine = 0;

		ifile.getline( sname, 100 );
		for( i = 0; i < Q; i++ )
		{
			ifile.getline( sname, 100 );

			for( int s = 0; s < S; s++ )
				if( sname == engines[ s ] )
				{
					catch_count[ s ]++;
					if( current_engine == s )
					{
						int new_s;
						for( new_s = current_engine + 1; new_s < S; new_s++ )
							if( catch_count[ new_s ] == 0 )
							{
								current_engine = new_s;
								break;
							}

						if( new_s == S )
						{
							result++;

							int ss;
							for( ss = 0; ss < S; ss++ )
								catch_count[ ss ] = 0;

							current_engine = s == 0 ? 1 : 0;
							catch_count[ s ] = 1;
						}
					}
					break;
				}
		}

		ofile << "Case #" << test_case + 1 << ": " << result << std::endl;
	}

	return 0;
}

