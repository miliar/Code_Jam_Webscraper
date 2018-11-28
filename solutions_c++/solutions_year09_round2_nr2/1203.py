#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

FILE * fin = fopen("e:/cj/a.in","r");
FILE * fout = fopen("e:/cj/a.out","w");
#define ll long long

int main () {

			
	int tc ;
	fscanf(fin,"%d",&tc);

	int t = 0 ;
	char str[50] ;
	char s[50] ;
	while( t < tc ) {
		t++ ;
		int no ,nt;
		ll d[30] ;
		ll d1[30] ;
		str[0] = '0' ;
		fscanf(fin,"%s",str+1 );
		strcpy( s,str) ;
		
		
		int l = strlen(s) ;
		int i = l-1 ;
		while ( i > 0 ) {

			if( s[i] > s[i-1] ) {
				int bb ;
				for(  bb = l-1 ; bb > i-1 ; bb-- ) {
					if( s[bb] > s[i-1] ) {
						break;
					}
				}
				
				char tmp = s[bb] ; 
				s[bb] = s[i-1] ;
				s[i-1] = tmp ;

				for( int j = i   ; j < l ; j++ ) {
					for( int k = j +1 ; k < l ; k++ ) {
						if( s[j] > s[k] ) {
							char tmp = s[j] ; 
							s[j] = s[k] ;
							s[k] = tmp ;
						}
										
					}
				}
				break ;
			}
			i -- ;
		}
		if( s[0] == '0' ) {
			fprintf(fout,"Case #%d: %s\n",t,s+1);
			fflush(fout);
		}else{
			fprintf(fout,"Case #%d: %s\n",t,s);
			fflush(fout);
		}
		/*nt = no ;
		int i = 0 ;
		for( i = 0 ; i < 30 && no > 0 ; i ++ ) {
			d1[i]= no % 10 ;
			if( d1[i] == 0 ) {
				i -- ;
			}
			no = no / 10 ;
		}
		for ( int j = 0 ; j < i ; j ++ ) {
			d[j] = d1[i -j -1 ] ;
		}
		d[i]= 0;

		for ( int j = 0 ; j <= i ; j ++ ) {
			for ( int k = j+1 ; k <= i ; j ++ ) {
				if( d[j] < d[k] ) {
					ll tm = d[j] ; 
					d[j] = d[k] ;
					d[k] = tm ;
				}
			}
		}
		int I = i ;
		no = nt ;
		for( i = 0 ; i < 30 && no > 0 ; i ++ ) {
			d1[i]= no % 10 ;
			no = no / 10 ;
		}

		int kk = 0 ;
		while ( kk < I ) {
			if( d1[kk] != d[kk] ) {
				
				break ;
			}
		}
		//fprintf(fout,"Case #%d: %.4d\n",tc,(int)tc);
		//s(fout);
		*/
	}
}
