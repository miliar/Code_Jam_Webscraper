// google_a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <stdio.h>

char scheme[255];

void proceed_key( const char* a, const char* b ){
	for(int i = 0; i < strlen(a); ++i )
		scheme[ a[i] ] = b[i];
}

void decode( int index, const char* a ){
	printf("Case #%d: ", index );
	for(int i = 0; i < strlen(a); ++i ){
		if ( a[i] == ' ' )
			printf(" ");
		else
			printf("%c", scheme[ a[i] ] );
	}
	printf("\n");
}

int _tmain(int argc, _TCHAR* argv[])
{
	memset( scheme, 0, sizeof(scheme) );

	scheme['z'] = 'q';
	scheme['q'] = 'z';

	proceed_key("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand" );
	proceed_key("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	proceed_key("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
/*
	for( char i = 'a'; i <= 'z'; ++i ){
		printf( "%c = %c\n", i, scheme[i] ? scheme[i] : '?' );
	}
*/
	FILE* f = fopen( "input", "rt" );
	char line[128];
	int i = 1;

	fgets ( line, sizeof line, f );
	while ( fgets ( line, sizeof line, f ) != NULL ){ /* read a line */
		decode( i++, line );
	}

	return 0;
}
