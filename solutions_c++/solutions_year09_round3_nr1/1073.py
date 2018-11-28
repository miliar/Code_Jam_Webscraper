# include <stdio.h>
# include <cmath>
# include <string>

typedef char Str65[ 65 ];

int main()
{
	Str65 words;
	Str65 tempWords;
	int wordNum[ 65 ];
	int T;
	int n;
	int counter;
	int sum;


	scanf( "%d", &T );
	for ( int tc = 1 ; tc <= T ; ++tc )
	{
		scanf( "%s", &words );
		for ( int m = 0 ; m < 65 ; ++m )
		{
			tempWords[ m ] = '$';
			wordNum[ m ] = 0;
		} // for

		tempWords[ 0 ] = words[ 0 ];
		for ( int j = 1 ; words[ j ] != NULL ; ++j )
		{
			for ( n = 0 ; tempWords[ n ] != '$' ; ++n )
			{
				if ( words[ j ] == tempWords[ n ] )
					break;
			} // for

			if ( tempWords[ n ] == '$' )
			{
				tempWords[ n ] = words[ j ];
				// printf( "tempWords[ n ] = %c\n", tempWords[ n ] );
			} // if

		} // for

		for ( counter = 0 ; tempWords[ counter ] != '$' ; ++counter )
			;

		// printf( "counter ***** = %d\n", counter );
		wordNum[ 0 ] = 1;
		int p = 0;
		for ( int i = 1 ; i < strlen( words ) ; ++i )
		{
			for ( int j = 0 ; j < i ; ++j )
			{
				if ( words[ i ] == words[ j ] )
				{
					wordNum[ i ] = wordNum[ j ];
					break;
				} // if
			} // for

			if ( j == i )
			{
				if ( p == 1 )
				{
					++p;
				} // if

				wordNum[ i ] = p++;

			} // if
		
		} // for

		int len = strlen( words );
		int realLen = len;
		sum = 0;
		if ( len == 1 )
			sum = 1;
		else
		{

			if ( counter < 2 )
				counter = 2;
		for ( int x = 0 ; x < realLen ; ++x )
		{
         sum += pow( counter, ( len - 1 ) ) * wordNum[ x ];
			--len;
		} // for

		} // else

		// sum /= counter;
		// printf( "counter = %d\n", counter );
		printf( "Case #%d: %d\n", tc, sum );
	} // for

	return 0;
} // main()