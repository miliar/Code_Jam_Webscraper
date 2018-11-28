#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

FILE * fin = fopen("f:/cj/a.in","r");
FILE * fout = fopen("f:/cj/a.out","w");
#define ll long long

int main () {

			
	int tc ;
	fscanf(fin,"%d",&tc);
	int t = 0 ;
	
	while( t < tc ) {
		t++ ;
		int N = 0 ;
		fscanf(fin,"%d",&N);
		int a[1010] , b[1010] ;
		int ans = 0 ;
		for( int i = 0 ; i < N ;i++ ) {
			fscanf(fin,"%d%d",(a+i),(b+i));
			for( int j = 0 ; j < i ; j++ ) {
				if(( a[i] < a[j] && b[i]>b[j] ) || ( a[i] > a[j] && b[i]<b[j] )) {
					ans++ ;
				}
			}
		}
		fprintf(fout,"Case #%d: %d\n",t,ans);
		
	}

	
	fflush(fout);
	fclose(fout) ;
	fclose(fin);

	return 0 ;

}
