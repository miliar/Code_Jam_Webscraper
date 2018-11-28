#include<stdio.h>
#include<memory.h>
#include<string.h>

int T, N, M;

int len[ 103 ];

char data [ 103 ] [ 13 ];
char list [ 13 ] [ 33 ];

bool check [ 103 ] ;
bool alphabet [ 33 ] ;

void process ( )
{
	int i, j, k, l , a, cnt, res, resk  ;

	bool f;

	for ( i = 1 ; i <= M ; i ++ ) 
	{
		res = -1 ; 
		for( j = 1 ; j <= N ; j ++ ) 
		{
			memset( check, 0, sizeof( check ) );
			cnt = 0;

			for( a = 0 ; a < 26 ; a ++ ) 
			{
				memset( alphabet, 0, sizeof( alphabet ) );
				f = false;

				for( k = 1 ; k <= N ; k ++ ) 
				{
					if( check [ k ] == true ) continue ; 
					if( len [ k ] != len [ j ] ) continue ; 

					for( l = 0 ; l < len [ k ] ; l ++ ) 
					{
						alphabet [ data[ k ] [ l ] - 'a' ] = true ; 
						if( data[ j ] [ l ] == list [ i ] [ a ] ) 
						{
							f = true ; 
						}
					}
				}
				if( alphabet [ list [ i ] [ a ] - 'a' ] )
				{
					if( f == false ) 
						cnt ++;
					for( k = 1 ; k <= N ; k ++ ) 
					{
						if( check [ k ] == true ) continue;
						if( len [ k ] != len [ j ] ) continue ;

						for ( l = 0 ; l < len [ k ] ; l ++ ) 
						{
							if( ( data [ k ] [ l ] != list[ i ] [ a ] && data [ j ] [ l ] == list [ i ] [ a ] ) ||
								( data [ k ] [ l ] == list[ i ] [ a ] && data [ j ] [ l ] != list [ i ] [ a ] ) )
								check [ k ] = true ; 
						}
					}
				}
			}
			if( res < cnt ) 
			{
				res = cnt ;
				resk = j ; 
			}
		}
		printf("%s ", data[ resk ] );
	}
	printf("\n" );
}

void input ( ) 
{
	FILE *fp = stdin ; 

	int i;

	fscanf ( fp, "%d" , &T );

	for( int c = 1 ; c <= T ; c ++ ) 
	{
		fscanf( fp , "%d %d", &N , &M );

		for ( i = 1 ; i <= N ; i ++ ) 
		{
			fscanf ( fp , "%s", data[i] );
			len[i]=strlen(data[i]);
		}

		for( i = 1 ; i <= M ; i ++ ) 
			fscanf ( fp , "%s", list[i]);

		printf("Case #%d: ", c );
		process( ) ;
	}

	fclose ( fp ) ;
}

int main ( ) 
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	input ( );
	return 0;
}