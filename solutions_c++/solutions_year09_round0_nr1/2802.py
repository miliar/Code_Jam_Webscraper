# include <stdio.h>

typedef char Str20[ 20 ];

int main()
{
	int L, D, N;
	Str20 dic[ 5005 ];
	char word[ 2000 ];
	char set[ 50 ][ 50 ];
	char * charPtr;
	int m, n;

	scanf( "%d %d %d", &L, &D, &N );
	for ( int i = 0 ; i < D ; ++i )
		scanf( "%s", &dic[ i ] );



	

	int a = 0;
	for ( int t = 1 ; t <= N ; ++t ) // run all test cases
	{

		scanf( "%s", &word );
		m = 0;
		for ( charPtr = word ; ( *charPtr ) != 0 ; ++charPtr )
		{
			n = 0;
			if ( *charPtr == '(' )
			{
				for ( ++charPtr ; *charPtr != ')' ; ++charPtr )
				{
					set[ m ][ n++ ] = *charPtr;
				} // for

			} // if
			else
			{
				set[ m ][ n++ ] = *charPtr;
			} // else

			set[ m ][ n ] = 0;
			++m;
		} // for // *charPtr != '\n'





		int sum = 0;
		int counter = 0;
		a = 0;
		int i = 0;
		int j = 0;
    while ( a < D )
		{

			if ( dic[ a ][ i ] == set[ i ][ j ] ) // the ith word, and there are j possibilities of the word
			{			

				

				++i;
				j = 0;
				if ( i == L )
				{
					sum += 1;
					++a;
					i = 0;
					j = 0;
				} // if
			} // if
			else
			{
				++j;
				if ( set[ i ][ j ] == 0 )
				{
					++a;
					i = 0;
					j = 0;
				} // if
			} // else
		} // while

		printf( "Case #%d: %d\n", t, sum );
	} // for


} // main()

