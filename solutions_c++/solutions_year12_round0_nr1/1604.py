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
	
	char ostr[1024] ;
	char mstr[1024] ;
	char abcd[100] ;

	strcpy(ostr,"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq");
	strcpy(mstr,"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz");
	int i=0;
	for( ; i < 26 ; i++ ) {
		char *ptr = strchr(ostr,'a'+i);
		if( ptr == NULL ) {
				abcd[i]= 'Z';
		} else {
			int idx = ptr -ostr ;

			abcd[ostr[idx]-'a']= mstr[idx];
		}
	}
	
	abcd[i]=0;

	char input[1024];
	
	fgets(input,1024,fin);

	while( t < tc ) {
		t++ ;
		fgets(input,1024,fin);
		
		for( int i = 0 ; i < strlen(input) ; i++ ) {
			if( input[i] >='a' && input[i]<='z'  ) {
				input[i]= abcd[input[i]-'a'];
			}
		}
		input[strlen(input)-1]=0;
		fprintf(fout,"Case #%d: %s\n",t,input);
				
	}

	delete(arr);
	fflush(fout);
	fclose(fout) ;
	fclose(fin);

	return 0 ;

}
