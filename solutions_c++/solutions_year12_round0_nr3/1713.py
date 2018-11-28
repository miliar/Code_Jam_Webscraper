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
	int *arr = new int[10000];
	while( t < tc ) {
		t++ ;
		int A = 0 ;
		int B = 0 ;
		int ans = 0;
		fscanf(fin,"%d%d",&A,&B);
		char str[1024];
		char newstr[1024] ;
		int slen= 0;
		int idx =0;

		for( int i = A ; i < B ; i++ ) {
			itoa(i,str,10);
			slen = strlen(str);
			idx=0;
			for( int j = 1;j<slen; j++) {
				if( str[0] > str[j] ) {
					continue;
				}
				strcpy(newstr,str+j);
				strcat(newstr,str);
				newstr[slen]='\0';
				int m = atoi(newstr);
				if( i < m && m <= B){
					//fprintf(fout,"run #%d: %d\n",i,m);
					int k =0;
					for( ; k<idx ; k++ ) {
						if( arr[k]==m){
							break;
						}
					}
					if( k == idx ) {
						arr[idx]=m;
						idx++;
						ans++;
					}
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
