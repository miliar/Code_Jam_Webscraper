#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

FILE * fin = fopen("e:/cj/A-small-practice.in","r");
FILE * fout = fopen("e:/cj/A-small-practice0.out","w");

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

void deleteArrStr( char ** arrstr,int size ) {
	for( int i = 0 ; i < size ; i ++ ) {
		delete arrstr[i] ;
	}
}

int javab = 0 ;

int rec( char **dic,char ** arr,int L,int D,int N , int dicid , int cln, int cp) {
	
	

	int i = 0 ;
	for( i = dicid ; i < D ; i ++ ) {
		if( dic[i][cln] == arr[cln][cp] ) {
			break;
		}
		for( int l = 0 ; l < cln && i +1 < D ; l++ ) {
			if( dic[i+1][l] != dic[i][l] ) {
				i = D-1;
				break ;
			}
		}
	}
	if( i != D ) {

		if( cln == L-1 ) {
			javab++; 
			return 1 ;
		}else {
			cln++;
			cp = 0 ;
			int t1= cp ;
			while( arr[cln][t1] != NULL ) {
				rec(dic, arr,L,D,N,i,cln,t1);
				t1++;
			}
		}

	}else {
		return 0 ;
		
	}
	
}

int slen = 0 ;
int arrlen = 0 ;

void recor( char * base , char *arr , int bi, int ai) {
	for( int i = bi ; i < slen ; i ++ ) {
		if( arr[ai] == base[i] ) {
			if( ai+1 < arrlen) {
				recor(base,arr,i,ai+1) ;
			} else {
				javab++;
			}
		}
	}
}

int main () {

			
	char *sline = new char [99999] ;
	char **arrstr = new char * [99999] ;

	char **dic = new char* [99999] ;

	readLine( sline ) ;
	int notest = atoi(sline);
	int tc = 0 ;
	while( tc < notest ) {
		tc++;
		readLine( sline ) ;
		javab = 0 ;
		
		slen = strlen( sline ) ;
		arrlen = strlen( "welcome to code jam" ) ;
		recor( sline , "welcome to code jam" , 0,0 ) ;

		fprintf(fout,"Case #%d: %.4d\n",tc,(int)javab);
		fflush(fout);
	}
	

}

