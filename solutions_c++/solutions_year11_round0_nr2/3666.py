#include <iostream>
#include <fstream>
#include <list>
#include <hash_map>
#include <string>

int main()
{
	std::ifstream fin( "C:/Users/0xc0deface/Downloads/B-small-attempt0.in" );
	std::ofstream fout( "C:/Users/0xc0deface/Desktop/test.out" );

	int testCases;
	fin >> testCases;

	for ( int i = 0; i < testCases; ++i )
	{

		int C, D, N;
		fin >> C;

		stdext::hash_map< std::string, char > combiningBases;
		stdext::hash_map< char, char > opposedBases;

		for ( int j = 0; j < C; ++j )
		{
			// the bases combine to form the nonbase
			char base1, base2, nonBase;
			fin >> base1 >> base2 >> nonBase;
			combiningBases[ std::string() + base1 + base2 ] = nonBase;
			combiningBases[ std::string() + base2 + base1 ] = nonBase;
		}

		fin >> D;

		for ( int j = 0; j < D; ++j )
		{
			// the bases oppose eachother
			char base1, base2;
			fin >> base1 >> base2;
			opposedBases[ base1 ] = base2;
			opposedBases[ base2 ] = base1;
		}

		fin >> N >> std::ws;

		std::list< char > elementList;

		for ( int j = 0; j < N; ++j )
		{
			char x;
			fin.get( x );

			if( !elementList.empty() )
			{
				stdext::hash_map< std::string, char >::iterator it = combiningBases.find( std::string() + elementList.back() + x );

				if ( it != combiningBases.end()	)
				{
					elementList.pop_back();
					elementList.push_back( it->second );
					continue;
				}

				stdext::hash_map< char, char >::iterator it2 = opposedBases.find( x );

				if ( it2 != opposedBases.end() )
				{
					bool loopBreak = false;
					for( std::list< char >::iterator k( elementList.begin() ), kEnd( elementList.end() ); k != kEnd; ++k )
					{
						if ( *k == it2->second )
						{
							elementList.clear();
							loopBreak = true;
							break;
						}
					}
					if ( loopBreak )
						continue;
				}

			}
			elementList.push_back( x );
		}

		fout << "Case #" << i+1 << ": [";

		for( std::list< char >::iterator k( elementList.begin() ), kEnd( elementList.end() ); k != kEnd; )
		{
			fout << *k;
			++k;
			if ( k != kEnd )
				fout << ", ";
		}

		fout << "]" << std::endl;
	}
	return 0;
}
