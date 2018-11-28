#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

FILE * fin = fopen("e:/cj/run/C-small-attempt0.in","r");
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
		int N,R,k ;
		R = atoi(sline) ;
		sline = p+1 ;
		p = strchr(sline,' ');
		p[0] = NULL ;
		k = atoi(sline) ;

		sline = p+1 ;
		N = atoi(sline) ;

		int g[1000] ;
		sline = s ;
		readLine( sline ) ;

		int i = 0 ;
		while( i < N-1 ) {
			p = strchr(sline,' ');
			p[0] = NULL ;
			g[i] = atoi(sline) ;
			sline = p+1 ;
			i++ ;
		}
		g[i] = atoi(sline) ;

		int index = 0 ;

		int roller = 0 ;

		for( int i = 0 ; i < R ; i ++ ) {
			long long sum = 0 ;
			int j=0  ;
			
			/*if( i != 0 && index == 0 ) {
				int rc = R / i ;
				javab = javab * rc ;
				i = R - rc * i ;
				continue ;
			}*/
			bool flg = false ; 
			for( j=0  ; j< N ; j++) {
				sum += g[index] ;
				if( sum > k ) {
					sum -= g[index] ;
					flg = true ;
					break ;
				}else {
					index = (index +1 ) %N ;
					
				}
			}
			if( j != N && flg == false ) {
				javab =0 ; 
				javab = ( sum )  * R ;
				break ;
			}

			javab = javab +  sum ;
			
		}
		fprintf(fout,"Case #%d: %ld\n",tc,javab);
		javab = 0 ;
		fflush(fout);
	}
	

}

