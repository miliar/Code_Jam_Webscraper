#include<stdio.h>

char buff[350];
int coresp[] = {0,25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};

int main () {
	
	FILE*f=fopen("speaking.in","r");
	FILE*g=fopen("speaking.out","w");
	
	int t;
	fscanf(f,"%d\n",&t);
	for ( int i = 1 ; i <= t ; ++i ){
		fgets(buff+1,300,f);
		
		fprintf(g,"Case #%d: ",i);
		for ( int i = 1 ; buff[i] == ' ' || (buff[i] >= 'a' && buff[i] <= 'z') ; ++i ){
			if ( buff[i] == ' ' ){
				fprintf(g," ");
			}
			else
				fprintf(g,"%c",coresp[buff[i]-'a'+1]+'a'-1);
		}
		fprintf(g,"\n");
	}
	
	return 0;
}
