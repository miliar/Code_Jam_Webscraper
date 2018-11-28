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

#define file "..\\..\\GCJ\\2012qual\\in\\b"

void prepare()
{
#ifdef _DEBUG
	freopen( "in.txt", "r", stdin );
#else
	freopen( file ".in", "r", stdin );
	freopen( file ".out", "w", stdout );
#endif
}

int get(int p, int d)
{
	return 
		p +
		( p < d ? 0 : p - d ) + 
		( p < d ? 0 : p - d );
}

bool solve()
{
	int s, p, n, x, res = 0;
	scanf( "%d%d%d", &n, &s, &p );
	while ( n-- )
	{
		scanf( "%d", &x );
		if ( x >= get(p, 1) )
			res++;
		else
		if ( x >= get(p, 2) && s > 0 )
		{
			res++;
			s--;
		}
	}
	printf( "%d\n", res );
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
		solve( );
	}
//#endif
	return 0;
}