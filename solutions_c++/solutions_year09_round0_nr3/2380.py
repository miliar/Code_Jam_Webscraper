// Qualification1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "stdlib.h"
#include "string.h"
#include <new>

using std::bad_alloc;

#pragma warning(disable:4996)

enum { INVALID = 0, NUMBER = 1, LETTER = 2, DELIMS = 3 };
int Chars[ 256 ];

struct ErrMsg {
	const char* msg;
	ErrMsg( const char* info ) : msg( info ) {}
};


char* Loading ( const char* filename ) {
	FILE* input		= NULL;
	char* word = NULL;
	try {
		if ( ( input = fopen( filename, "rb" ) ) == NULL ) throw ErrMsg( "failed to open input file" );

		fseek( input, 0, 2 );
		int size = ftell( input );
		fseek( input, 0, 0 );

		word = new char[ size + 1 ];
		word[ size ] = '\0';
		if ( fread( word, sizeof( char ), size, input ) != size ) throw ErrMsg( "failed to read out all of word from input file" );

		fclose( input );

		return word;
	}
	catch( bad_alloc err ) {
		printf ( "%s\n",  err.what() );
		throw ErrMsg ( "failed to allocate a char buff" );
	}
	catch ( ErrMsg ) {
		printf( "%s", word );
		if ( input != NULL ) fclose( input);
		if ( word != NULL ) { delete [] word; word = NULL; }
		throw;
	}
}

void Init () {
	for ( int i = 0; i < 256; ++i )
		Chars[ i ] = INVALID;

	for ( int i = 0; i < 10; ++i )
		Chars[ i + '0' ] = NUMBER;

	for ( int i = 0; i < 26; ++i )
		Chars[ i + 'a' ] = LETTER;
	Chars[ ' ' ] = LETTER;

	Chars['\n'] = Chars['\r'] = DELIMS;
}


inline void GetDelims ( char*& word ) {
	while ( Chars[ *word ] == DELIMS ) ++word;
}


inline int GetNumber ( char*& word ) {
	char* literal = word;
	while( Chars[ *word ] == NUMBER ) ++word;
	*(word++) = '\0';

	GetDelims( word );

	return atoi ( literal );
}


inline char* GetString( char*& word ) {
	char* string = word;
	while ( Chars[ *word ] == LETTER ) ++word;
	*(word++) = '\0';
	GetDelims( word );

	return string;
}

const char* patterns = "welcome to code jam";

int FindPatterns( char* content, int pattern_id ) {
	int result = 0;

	if ( pattern_id == 18 ) {		// last letter of pattern
		while( *content != '\0' ) {
			if ( *content == patterns[pattern_id] ) ++result;
			++content;
		}
		return result;
	}
	
	while( *content != '\0' ) {
		if ( *content == patterns[pattern_id] ) 
			result += FindPatterns( content + 1, pattern_id + 1 );
		++content;
	}
	return result;
}

void main( int argc, char* argv[] )
{
	char*		content = NULL;
	try {
		char* current = content = Loading( argv[ 1 ] );
		Init();

		int lines = GetNumber( current ),
			i	  = 0;

		while ( i < lines ) {
			printf( "Case #%d: %.4d\n", ++i, FindPatterns( GetString( current ), 0 ) );
		}
	}
	catch ( ErrMsg err ) {
		printf( "ERROR : %s\n", err.msg );
	}

	if ( content != NULL )	delete [] content;
}