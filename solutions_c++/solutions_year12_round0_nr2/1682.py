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
	int *arr = new int[200];
	while( t < tc ) {
		t++ ;
		int N = 0 ;
		int S = 0 ;
		int P = 0;
		int ans=0;
		fscanf(fin,"%d%d%d",&N,&S,&P);
		if( P == 0 ) {
			for( int i = 0 ; i < N ; i++ ) {
				fscanf(fin,"%d",(arr+i));
			}
			ans = N;
		} else if ( P == 1 ) {
			for( int i = 0 ; i < N ; i++ ) {
				fscanf(fin,"%d",(arr+i));
				if( arr[i]>0){
					ans++;
				}
			}
		}else  {
		
			for( int i = 0 ; i < N ; i++ ) {
				fscanf(fin,"%d",(arr+i));
				
				if( arr[i] >= P*3-2 ) {
						ans++;
				} else if ( arr[i] >= P*3-4 && S > 0 ) {
					S--;
					ans++;
				}
			}
		}
				
		fprintf(fout,"Case #%d: %d\n",t,ans);
				
	}

	delete(arr);
	fflush(fout);
	fclose(fout) ;
	fclose(fin);

	return 0 ;

}
