#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<fstream>
#include<queue>
#define MAXSIZE 10000
using namespace std;

int main()
{
	freopen( "D-large.in", "r", stdin );
	freopen( "D-large.out", "w", stdout );
	int datacase, t = 0, n , a[MAXSIZE], b[MAXSIZE];
	scanf( "%d", &datacase );
	while( datacase-- )
	{
		int q = 0;
		scanf("%d", &n );
		for( int i = 0; i < n; i++ )
		{
			scanf("%d", &a[i] );
			b[i] = a[i];
		}
		sort( a, a+n );
		for( int i = 0; i < n; i++ )
			if( a[i] != b[i] )
				q++;
		printf("Case #%d: %d.000000\n", ++t, q );
	}	
	return 0;
}
