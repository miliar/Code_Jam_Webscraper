#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
char str[100][100],q[1000][100];
int main ()
{
    int N;
	int Q,S , i , j , p , P,ans;
	int test = 0;
	freopen( "A-large.in" ,"r" , stdin );
	freopen( "out.txt", "w", stdout );
	scanf( "%d" , &N );
	while( N -- ) 
	{
		test++;
		scanf( "%d\n", &S );
		for(i = 0; i < S; i++)
		{
			gets( str[i] );
		}
		scanf ( "%d\n" , &Q );
		for(i = 0; i < Q; i++)
		{
			gets( q[i] );
		}
		ans = P = p = 0;
		while ( p < Q )
		{
			for(i = 0; i < S; i++)
			{
				for(j = p; j < Q; j++)
				{
					if( strcmp(q[j] , str[i]) == 0 ) break;
				}
				P = max( P , j - p );

			}
			p += P;
			P = 0;
			if( p < Q )ans++;
		}
		printf( "Case #%d: %d\n" ,test, ans );

	}
	return 0;
}