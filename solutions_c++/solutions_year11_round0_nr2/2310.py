#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <map>
#include <vector>
#include <set>
#include <assert.h>

struct Pair
{
	char c1, c2;
	Pair() {}
	Pair( char a1, char a2 ) : c1( a1 ), c2( a2 ) {}
	bool operator < ( const Pair &p ) const
	{
		if ( c1 < p.c1 ) return true;
		else if( c1 == p.c1 )
			return c2 < p.c2;
		return false;
	}
};


int main()
{
	FILE *fin, *fout;
	if ( !(fin = fopen( "B-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int nCombine;
		fscanf( fin, "%d ", &nCombine );

		char c1, c2, c3;
		std::map< Pair, char > mCombine;
		for( int iCombine = 0; iCombine < nCombine; iCombine++ )
		{
			c1 = fgetc( fin );
			c2 = fgetc( fin );
			c3 = fgetc( fin );
			fgetc( fin );
			mCombine.insert( std::make_pair( Pair( c1, c2 ), c3 ) );
			mCombine.insert( std::make_pair( Pair( c2, c1 ), c3 ) );
		}

		int nOppose;
		fscanf( fin, "%d ", &nOppose );
		std::set< Pair > sOppose;
		for( int iOppose = 0; iOppose < nOppose; iOppose++ )
		{
			c1 = fgetc( fin );
			c2 = fgetc( fin );
			fgetc( fin );
			sOppose.insert( Pair( c1, c2 ) );
			sOppose.insert( Pair( c2, c1 ) );
		}
		int nCast;
		fscanf( fin, "%d ", &nCast );

		std::vector< char > vResult;
		for( int iCast = 0; iCast < nCast; iCast++ )
		{
			char cLast = 0;
			if ( !vResult.empty() )
				cLast = vResult.back();

			int c = fgetc( fin );
			std::map< Pair, char >::iterator ic;
			ic = mCombine.find( Pair( cLast, c ) );
			if ( ic != mCombine.end() )
			{
				vResult.back() = ic->second;
			}
			else
			{
				bool bOppose = false;
				std::set< Pair >::iterator io;
				for( size_t ires = 0; ires < vResult.size(); ires++ )
				{
					io = sOppose.find( Pair( vResult[ires], c ) );
					if ( io != sOppose.end() )
					{
						vResult.clear();
						bOppose = true;
						break;
					}
				}
				if ( !bOppose )
					vResult.push_back( c );
			}
		}

		fprintf( fout, "Case #%d: ", iCase + 1 );
		fprintf( fout, "[" );
		for( int i = 0; i < (int)vResult.size(); i++ )
		{
			if ( i )
				fprintf( fout, ", " );
			fprintf( fout, "%c", vResult[i] );
		}
		fprintf( fout, "]\n" );
	}

	fclose( fin );
	fclose( fout );

	return 0;
}
