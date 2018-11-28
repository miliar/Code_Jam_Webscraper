#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <math.h>
#include <memory.h>
using namespace std;

#define file "input"

void prepare( )
{
	freopen( "input.txt", "r", stdin );
	freopen( "a.txt", "w", stderr );
	freopen( "output.txt", "w", stdout );
}

const int MAXW = 22;
const int MAXN = 252;

char s[MAXW][MAXW];
string a[2][MAXW][MAXW][MAXN * 2 + 20];
int z;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool calc( int n, int q )
{
	char c;
	bool boo = false;
	int i, k, j, t, qwe, asd;
	string ss;
	for ( i = 1; i <= n; i++ )
	{
		for ( k = 1; k <= n; k++ )
		{
			if ( ( ( i + k ) & 1 ) == z )
			{
				for ( j = 0; j < 4; j++ )
				{
					if ( i + dx[j] < 1 || i + dx[j] > n || k + dy[j] < 1 || k + dy[j] > n )
						continue;
					c = s[i + dx[j]][k + dy[j]];
					c = ( c == 1 ? '+' : '-' );
					for ( t = -MAXN + 1; t < MAXN; t++ )
					{
						ss = a[1 - q][i][k][t + MAXN];
						if ( ss.size( ) == 0 )
							continue;
						ss.push_back( c );
						qwe = a[q][i + dx[j]][k + dy[j]][t + MAXN].size( );
						if ( qwe == 0 || (int)ss.size( ) < qwe || ( (int)ss.size( ) == qwe && ss < a[q][i + dx[j]][k + dy[j]][t + MAXN] ) )
						{
							a[q][i + dx[j]][k + dy[j]][t + MAXN] = ss;
							boo = true;
						}
					}
				}
			}
			else
			{
				for ( j = 0; j < 4; j++ )
				{
					if ( i + dx[j] < 1 || i + dx[j] > n || k + dy[j] < 1 || k + dy[j] > n )
						continue;
					asd = s[i + dx[j]][k + dy[j]];
					c = asd + '0';
					asd *= s[i][k];
					for ( t = -MAXN + 1; t < MAXN; t++ )
					{
						if ( t + asd <= -MAXN )
							continue;
						if ( t + asd >= MAXN )
							continue;
						ss = a[1 - q][i][k][t + MAXN];
						if ( ss.size( ) == 0 )
							continue;
						ss.push_back( c );
						qwe = a[q][i + dx[j]][k + dy[j]][t + MAXN + asd].size( );
						if ( qwe == 0 || (int)ss.size( ) < qwe || ( (int)ss.size( ) == qwe && ss < a[q][i + dx[j]][k + dy[j]][t + MAXN + asd] ) )
						{
							a[q][i + dx[j]][k + dy[j]][t + MAXN + asd] = ss;
							boo = true;
						}
					}
				}
			}
		}
	}
	return boo;
}

void solve( int t )
{
	int n, i, w, q, k, j;
	memset( s, 0, sizeof( s ) );
	scanf( "%d %d\n", &w, &q );
	for ( i = 1; i <= w; i++ )
		for ( k = 1; k <= w; k++ )
			for ( j = -MAXN; j <= MAXN; j++ )
			{
				a[0][i][k][j + MAXN].clear( );
				a[1][i][k][j + MAXN].clear( );
			}
	for ( i = 1; i <= w; i++ )
		gets( s[i] + 1 );
	if ( s[1][1] == '+' || s[1][1] == '-' )
		z = 1;
	else
		z = 0;
	for ( i = 1; i <= w; i++ )
		for ( k = 1; k <= w; k++ )
		{
			if ( s[i][k] == '+' )
				s[i][k] = 1;
			else
			if ( s[i][k] == '-' )
				s[i][k] = -1;
			else
			{
				s[i][k] -= '0';
				a[0][i][k][s[i][k] + MAXN].push_back( s[i][k] + '0' );
			}
		}
	for ( i = 1; ; i++ )
	{
		if ( !calc( w, i & 1 ) )
			break;
	}
	fprintf( stderr, "%d\n", i );
	printf( "Case #%d:\n", t );
	string ans;
	for ( j = 0; j < q; j++ )
	{
		scanf( "%d", &n );
		ans.clear( );
		for ( i = 1; i <= w; i++ )
			for ( k = 1; k <= w; k++ )
			{
				if ( ( ( i + k ) & 1 ) != z )
					continue;
				if ( a[0][i][k][n + MAXN].size( ) == 0 ) 
					continue;
				if ( ans.size( ) == 0 || ( a[0][i][k][n + MAXN].size( ) < ans.size( ) ) || ( ans.size( ) == a[0][i][k][n + MAXN].size( ) && a[0][i][k][n + MAXN] < ans ) )
				{
					//printf( "%d %d\n", (int)ans.size( ), (int)a[0][i][k][n + MAXN].size( ) );
					ans = a[0][i][k][n + MAXN];
				}
			}
		puts( ans.data( ) );
	}
	return;
}

int main( )
{
	int t, i;
	prepare( );
	scanf( "%d\n", &t );
	for ( i = 0; i < t; i++ )
		solve( i + 1 );
	fclose( stderr );
	return 0;
}