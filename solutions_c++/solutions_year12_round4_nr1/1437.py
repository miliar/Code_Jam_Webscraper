#include<stdio.h>
#include<memory.h>

int N, K, H, T;

int D[ 10003 ];
int L[ 10003 ];

int Queue[ 10000003 ][ 2 ];

bool A[ 10003 ][ 10003 ];


int main() 
{
	int TC;

	scanf( "%d", &TC );

	for( int tt = 1; tt <= TC; tt ++ )
	{
		scanf( "%d", &N );
		for( int i = 1; i <= N; i ++ ) 
		{
			scanf( "%d", &D[ i ] );
			scanf( "%d", &L[ i ] );
		}
		scanf( "%d", &K );

		memset( A, 0, sizeof( A ) );
		H = T = 0;
	
		Queue[ H ][ 0 ] = 0;
		Queue[ H ][ 1 ] = 1;
		H ++;
		A[ 0 ][ 1 ] = true;

		do
		{
			int first = Queue[ T ][ 0 ];
			int second = Queue[ T ][ 1 ];
			int pos = D[ first ];
			int length;

			T ++;
			if( T >= 10000000 ) T = 0;
			
			if( first < second ) 
			{
				if( pos < D[ second ] - L[ second ] ) 
				{
					pos = D[ second ] - L[ second ];
					length = L[ second ];
				}
				else 
					length = D[ second ] - D[ first ];


				if( pos + length + length >= K ) 
				{
					T --;
					break;
				}

				for( int i = first + 1; i <= N; i ++ ) 
				{
					if( D[ i ] > pos + length + length ) break;
					if( A[ second ][ i ] ) continue;
					if( second == i ) continue;
					
					Queue[ H ][ 0 ] = second;
					Queue[ H ][ 1 ] = i;
					A[ second ][ i ] = true;
					H ++;
					if( H >= 10000000 ) H = 0;
				}
			}
			else
			{
				if( pos > D[ second ] + L[ second ] )
				{
					pos = D[ second ] + L[ second ];
					length = L[ second ];
				}
				else
					length = D[ first ] - D[ second ];

				
				for( int i = first - 1; i >= 1; i -- ) 
				{
					if( D[ i ] < pos - length - length ) break;
					if( A[ second ][ i ] ) continue;
					if( second == i ) continue;
					
					Queue[ H ][ 0 ] = second;
					Queue[ H ][ 1 ] = i;
					A[ second ][ i ] = true;
					H ++;
					if( H >= 10000000 ) H = 0;
				}

			}
			
		} while( H != T );

		if( H != T ) 
			printf( "Case #%d: YES\n", tt );
		else
			printf( "Case #%d: NO\n", tt );
	}

	return 0;
}
