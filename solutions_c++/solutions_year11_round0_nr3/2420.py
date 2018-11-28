#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <set>
#include <assert.h>

void foo() {}

__int64 solve_optimal( const std::vector< __int64 > &vCandys )
{
	__int64 s = 0;
	size_t i;
	__int64 cmin = vCandys[0], imin = 0;
	for( i = 0; i < vCandys.size(); i++ )
	{
		s ^= vCandys[i];
		if ( vCandys[i] < cmin )
		{
			cmin = vCandys[i];
			imin = i;
		}
	}

	if ( s ) return -1;

	__int64 res = 0;
	for( i = 0; i < vCandys.size(); i++ )
		if ( i != imin )
			res += vCandys[i];
	return res;
}

__int64 solve_brute( const std::vector< __int64 > &vCandys )
{
	std::vector< bool > pile1;
	pile1.resize( vCandys.size() );
	size_t i;
	for( i = 0; i < vCandys.size(); i++ )
		pile1[i] = false;

	__int64 sTop = -1;
	while( true )
	{
		i = 0;
		while( i < vCandys.size() )
		{
			if ( pile1[i] )
			{
				pile1[i] = 0;
				i++;
			}
			else
			{
				pile1[i] = true;
				break;
			}
		}
		if ( !( i < vCandys.size() ) ) break;

		__int64 sc1 = 0, sc2 = 0;
		__int64 s1 = 0, s2 = 0;
		for( i = 0; i < vCandys.size(); i++ )
		{
			if ( pile1[i] )
			{
				s1 ^= vCandys[i];
				sc1 += vCandys[i];
			}
			else
			{
				s2 ^= vCandys[i];
				sc2 += vCandys[i];
			}
		}

		if ( s1 == s2 && sc1 > 0 && sc2 > 0 )
			sTop = std::max( sTop, std::max( sc1, sc2 ) );

		foo();
	}

	return sTop;
}

int main()
{
	FILE *fin, *fout;
	if ( !(fin = fopen( "C-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int nCandys;
		fscanf( fin, "%d", &nCandys );
		std::vector< __int64 > vCandys;
		for( int iCandy = 0; iCandy < nCandys; iCandy++ )
		{
			int c;
			fscanf( fin, "%d", &c );
			vCandys.push_back( c );
		}

//		__int64 res1 = solve_brute( vCandys );
		__int64 res = solve_optimal( vCandys );
//		assert( res == res1 );
		assert( res < INT_MAX );

		fprintf( fout, "Case #%d: ", iCase + 1 );
		if ( res >= 0 )
			fprintf( fout, "%d\n", (int)res );
		else fprintf( fout, "NO\n" );
	}


	fclose( fin );
	fclose( fout );

	return 0;
/*
	for( int iTest = 0; iTest < 1000000; iTest++ )
	{
		int n = rand() * 10 / RAND_MAX + 1;
		std::vector< __int64 > vCandys;
		__int64 s = 0;
		for( int i = 0; i < n; i++ )
		{
			__int64 c = rand() * 10000 / RAND_MAX + 1;
			s ^= c;
			vCandys.push_back( c );
		}
		if ( rand() % 5 == 0 )
		{
			vCandys.push_back( s );
		}
		__int64 res1 = solve_brute( vCandys );
		__int64 res2 = solve_optimal( vCandys );
		assert( res1 == res2 );

		assert( res1 < INT_MAX );
	}*/
}
