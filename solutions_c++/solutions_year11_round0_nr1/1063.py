# include <fstream>
# include <stdio.h>
using namespace std ;

char STR [ 261 ] ;
ifstream inf ;
ofstream outf ;

int T , N , N1 , N2 , Sec;
int separate [ 2 ][ 100 ] ;
int both [ 2 ][ 100 ] ;
char ch ;
# define ORANGE	0
# define BLUE	1
# define Orange(i)	(separate[ORANGE][i])
# define Blue(i)	(separate[BLUE][i])
# define Any(i)		(both[1][i])

int _rec ( int i , int i1 , int i2 , int pos1 , int pos2 )
{
	int REZ ( 0 ) ;
	int dist1 , dist2 ;
	
	while ( true )
	{
		if ( i1 == N1 )
		{
			for ( ; i2 < N2 ; ++i2 )
			{
				REZ += 1 + abs ( Blue(i2) - pos2 ) ;
				pos2 = Blue(i2) ;
			}
			break ;
		}
		if ( i2 == N2 )
		{
			for ( ; i1 < N1 ; ++i1 )
			{
				REZ += 1 + abs ( Orange(i1) - pos1 ) ;
				pos1 = Orange(i1) ;
			}
			break ;
		}

		dist1 = abs ( Orange(i1) - pos1 ) ;
		dist2 = abs ( Blue(i2) - pos2 ) ;

		if ( ORANGE == both[0][i] )
		{
			REZ += 1 + dist1 ;
			if ( dist1 < dist2 )
				if ( Blue(i2) > pos2 )
					pos2 += 1 + dist1 ;
				else
					pos2 -= 1 + dist1 ;
			else
				pos2 = Blue(i2) ;
			REZ += _rec ( i+1 , i1+1 , i2 , Orange(i1) , pos2 ) ;
			break ;
		}
		else
		{
			REZ += 1 + dist2 ;
			if ( dist2 < dist1 )
				if ( Orange(i1) > pos1 )
					pos1 += 1 + dist2 ;
				else
					pos1 -= 1 + dist2 ;
			else
				pos1 = Orange(i1) ;
			REZ += _rec ( i+1 , i1 , i2+1 , pos1 , Blue(i2) ) ;
			break ;
		}
	}

	return REZ ;
}

int main ( int argc , char * argv [ ] )
{
	printf ( "INPUT :\t" ) ;
	scanf ( "%s" , STR ) ;
	inf.open ( STR ) ;
	if ( inf.fail() ) return -1 ;
	outf.open ( "output.txt" ) ;
	if ( outf.fail() ) return -1 ;

	inf >> T ;
	for ( int CASE ( 1 ) ; CASE <= T ; ++ CASE )
	{
		/* Reading data */

		inf >> N ;
		N1 = N2 = 0 ;
		for ( int i ( 0 ) ; i < N ; ++i )
		{
			inf >> ch ;
			if ( 'O' == ch )
			{
				both [ 0 ][ i ] = ORANGE ;
				inf >> Any(i) ;
				Orange(N1++) = Any(i) ;
			}
			else
			{
				both [ 0 ][ i ] = BLUE ;
				inf >> Any(i) ;
				Blue(N2++) = Any(i) ;
			}
		}

		/* Processing */

		Sec = _rec ( 0 , 0 , 0 , 1 , 1 )
			;
		/* Writing */

		outf << "Case #" << CASE << ": " << Sec ;
		if ( CASE < T )
			outf << endl ;
	}

	inf.close ( ) ;
	outf.close ( ) ;

	return 0 ;
}
