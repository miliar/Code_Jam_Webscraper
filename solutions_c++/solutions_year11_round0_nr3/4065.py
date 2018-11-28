// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <cstdio>
#include <cassert>
#include <string>
#include <iostream>

#include <algorithm>


using namespace std;

typedef vector< int >	values_t;
typedef vector< int >	indexs_t;

struct testcase
{
	values_t	values;
};

typedef	vector< testcase >	testcases;

testcases	getTestCase( char *data )
{
	testcases	tcs;

	const char *delim = " \t\n";

	vector<char> data2( data, data + strlen(data) );

	int numberOfTestcases = 0;
	char *token = &data2[0];
	char *next_token = 0;

	token = strtok_s( token, delim, &next_token );
	numberOfTestcases = atoi( token );
	token = next_token;
		
	for( int j = 0; j < numberOfTestcases; ++j )
	{
		testcase	tc;

		token = strtok_s( token, delim, &next_token );
		int numberOfCandies = atoi( token );
		token = next_token;

		for( int i = 0; i < numberOfCandies; ++i )
		{
			token = strtok_s( token, delim, &next_token );
			int value = atoi( token );
			token = next_token;

			tc.values.push_back( value );
		}

		tcs.push_back( tc );
	}

	return tcs;
}

long getSize( const char *path )
{
	long size = 0;

	FILE *fp = 0;
	if( fopen_s( &fp, path, "rt" ) == 0 )
	{
		fseek( fp, 0, SEEK_END );
		size = ftell( fp );
		fclose( fp );
	}

	return size;
}

void getRead( const char *path, char *buffer, int size, int maxSize )
{
	FILE *fp = 0;
	if( fopen_s( &fp, path, "rt" ) == 0 )
	{
		fread_s( buffer, maxSize, size, 1, fp );
		fclose( fp );
	}
}

struct CandySplitting
{
	values_t		m_items;
	indexs_t			m_piles;
	
	CandySplitting( const values_t &value )
	{
		m_items = value;
	}

	size_t add( size_t arg1, size_t arg2 )
	{
		return arg1 ^ arg2;
	}

	size_t sum( const indexs_t &indexs )
	{
		size_t total = 0;

		for( size_t i = 0; i < indexs.size(); ++i )
			total = add( total, m_items[ indexs[i] ] );

		return total;
	}

	int realSum( const indexs_t &indexs )
	{
		int total = 0;

		for( size_t i = 0; i < indexs.size(); ++i )
			total += m_items[ indexs[i] ];

		return total;
	}

	void subset( int *aSet, size_t aSetLen, size_t current )
	{ 
		// 완성된 부분집합 하나를 출력하는 부분
		if( current == m_items.size() ) 
		{ 
			if( aSetLen > 0 && aSetLen < m_items.size() )
			{
				values_t	pile1( aSet, aSet + aSetLen );
				values_t	pile2;

				getSecondPile( pile1, pile2 );

				int total = -1;
				if( sum( pile1 ) == sum( pile2 ) )
					total = realSum( pile2 );

				m_piles.push_back( total );
			}
		}
		// 재귀적 호출을 통해 하나의 부분집합을 완성하는 부분
		else { 
			current++;
			subset(aSet, aSetLen, current);
			current--;
			aSet[aSetLen++]=current++;
			subset(aSet, aSetLen, current);
		}
	} 

	bool is( int value, const indexs_t &pp ) const
	{
		return find( pp.begin(), pp.end(), value ) != pp.end();
	}

	void getSecondPile( const indexs_t &first, indexs_t &second )
	{
		for( size_t i = 0; i < m_items.size(); ++i )
		{
			if( is( i, first ) == false )
				second.push_back( i );
		}
	}

	void getResult( void )
	{
		m_piles.clear();

		values_t	intermediate( m_items.size() );
		subset( &intermediate[0], 0, 0 );
	}
};

int getMaxTotal( values_t values )
{
	CandySplitting	cs( values );

	cs.getResult();

	sort( cs.m_piles.begin(), cs.m_piles.end(), greater<int>() );

	return cs.m_piles.empty() == true ? 0 : cs.m_piles[0];
}

void process( testcases &tcs )
{
	for( size_t i = 0; i < tcs.size(); ++i )
	{
		testcase	&tc = tcs[i];
		
		int total = getMaxTotal( tc.values );

		if( total != -1 )
			cout << "Case #" << i+1 << ": " << total << endl;
		else
			cout << "Case #" << i+1 << ": NO" << endl;
	}
}

int _tmain(int argc, char* argv[])
{
	if( argc < 2 )
		return 0;

	char *path = argv[1];

	long size = getSize( path );

	if( size != 0 )
	{
		vector< char >	buffer( size + 1 );

		getRead( path, &buffer[0], size, size + 1 );

		buffer[ size ] = 0;
		
		testcases	tcs = getTestCase( &buffer[0] );

		process( tcs );
	}

	return 0;
}

