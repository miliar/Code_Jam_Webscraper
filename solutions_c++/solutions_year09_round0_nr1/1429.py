// QR.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


bool lack[ 5000 ];

int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.out", "wt", stdout );

	int N = 0, D = 0, L = 0;

	cin >> L >> D >> N;

	vector<string> words( D );

	for( int i = 0; i < D; ++i )
	{
		cin >> words[ i ];
	}

	for( int ct = 1; ct <= N; ++ct)
	{
		memset( lack, false, sizeof( lack ) );

		string pattern;
		cin >> pattern;

		int res = D;

		vector<vector<char>> parsed_pattern( L, vector<char>( ) );

		int k = 0;
		int s = 0;

		bool bOpened = false;

		while( k < pattern.size( ) )
		{
			if( pattern[ k ] == ')' )
			{
				bOpened = false;
				++s;
			}
			else if( pattern[ k ] == '(' )
			{
				bOpened = true;
			}
			else
			{					
				parsed_pattern[ s ].push_back( pattern[ k ] );
				
				if( ! bOpened )
				{
					++s;
				}
			}
			++k;
		}
		
		for( int i = 0; i < parsed_pattern.size( ); ++i )
		{
			for( int j = 0; j < words.size( ); ++j )
			{
				if( lack[ j ] ) continue;

				if( parsed_pattern[ i ].end( ) == find( parsed_pattern[ i ].begin( ),
														parsed_pattern[ i ].end( ), words[ j ][ i ] ) )
				{
					--res;
					lack[ j ] = true;
				}
			}
		}

		cout << "Case #" << ct << ": " << res << endl;
	}

}