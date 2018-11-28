#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

#define file "..\\..\\GCJ\\2012r2\\in\\a"

void prepare()
{
#ifdef _DEBUG
	freopen( "in.txt", "r", stdin );
#else
	freopen( file ".in", "r", stdin );
	freopen( file ".out", "w", stdout );
#endif
}

const int MAXN = 60606;
int d[MAXN];
int l[MAXN];
int r[MAXN];

bool solve()
{
	int n, i, j, k;
	scanf( "%d", &n );
	for ( i = 0; i < n; i++ )
		scanf( "%d%d", d + i, l + i );
	scanf( "%d", d + n );
	memset( r, 0, sizeof( r ) );
	r[0] = d[0];
	for ( i = 0; i < n; i++ )
	{
		if ( d[n] <= d[i] + r[i] )
			return true;
		for ( k = i + 1; k < n && d[k] <= d[i] + r[i]; k++ )
		{
			j = d[k] - d[i];
			if ( l[k] < j )
				j = l[k];
			if ( r[k] < j )
				r[k] = j;
		}
	}
	return false;
}

int main()
{
	prepare( );
	//solve( );
//#ifdef _DEBUG
	int tt;
	scanf( "%d", &tt );
	for (int ttt = 0; ttt < tt; ttt++)
	{
		printf( "Case #%d: ", ttt + 1 );
		printf( solve( ) ? "YES\n" : "NO\n" );
		//fprintf(stderr, "test #%d done\n", ttt + 1);
	}
//#endif
	return 0;
}