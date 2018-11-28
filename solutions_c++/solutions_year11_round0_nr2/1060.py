# include <fstream>
# include <list>
# include <stdio.h>
using namespace std ;

char STR [ 261 ] ;
ifstream inf ;
ofstream outf ;

int T , C , D , N ;
char ch1 , ch2 , ch3 ;
char INPUT [ 100 ] ;
char COMBINE [ 26 ][ 26 ] ;
bool OPPOSE [ 26 ][ 26 ] ;
list < char > OUTPUT ;
list < char > :: iterator I ;
list < char > :: reverse_iterator R_I ;

# define CHAR_TO_NUM(ch)	((ch)-'A')
# define combine(ch1,ch2)	(COMBINE[CHAR_TO_NUM(ch1)][CHAR_TO_NUM(ch2)]!=0)
# define oppose(ch1,ch2)	(OPPOSE[CHAR_TO_NUM(ch1)][CHAR_TO_NUM(ch2)])

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

		for ( int i ( 0 ) ; i < 26 ; ++i )
			for ( int j ( 0 ) ; j < 26 ; ++j )
				COMBINE [ i ][ j ] = 0 ,
				OPPOSE [ i ][ j ] = false ;
		inf >> C ;
		for ( int i ( 0 ) ; i < C ; ++i )
		{
			inf >> ch1 >> ch2 >> ch3 ;
			COMBINE [ CHAR_TO_NUM(ch1) ][ CHAR_TO_NUM(ch2) ] =
				COMBINE [ CHAR_TO_NUM(ch2) ][ CHAR_TO_NUM(ch1) ] = ch3 ;
		}
		inf >> D ;
		for ( int i ( 0 ) ; i < D ; ++i )
		{
			inf >> ch1 >> ch2 ;
			OPPOSE [ CHAR_TO_NUM(ch1) ][ CHAR_TO_NUM(ch2) ] =
				OPPOSE [ CHAR_TO_NUM(ch2) ][ CHAR_TO_NUM(ch1) ] = true ;
		}
		inf >> N ;
		for ( int i ( 0 ) ; i < N ; ++i )
			inf >> INPUT [ i ] ;

		/* Processing */

		OUTPUT.clear ( ) ;
		for ( int i ( 0 ) ; i < N ; ++i )
		{
			bool bCLEAR ( false ) ;
			R_I = OUTPUT.rbegin() ;
			if ( R_I != OUTPUT.rend() )
				if ( combine((*R_I),INPUT[i]) )
				{
					(*R_I) = COMBINE[CHAR_TO_NUM(*R_I)][CHAR_TO_NUM(INPUT[i])] ;
					continue ;
				}
			for ( I = OUTPUT.begin() ; I != OUTPUT.end() ; ++ I )
				if ( oppose((*I),INPUT[i]) )
				{
					bCLEAR = true ;
					break ;
				}
			if ( bCLEAR )
				OUTPUT.clear ( ) ;
			else
				OUTPUT.push_back ( INPUT[i] ) ;
		}

		/* Writing */

		outf << "Case #" << CASE << ": [" ;
		if ( ! OUTPUT.empty() )
		{
			I = OUTPUT.begin() ;
			outf << (*I) ;
			for ( ++I ; I != OUTPUT.end() ; ++I )
				outf << ", " << (*I) ;
		}
		outf << "]" ;
		if ( CASE < T )
			outf << endl ;
	}

	inf.close ( ) ;
	outf.close ( ) ;

	return 0 ;
}