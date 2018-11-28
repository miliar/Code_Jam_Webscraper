#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

int TT[26];  // Translation Table

int main(){
	int T;
	char line[100];
	scanf("%d\n",&T);
	char c;

	for( int j=0; j<26; j++ )
		TT[j]=0;
	TT['a'-'a']='y';
	TT['b'-'a']='h';
	TT['c'-'a']='e';  
	TT['d'-'a']='s'; 
	TT['e'-'a']='o';
	TT['f'-'a']='c';
	TT['g'-'a']='v';
	TT['h'-'a']='x';
	TT['i'-'a']='d';
	TT['j'-'a']='u';
	TT['k'-'a']='i';
	TT['l'-'a']='g';
	TT['m'-'a']='l';
	TT['n'-'a']='b';
	TT['o'-'a']='k';
	TT['p'-'a']='r';
	TT['q'-'a']='z'; //
	TT['r'-'a']='t'; 
	TT['s'-'a']='n';
	TT['t'-'a']='w';
	TT['u'-'a']='j';
	TT['v'-'a']='p';
	TT['w'-'a']='f';
	TT['x'-'a']='m';
	TT['y'-'a']='a';
	TT['z'-'a']='q'; //
	//TT[25]=

	for(int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		while( (c = getchar())!='\n' ){
			if(c!=' ')
				printf("%c",TT[c-'a']);
			else
				printf("%c",c);
			//printf("%c",(int)'a');
		}
		printf("\n");
	}

	return 0;
}
