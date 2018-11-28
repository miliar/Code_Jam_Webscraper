#include <fstream>
#include <iostream>
#include <string>

#define PROBLEM_C

#ifdef PROBLEM_B
#	define PROBLEM_SMALL "B-small-attempt"
#endif

#ifdef PROBLEM_C
#	define PROBLEM_SMALL "C-small-attempt"
#endif

#define IN_FILE ( std::string( PROBLEM_SMALL ) + ".in" ).c_str()
#define OUT_FILE ( std::string( PROBLEM_SMALL ) + ".out" ).c_str()

int playerNotes[100];

int main()
{
	std::ifstream fin( IN_FILE );
	std::ofstream fout( OUT_FILE );

	int testCases;
	fin >> testCases;


	for ( int i = 0; i < testCases; ++i )
	{
		memset( playerNotes, 0, sizeof( int ) * 100 );


		int N, L, H;
		fin >> N >> L >> H;

		for ( int j = 0; j < N; ++j )
			fin >> playerNotes[j];

		//from L to H % 

		bool harmonious = true;

		for ( int j = L; j < H+1; ++j )
		{
			harmonious = true;

			for ( int k = 0; k < N; ++k )
			{
				int minK = std::min( playerNotes[k], j );
				int maxK = std::max( playerNotes[k], j );

				if( maxK % minK != 0 )
				{
					harmonious = false;
					break;
				}
			}

			if ( harmonious )
			{
				fout << "Case #" << i+1 << ": " << j << std::endl;
				break;
			}
		}

		if ( !harmonious )
			fout << "Case #" << i+1 << ": NO" << std::endl;
	}
}
