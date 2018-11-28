# include <fstream>
# include <list>
# include <stdio.h>
using namespace std ;

char STR [ 261 ] ;
ifstream inf ;
ofstream outf ;

int T , N ;
unsigned long int CANDY ;
unsigned long int MIN_VALUE , SUM_SEAN , SUM_PATRICK ;

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
		/* Reading and processin data simulteneously */

		inf >> N ;
		SUM_PATRICK = SUM_SEAN = 0UL ;
		MIN_VALUE = 1000000 ;
		for ( int i ( 0 ) ; i < N ; ++i )
		{
			inf >> CANDY ;
			SUM_SEAN += CANDY ;
			SUM_PATRICK ^= CANDY ;
			if ( CANDY < MIN_VALUE )
				MIN_VALUE = CANDY ;
		}	

		/* Writing */

		outf << "Case #" << CASE << ": " ;
		if ( SUM_PATRICK == 0 )
			outf << SUM_SEAN - MIN_VALUE ;
		else
			outf << "NO" ;
		if ( CASE < T )
			outf << endl ;
	}

	inf.close ( ) ;
	outf.close ( ) ;

	return 0 ;
}
