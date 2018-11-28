#include <fstream>
#include <iostream>
#include <string>

#define PROBLEM_A

#ifdef PROBLEM_A
#	define PROBLEM_SMALL "A-large"
#endif

#ifdef PROBLEM_B
#	define PROBLEM_SMALL "B-small-attempt"
#	define PROBLEM_LARGE "B-large"
#endif

#ifdef PROBLEM_C
#	define PROBLEM_SMALL "C-small-attempt"
#	define PROBLEM_LARGE "C-large"
#endif

#define IN_FILE ( std::string( PROBLEM_SMALL ) + ".in" ).c_str()
#define OUT_FILE ( std::string( PROBLEM_SMALL ) + ".out" ).c_str()

char tiles[50][50];

bool overlapsOrImpossible( int x, int y )
{
	if( tiles[x][y] == '.' || tiles[x+1][y] == '.' || tiles[x][y+1] == '.' || tiles[x+1][y+1] == '.' )
		return true;
	if( tiles[x][y] == '/' || tiles[x+1][y] == '/' || tiles[x][y+1] == '/' || tiles[x+1][y+1] == '/' )
		return true;
	if( tiles[x][y] == '\\' || tiles[x+1][y] == '\\' || tiles[x][y+1] == '\\' || tiles[x+1][y+1] == '\\' )
		return true;
	return false;
}

int main()
{
	std::ifstream fin( IN_FILE );
	std::ofstream fout( OUT_FILE );

	int testCases;
	fin >> testCases;

	memset( tiles, 0, sizeof( char ) * 50 * 50 );


	for ( int i = 0; i < testCases; ++i )
	{

		int R,C;
		fin >> R >> C;

		for ( int x = 0; x < R; ++x )
		{
			for ( int y = 0; y < C; ++y )
			{
				fin >> std::ws;
				fin >> tiles[x][y];
			}
		}

		bool impossible = false;

		for ( int x = 0; x < R && !impossible; ++x )
		{
			for ( int y = 0; y < C; ++y )
			{
				if ( tiles[x][y] == '#' )
				{
					// try replace
					if ( x + 1 < R && y + 1 < C && !overlapsOrImpossible( x, y ) )
					{
						tiles[x][y] = '/' ;
						tiles[x+1][y] = '\\'; 
						tiles[x][y+1] = '\\' ;
						tiles[x+1][y+1] = '/';
					}
					else
					{
						impossible = true;
						break;
					}
				}
			}
		}


		if ( impossible )
		{
			fout << "Case #" << i+1 << ":\nImpossible" << std::endl; 
		}
		else
		{
			fout << "Case #" << i+1 << ": " << std::endl; 

			for ( int x = 0; x < R ; ++x )
			{
				for ( int y = 0; y < C; ++y )
					fout << tiles[x][y];
				fout << std::endl; 
			}
		}


	}
}
