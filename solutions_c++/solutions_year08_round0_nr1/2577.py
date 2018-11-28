#pragma warning(disable : 4786)
#include <cstdio>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;
vector< string > engine, list;
char input[400];

int main()
{
	freopen( "aa.in", "r", stdin );
	freopen( "bb.txt", "w", stdout );
	int N, tcase = 0, S, Q, i, j, T;
	string hold;
	set< string > seen;
	scanf( "%d", &N );
	while( N-- )
	{
		++tcase;
		engine.clear();
		list.clear();
		printf( "Case #%d: ", tcase );
		scanf( "%d ", &S );
		for( i = 0; i < S; ++i )
		{
			gets( input );
			engine.push_back( string( input ) );
		}
		scanf( "%d ", &Q );
		for( i = 0; i < Q; ++i )
		{
			gets( input );
			list.push_back( string( input ) );

		}
		int ans = 0,cnt, maxi;;
		i = 0;
		while( i < list.size() )
		{
			hold = list[i];
			cnt = 0;
			maxi = 0;
			i++;
			seen.clear();
			bool found = false;
			while( ( i < (int)list.size() ) && ( (int)seen.size() < (int)engine.size() - 1 ) )
			{
				if( list[i] != hold && seen.find( list[i] ) == seen.end() )
				{
					found = true;
					maxi = i;
					seen.insert( list[i] );
				}
				++i;
			}
			if( seen.size() != engine.size() - 1 ) break;
			//cout << list[maxi] << endl;
			ans++;
			if( found ) i = maxi ;
		}
		printf( "%d\n", ans );
	}

	return 0;
}