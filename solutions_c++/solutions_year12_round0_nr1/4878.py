#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>

using namespace std ;

int ler_int( int *soma ){ // int de 32 bits

	int entrada[13], i=0 ;

	while( (entrada[i] = getc(stdin)) != '-' && (entrada[i] < '0' || entrada[i] > '9') && entrada[i] != EOF ){}

	if( entrada[i] == EOF ){ return EOF ; }

	while( (entrada[++i] = getc(stdin)) >= '0' && entrada[i] <= '9' ){}

	entrada[i] = '\0' ;

	*soma  = 0 ;
	i = 0 ;
	if( entrada[i] == '-' ){
		for(i++ ; entrada[i] ; ++i){
			*soma = *soma * 10 - (entrada[i] - '0') ;
		}
	}else{
		for( ; entrada[i] ; ++i){
			*soma = *soma * 10 + (entrada[i] - '0') ;
		}
	}

	return *soma ;
}


///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
//  
//	 /  / 2011
//
//
//  tempo:  segundos (recorde: )
//  memoria: 
//  ranking: 
//
//
//	Metodo:
//
//
//
//


int main(void){

	char map[] = "yhesocvxduiglbkrztnwjpfmaq" ;
	int t, Case = 0 ;
	string linha ;


	cin >> t ;
	getline(cin, linha) ;
	while( t-- )
	{
		printf("Case #%d: ", ++Case) ;
		getline(cin, linha) ;
		for(int i = 0 ; i < linha.size() ; i++)
		{
			if( linha[i] == ' ' )
				putc(' ', stdout) ;
			else
				putc(map[linha[i] - 'a'], stdout) ;
		}
		putc('\n', stdout) ;
	}

	return 0 ;
}



