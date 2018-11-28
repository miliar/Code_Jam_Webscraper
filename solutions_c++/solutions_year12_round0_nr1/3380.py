#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

int n, m;

char mapper[26];

char str_a[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char str_b[] = {"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"};



int main() {

	int t=0, tt=0;
			

	int i;	
	for( i=0; i<strlen( str_a ); i++ ) {
		if( str_a[i] == ' ' ) continue;
		mapper[ str_a[i] - 'a' ] = str_b[i];
	}
	
	mapper['z'-'a'] = 'q';
	mapper['q'-'a'] = 'z';	
	
	/*
	for( i=0; i<26; i++ ) {
		printf("map %c -> %c\n", i+'a', mapper[i] );
	}
	*/
	
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );



	scanf( "%d\n", &tt );
	
	char str [1024];

	for( t=1; t<=tt; t++ ) {
	
	
		printf( "Case #%d: ", t );
		gets( str );
		
		//printf("str>> %s\n", str );
		
		for( i=0; i<strlen( str ); i++ ) {
			if( str[i] == ' ' ) {
				printf(" ");
			}else {
				printf( "%c", mapper[ str[i] -'a' ] );
			}
		}
		
		printf("\n");
	}



	return 0;
}
