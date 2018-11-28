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
	char str[100] ;
	int arr[100] ;  ;
	char s[100] ;
	int base = 0; 
	while( t < tc ) {
		t++ ;
		fscanf(fin,"%s",s);
		int l = strlen( s) ;
		int cl = 1 ;
		
		str[0]=s[0] ; 
		str[1] = 0 ;
		base = 1 ;
		for( int i = 0 ; i < 100 ; i ++ ) {
			arr[i] = 0 ;
		}
		while( cl < l ) {
			char tmp = s[cl] ;
			s[cl] = 0 ;
			if( strchr(s,tmp) == NULL ) {
				char str1[2] ;
				str1[1] = 0 ;
				str1[0] = tmp ;
				
				strcat(str,str1) ;
				arr[base]=1;

				base++ ;
			}else{
				arr[strchr(s,tmp) - s ] ++ ;
			}
			s[cl] = tmp ;
			cl++ ;

		}

		/*for( int ii = 0 ; ii < base ; ii ++ ) {
			for( int jj = ii +1 ; jj < base ; jj ++ ) {
				if( arr[ii] > arr[ jj ] ) {
					int t = arr[ii] ;
					arr[ii] = arr[jj] ;
					arr[jj] = t ;
					char cc = str[ii] ;
					str[ii] = str[jj] ;
					str[jj] = cc ;

				}
			}
		}*/
		int l2 = strlen(s);
		ll mul = 1 ;
		ll sum = 0 ;
		if( l2 == 1 ) {
			fprintf(fout,"Case #%d: %d\n",t,1) ;
			fflush(fout) ;

		}else{
		for( int i = 0 ; i < l2 ; i ++ ) {
			/*if( l2 - 1 == i  ) {
				sum += mul * 1 ;
			}else if ( l2- 2 == i ) {
				sum += mul * 0 ;
			}else */{
				int tmp = s[l2-i-1] ;
				char *tt = strchr(str,tmp);
				int value = tt - str ;
				if( value == 0 ) {
					value = 1 ;
				}else if( value == 1 ) {
					value = 0 ;
				}
				sum += mul * value ;
			}
			mul = mul * base ;
		}
		
		fprintf(fout,"Case #%d: %ld\n",t,sum) ;
		fflush(fout) ;
		}


	}
}
