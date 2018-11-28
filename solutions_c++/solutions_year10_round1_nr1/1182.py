#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 200
int dir[4][2] = { -1, 0, 1, 0, 0, -1, 0, 1 };
int ca, n, m;
char mp1[N][N], mp2[N][N];

void rotate( )
{
	int i, j, k;
	memset( mp2, 0, sizeof(mp2) );
	for ( i = 0; i < n; i++ )
	{
		for ( j = 0; j < n; j++ )
			mp2[j][n-1-i] = mp1[i][j];
	}
	//for ( i = 0; i < n; i++) printf( "%s\n", mp2[i] );
	for ( i = 0; i < n; i++ )
	{
		for ( j = n-1; j >= 0; j-- )
		{
			if ( mp2[j][i] == '.' ) continue;
			for ( k = j+1; k < n; k++ )
			{
				if ( mp2[k][i] != '.' ) break;
				swap( mp2[k][i], mp2[k-1][i] );
			}
		}
	}
	//for ( i = 0; i < n; i++ ) printf( "%s\n", mp2[i] );
}

bool checkR( )
{
	int i, j, k, x, y;
	for ( i = 0; i < n; i++ )
	{
		for ( j = 0; j < n; j++ )
		{
			if ( mp2[i][j] != 'R' ) continue;
			for ( k = 0; k < m; k++ )
			{
				if ( j+k >= n ) break;
				if ( mp2[i][j+k] != 'R' ) break;
			}
			if ( k == m ) return true;
			for ( k = 0; k < m; k++ )
			{
				if ( i+k >= n || mp2[i+k][j] != 'R' ) break;
			}
			if ( k == m ) return true;
			for ( k = 0; k < m; k++ )
			{
				if ( i+k >= n || j+k >= n || mp2[i+k][j+k] != 'R' ) break;
			}
			if ( k == m ) return true;
		}
	}
	return false;
}

bool checkB( )
{
	int i, j, k, x, y;
	for ( i = 0; i < n; i++ )
	{
		for ( j = 0; j < n; j++ )
		{
			if ( mp2[i][j] != 'B' ) continue;
			for ( k = 0; k < m; k++ )
			{
				if ( j+k >= n ) break;
				if ( mp2[i][j+k] != 'B' ) break;
			}
			if ( k == m ) return true;
			for ( k = 0; k < m; k++ )
			{
				if ( i+k >= n || mp2[i+k][j] != 'B' ) break;
			}
			if ( k == m ) return true;
			for ( k = 0; k < m; k++ )
			{
				if ( i+k >= n || j+k >= n || mp2[i+k][j+k] != 'B' ) break;
			}
			if ( k == m ) return true;
		}
	}
	return false;
}

int main( )
{
	freopen( "A-small.in", "r", stdin );
	freopen( "A-small.out", "w", stdout );
	int i, j, t = 0;
	scanf( "%d", &ca );
	while ( ca-- )
	{
		scanf( "%d%d", &n, &m );
		for ( i = 0; i < n; i++ ) scanf( "%s", mp1[i] );
		rotate( );
		i = checkR( );
		j = checkB( );
		printf( "Case #%d: ", ++t );
		if ( i&&j ) printf( "Both\n" );
		else if ( i && !j ) printf( "Red\n" );
		else if ( !i && j ) printf( "Blue\n" );
		else printf( "Neither\n" );
	}
}
