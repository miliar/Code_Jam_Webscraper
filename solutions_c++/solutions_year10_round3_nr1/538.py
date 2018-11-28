#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
int n;
int A[ 1005 ];
int B[ 1005 ];
int ans;
void read()
{
	scanf( "%d" , &n );
	for(int i = 0;i < n;++i)
		scanf( "%d%d" , A + i , B + i );
}

void work()
{
	int i, j;
	ans = 0;
	for(i = 0;i < n;++i)
		for(j = i + 1;j < n;++j)
		{
			if( A[ i ] > A[ j ] && B[ i ] < B[ j ] ) ans++;
			if( A[ i ] < A[ j ] && B[ i ] > B[ j ] ) ans++;
		}
}

void write(int test)
{
	printf( "Case #%d: %d\n" , test , ans );
}

int main()
{
	freopen(  "A-large.in" , "r" , stdin  );
	freopen( "out.txt" , "w" , stdout );

	int t;
	scanf( "%d" , &t );
	for(int test = 1;test <= t;++test)
	{
		read();
		work();
		write( test );
	}

	return 0;
}