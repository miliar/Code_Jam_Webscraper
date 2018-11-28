#include<stdio.h>

int main () {
	freopen ( "input.txt" , "r" , stdin ) ;
	freopen ( "output.txt" , "w" , stdout ) ;
	int TESTCase ;
	int i , j , k ;
	char input [ 5 ][ 5 ] ;
	int check_x [ 5 ] , check_y [ 5 ] , check_r1 , check_r2 ;
	bool check_draw ;
	scanf ( "%d" , &TESTCase ) ;

	for ( k = 1 ; k <= TESTCase ; k ++ ) {
		for ( i = 0 ; i < 4 ; i ++ ) {
			scanf ( "%s" , input [ i ] ) ;
			//printf ( "%s\n" , input [ i ] ) ;
			check_x [ i ] = check_y [ i ] = 0 ;
		}
		check_r1 = check_r2 = 0 ;
		//printf ( "\n" ) ;
		check_draw = true ;

		for ( i = 0 ; i < 4 ; i ++ ) {
			for ( j = 0 ; j < 4 ; j ++ ) {
				if ( input [ i ][ j ] == 'O' ) {
					check_x [ i ] ++ ;
					check_y [ j ] ++ ;
				}
				else if ( input [ i ][ j ] == 'X' ) {
					check_x [ i ] -- ;
					check_y [ j ] -- ;
				}
				else if ( input [ i ][ j ] == 'T' ) {
					check_x [ i ] += 10 ;
					check_y [ j ] += 10 ;
				}
				else check_draw = false ;
			}

			j = 3 - i ;
			if ( input [ i ][ i ] == 'O' ) check_r1 ++ ;
			else if ( input [ i ][ i ] == 'X' ) check_r1 -- ;
			else if ( input [ i ][ i ] == 'T' ) check_r1 += 10 ;
			if ( input [ i ][ j ] == 'O' ) check_r2 ++ ;
			else if ( input [ i ][ j ] == 'X' ) check_r2 -- ;
			else if ( input [ i ][ j ] == 'T' ) check_r2 += 10 ;

		}

		if ( check_r1 == 4 || check_r1 == 13 || check_r2 == 4 || check_r2 == 13 ) {
			printf ( "Case #%d: O won\n" , k ) ;
			continue ;
		}
		else if ( check_r1 == -4 || check_r1 == 7 || check_r2 == -4 || check_r2 == 7 ) {
			printf ( "Case #%d: X won\n" , k ) ;
			continue ;
		}
		for ( i = 0 ; i < 4 ; i ++ ) {
			if ( check_x [ i ] == 13 || check_x [ i ] == 4 || check_y [ i ] == 13 || check_y [ i ] == 4 ) {
				printf ( "Case #%d: O won\n" , k ) ;
				break ;
			}
			else if ( check_x [ i ] == -4 || check_x [ i ] == 7 || check_y [ i ] == -4 || check_y [ i ] == 7 ) {
				printf ( "Case #%d: X won\n" , k ) ;
				break ;
			}
		}
		if ( i != 4 ) continue ;
		if ( check_draw ) printf ( "Case #%d: Draw\n" , k ) ;
		else printf ( "Case #%d: Game has not completed\n" , k ) ;

	}

	return 0 ;
}