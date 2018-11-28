#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define fo(a,b,c) for( (a) = (b); (a) < (c); ++ (a) )
#define fr(a,b) fo( (a), 0, (b) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define all(v) (v).begin( ), (v).end( )
#define pb push_back
#define mp make_pair

const int maxn = 2005;

int n, m;
int tot[maxn];
int mal[maxn];
int p[maxn];
vector< int > usr[maxn];
vector< int > q;

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d", &n );
		scanf( "%d", &m );

		fi( n ) usr[i].clear( );

		q.clear( );
		memset( mal, -1, sizeof( mal ) );
		memset( tot, 0, sizeof( tot ) );
		fi( m )
		{
			int z;
			scanf( "%d", &z );
			fj( z )
			{
				int a, b;
				scanf( "%d", &a );
				-- a;
				scanf( "%d", &b );

				if( b ) mal[i] = a;
				else
				{
					usr[a].pb( i );
					++ tot[i];
				}
			}

			if( !tot[i] ) q.pb( i );
		}

		memset( p, 0, sizeof( p ) );
		bool possible = true;
		while( q.size( ) )
		{
			int cur = q.back( );
			q.pop_back( );

			if( mal[cur] == -1 )
			{
				possible = false;
				break;
			}

			if( !p[mal[cur]] )
			{
				p[mal[cur]] = 1;
				fi( usr[mal[cur]].size( ) )
				{
					-- tot[usr[mal[cur]][i]];
					if( !tot[usr[mal[cur]][i]] )
						q.pb( usr[mal[cur]][i] );
				}
			}
		}

		printf( "Case #%d:", tt );
		if( !possible ) printf( " IMPOSSIBLE\n" );
		else
		{
			fi( n ) printf( " %d", p[i] );
			printf( "\n" );
		}
	}

	return 0;
}
