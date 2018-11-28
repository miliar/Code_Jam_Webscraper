#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <assert.h>
#include <set>

std::vector< __int64 > simples;

__int64 next_simple()
{
	if ( simples.empty() )
	{
		simples.push_back( 2 );
		return 2;
	}
	else
	{
		std::vector< __int64 >::iterator i = simples.end();
		i--;
		__int64 s = *i;

		while( true )
		{
			s++;
			bool ok = true;
			for( i = simples.begin(); i != simples.end(); i++ )
			{
				double d = fmod( (double)s, (double)*i );
				if ( d == 0 )
				{
					ok = false;
					break;
				}
/*				__int64 k = 2;
				while( true )
				{
					__int64 m = k * *i;
					if ( m > s ) break;
					else if ( k * *i == s )
					{
						ok = false;
						break;
					}
					k++;
				}*/
/*
				std::vector< __int64 >::iterator i2;
				for( i2 = simples.begin(); i2 != simples.end(); i2++ )
				{
					if ( *i * *i2 == s )
					{
						ok = false;
						break;
					}
				}
				if ( !ok ) break;*/
			}
			if ( ok )
			{
				simples.push_back( s );
				return s;
			}
		}
	}
}

int main()
{
	FILE *fin, *fout;
	if ( !(fin = fopen( "C-small-attempt0.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int np;
		__int64 nlow, nhigh;
		fscanf( fin, "%d %I64d %I64d\n", &np, &nlow, &nhigh );
		std::vector< __int64 > notes( np );

		for( int i = 0; i < np; i++ )
		{
			__int64 n;
			fscanf( fin, "%I64d", &n );
			notes[i] = n;
		}

		fprintf( fout, "Case #%d: ", iCase + 1 );
		bool found = false;
		for( __int64 f = nlow; f <= nhigh; f++ )
		{
			bool ok = true;
			for( int i = 0; i < np; i++ )
			{
				if ( !( fmod( double( f ), double( notes[i] ) ) == 0 ||
					fmod( double( notes[i] ), double( f ) ) == 0 ) )
				{
					ok = false;
					break;
				}
			}

			if ( ok )
			{
				fprintf( fout, "%d\n", int( f ) );
				found = true;
				break;
			}
		}
		if ( !found ) fprintf( fout, "NO\n" );
	}

	fclose( fin );
	fclose( fout );

	return 0;
}

