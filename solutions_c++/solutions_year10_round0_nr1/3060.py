#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

FILE * fin = fopen("e:/cj/run/A-small-attempt0.in","r");
FILE * fout = fopen("e:/cj/run/b.out","w+");

int  readLine( char *strline ) {
	char dilim = '\n' ;
	char ch ;
	int offset = 0 ;

	while( fread(&ch,1,1,fin) == 1 ) {
		if( ch == '\n' ) {
			strline[offset] = '\0' ;
			offset ++ ;
			break;
		} else {
			strline[offset] = ch ;
			offset ++ ;
		}
	}
	return offset ;
}


int splitLine( char *strline, char ** arrstr  ) {
	char dilim = ' ' ;
	char ch ;
	int offset = 0 ;
	char *strelement = new char [9999] ;
	int off1 = 0 ;

	int retInt = 0 ;
	while(  true ) {
		ch = strline[offset] ;

		if( ch == '\0'  ) {
			strelement[off1] = '\0' ;
			arrstr[retInt] = strelement ;
			retInt ++ ;
			break ;
		} else if( ch == dilim  ) {
			
			strelement[off1] = '\0' ;
			off1 = 0 ;
			arrstr[retInt] = strelement ;
			strelement = new char [9999] ;
			retInt ++ ;
		} else {
			strelement[off1] = ch ;
			off1++;
			
		}
		offset ++ ;
	}
	return retInt ;
}



long long javab = 0 ;

int main () {

			
	char *sline = new char [99999] ;
	char * s = sline ;

	readLine( sline ) ;
	int notest = atoi(sline);
	int tc = 0 ;
	while( tc < notest ) {
		tc++;
		sline = s ;

		readLine( sline ) ;
		
		char * p = strchr(sline,' ');
		p[0] = NULL ;
		int N,K ;
		N = atoi(sline) ;
		
		sline = p+1 ;
		K = atoi(sline) ;

		int count = 1 ;

		for( int i = 0 ; i < N ; i++ ) {
				count = count * 2 ;
		}
		bool flg = false ;

		int remi = ( K +1 ) % count ;

		if( remi == 0 && K > 0 ) {
			fprintf(fout,"Case #%d: ON\n",tc);
		}else{
			fprintf(fout,"Case #%d: OFF\n",tc);
		}
		
		fflush(fout);
	}
	

}

