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
		int M = 0 ;
		fscanf(fin,"%d%d",&M,&N);
		short matrix[512][512] ;
		
		int res[512] ;
		memset(res,0,512*4);


		int ans = 0 ;
		char str[512] ;
		for( int i = 0 ; i < M ;i++ ) {
			fscanf(fin,"%s",str);
			
			for( int j = 0 ; j < N/4 ; j ++ ) {
				if( str[j] <= '9') {
					str[j] = str[j] -'0' ;
				}else{
					str[j] = str[j] -'A' + 10;
				}
				int a = 8 ;
				int a1 = 4 ;
				int a2 = 2 ;
				int a3 = 1 ;
				matrix[i][j*4] = (str[j] & a ) != 0;
				matrix[i][j*4+1] = (str[j] & a1)  != 0;
				matrix[i][j*4+2] = (str[j] & a2) != 0;
				matrix[i][j*4+3] = (str[j] & a3) != 0;
			}
		}

		int K = M ;
		if( N < M ) {
			K = N ;
		}
		for( int i = K ; i > 0 ; i -- ) {
			int ic = 0 ;
			for( int y = 0 ; y < M ; y ++ ) {
				for(int x = 0 ; x < N ; x++ ) {
					
					
					if( matrix[y][x] == 2 ) {
						continue ;
					}

					int jj ; 
					int v = matrix[y][x] ;

					for( jj = y ; jj < y + i ; jj++ ) {
						int v1 = v ;
						v =!v ;
						int ii =0 ;
						for(  ii = x ; ii < x + i ; ii ++ ) {
							
							if( matrix[jj][ii] != v1 ) {
								break;
							}else {
								v1 = !v1 ;
							}
						}
						if( ii != x+i) {
							break ;
						}
					}
					if( jj == y+i ) {
						res[i]++ ;
						if( res[i] == 1 ) {
							ans++ ;
						}
						for( jj = y ; jj < y + i ; jj++ ) {
							int ii =0 ;
							for(  ii = x ; ii < x + i ; ii ++ ) {
								matrix[jj][ii] = 2 ;
									
							}
						}
					}
				}
			}
		}

		
		fprintf(fout,"Case #%d: %d\n",t,ans);
		for( int i = K ; i > 0 ; i -- ) {
			if( res[i] > 0 ) {
				fprintf(fout,"%d %d\n",i,res[i]);
			}
		}
		
	}

	
	fflush(fout);
	fclose(fout) ;
	fclose(fin);

	return 0 ;

}
