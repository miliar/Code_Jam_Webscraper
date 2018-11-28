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

#define file "..\\..\\GCJ\\2012r2\\in\\c"

void prepare()
{
#ifdef _DEBUG
	freopen( "in.txt", "r", stdin );
#else
	freopen( file ".in", "r", stdin );
	freopen( file ".out", "w", stdout );
#endif
}

const int MAXN = 2002;
int a[MAXN];
int h[MAXN];
int r[MAXN];

bool solve()
{
	int n, i, k;
	scanf( "%d", &n );
	for ( i = 1; i < n; i++ )
		scanf( "%d", a + i );
	h[n] = 1000 * 1000 * 1000 - 1;
	r[n] = 0;
	for ( i = n - 1; i > 0; i-- )
	{
		for ( k = i + 1; k < a[i]; k++ )
		{
			if ( a[k] > a[i] )
			{
				printf("Impossible\n");
				return false;
			}
		}
	}
	for ( i = n - 1; i > 0; i-- )
	{
		r[i] = r[a[i]] + 1;
		h[i] = h[a[i]] - r[a[i]] * ( a[i] - i ) - 1;
	}
	for ( i = 1; i <= n; i++ )
		printf( "%d%c", h[i], i == n ? '\n' : ' ' );
	return true;
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
		solve( );
		//fprintf(stderr, "test #%d done\n", ttt + 1);
	}
//#endif
	return 0;
}