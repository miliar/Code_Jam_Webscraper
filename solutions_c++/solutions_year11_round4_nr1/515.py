#include <stdio.h>
#include <algorithm>

int T;
int X, N;
int walk, run, runtime;

std::pair<int, int> data [ 1003 ] ; 

int main () 
{

	freopen("input.txt", "r" , stdin );
	freopen("output.txt", "w" , stdout );
	int test, i ; 
	scanf ( "%d", &T );

	double remain, result ; 

	for ( test = 1 ; test <= T ; test ++ ) 
	{

		scanf ("%d %d %d %d %d", &X, &walk, &run, &runtime, &N );
		run -= walk;
		remain = runtime;
		result = 0;

		for ( i = 1 ; i <= N ; i ++ ) 
		{
			int a, b; 
			scanf( "%d %d %d", &a, &b, &data[ i ].first );
			data[ i ].first += walk;
			data[ i ].second = b - a ; 
			X -= data[ i ] . second;
		}

		data[ 0 ].first = walk;
		data[ 0 ].second = X;
		std::sort( data , data + N + 1 ) ;

		for( i = 0 ; i <= N ; i ++ ) 
		{
			if( remain <= 1e-13 ) 
			{
				result += data[i].second/(double)data[i].first;
				continue;
			}

			if( data[ i ].second / (double) (data[ i ].first + run) <= remain + 1e-13 ) 
			{
				remain -= data[ i ].second / (double) (data[i].first+run);
				result += data[ i ].second / (double) (data[i].first+run);
			}
			else
			{
				result += remain;
				result += ( (double) data[i].second - remain * (double) (data[i].first+run) ) / (double) data[i].first;
				remain = 0 ;
			}
		}
		printf("Case #%d: %.13lf\n", test, result );

		
	}
	return 0;
}
