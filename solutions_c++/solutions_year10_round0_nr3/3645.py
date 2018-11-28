#include <stdio.h>
#include <conio.h>


int main( void )
{
	int T; /* #cases */
	int R; /* run times in a day */
	int k; /* coaster capacity */
	int N; /* group count */
	int g[1000]; /* group size */
	int i; /* counter */
	int j; /* counter */
	int in; /* income */
	int head;
	int iter;
	int cursize = 0;

	scanf( "%d", &T );
	for( i=0; i<T; i++ )
	{
		scanf( "%d %d %d", &R, &k, &N );
		for( j=0; j<N; j++ )
			scanf( "%d", &g[j] );

		in = 0;
		head = 0;
		for( j=0; j<R; j++ )
		{
			cursize = 0;
			iter = 0;
			while( cursize + g[head] <= k )
			{
				cursize += g[head];
				head = (head+1) % N;

				iter ++;
				if( iter >= N )
					break;
			}

			in += cursize;
		}

		printf( "Case #%d: %d\n", i+1, in );
	}

	return 0;
}