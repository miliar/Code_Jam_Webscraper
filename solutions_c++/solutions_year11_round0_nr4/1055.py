# include <fstream>
# include <list>
# include <stdio.h>
using namespace std ;

char STR [ 261 ] ;
ifstream inf ;
ofstream outf ;

int T , N ;
int INPUT [ 1000 ] ;

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
		for ( int i ( 0 ) ; i < N ; ++i )
			inf >> INPUT [ i ] ;

		/* Processing */

		int REZ ( 0 ) ;
		while ( true )
		{
			int i ( 0 ) ;
			while ( i < N )
				if ( INPUT[i] > 0 )
					break ;
				else ++ i ;
			if ( i == N )
				break ;
			if ( INPUT [ i ] == i+1 )
			{
				INPUT [ i ] = 0 ;
				continue ;
			}
			while ( INPUT [i] > 0 )
			{
				++ REZ ;
				int j ( INPUT [ i ] - 1 ) ;
				INPUT [ i ] = 0 ;
				i = j ;
			}
		}

		/* Writing */

		outf << "Case #" << CASE << ": " << REZ ;
		if ( CASE < T )
			outf << endl ;
	}

	inf.close ( ) ;
	outf.close ( ) ;

	return 0 ;
}
