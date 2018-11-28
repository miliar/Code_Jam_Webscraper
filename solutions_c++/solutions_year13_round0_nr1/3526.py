#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//		#define out stdout
//		#define in stdin

int price[1001];

int main(void)
{
#ifndef in
	FILE *in;
	in=fopen("A-large.in","rt");
	if(in==NULL){
		printf("\a");
		return -1;
	}
#endif
#ifndef out
	FILE *out;
	out=fopen("a.txt","wt");
	if(out==NULL){
		printf("\a");
		return -1;
	}
#endif
	
	char str[4][5];
	int n,t,i,O,X,T,j;
	char ok;
	fscanf(in,"%d",&t);
	for(n=1;n<=t;++n){
		fprintf(out,"Case #%d: ",n);
		for(i=0;i<4;++i)
			fscanf(in,"%s",str[i]);
		ok=0;
		for(i=0;i<4;++i){
			O=X=T=0;
			for(j=0;j<4;++j){
				switch( str[i][j] ){
					case 'X': ++X; break;
					case 'O': ++O; break;
					case 'T': ++T; break;
				}
			}
			if( X==4 || (X==3 && T==1) ){
				fprintf(out,"X won\n");
				ok=1;
				break;
			}
			if(O==4 || (O==3 && T==1)){
				fprintf(out,"O won\n");
				ok=1;
				break;
			}
		}
		if(ok)
			continue;
		
		for(j=0;j<4;++j){
			O=X=T=0;
			for(i=0;i<4;++i){
				switch(str[i][j]){
				case 'X': ++X; break;
				case 'O': ++O; break;
				case 'T': ++T; break;
				}
			}
			if(X==4 || (X==3 && T==1)){
				fprintf(out,"X won\n");
				ok=1;
				break;
			}
			if(O==4 || (O==3 && T==1)){
				fprintf(out,"O won\n");
				ok=1;
				break;
			}
		}
		if(ok)
			continue;
		
		O=X=T=0;
		for(i=0;i<4;++i){
			switch(str[i][i]){
				case 'X': ++X; break;
				case 'O': ++O; break;
				case 'T': ++T; break;
			}
		}
		if(X==4 || (X==3 && T==1)){
			fprintf(out,"X won\n");
			continue;
		}
		if(O==4 || (O==3 && T==1)){
			fprintf(out,"O won\n");
			continue;
		}
		O=X=T=0;
		for(i=0;i<4;++i){
			switch(str[i][3-i]){
				case 'X': ++X; break;
				case 'O': ++O; break;
				case 'T': ++T; break;
			}
		}
		if(X==4 || (X==3 && T==1)){
			fprintf(out,"X won\n");
			continue;
		}
		if(O==4 || (O==3 && T==1)){
			fprintf(out,"O won\n");
			continue;
		}
		
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				if(str[i][j]=='.'){
					fprintf(out,"Game has not completed\n");
					ok=1;
					i=4;
					break;
				}
		if(!ok)
			fprintf(out,"Draw\n");
	}

	fclose(out);
	return 0;
}

