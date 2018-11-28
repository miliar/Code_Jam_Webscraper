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

	Chars[' '] = Chars['\n'] = Chars['\r'] = DELIMS;
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

void FillNext( int* digits, int* nodes, int index ) {
	for ( int i = 0; i < 10; ++i ) {
		if ( digits[ i ] > 0 ) {
			nodes[ index ] = i;
			--digits[ i ];
			FillNext( digits, nodes, index + 1 );
			return;
		}
	}
}

void FindNext( int* digits, int* nodes, int size ) {
	if ( size == 0 ) {
		for ( int i = 1;  i < 10; ++i ) {
			if ( digits[ i ] > 0 ) {
				nodes[ 0 ] = i;
				--digits[ i ];
				break;
			}
		}
		nodes[ 1 ] = 0;
		FillNext( digits, nodes, 2 );
		return;
	}

	for ( int i = nodes[ size - 1 ] + 1; i < 10; ++i ) {
		if ( digits[ i ] > 0 ) {
			++digits[ nodes[ size - 1 ] ];
			nodes[ size - 1 ] = i;
			--digits[ i ];
			FillNext( digits, nodes, size );
			return;
		}
	}

	digits[ nodes[ size - 1 ] ]++;
	FindNext( digits, nodes, size - 1 );
}


void main( int argc, char* argv[] )
{
	char*		content = NULL;
	try {
		char* current = content = Loading( argv[ 1 ] );
		Init();

		int cases = GetNumber( current ),
			now	  = 0;

		while ( now < cases ) {	
			int digits[ 10 ];
			for ( int i = 0; i < 10; ++i )
				digits[ i ] = 0;

			GetDelims( current );
			int nodes[ 20 ];
			for ( int i = 0; i < 20; ++i )
				nodes[ i ] = -1;

			int size = 0;
			while ( Chars[ *current ] == NUMBER ) {
				int key = *current - '0';
				nodes[ size ] = key;
				++size;
				++current;
			}
			GetDelims( current );

			FindNext( digits, nodes, size );

			int result = 0;
			for ( int i = 0; i < 20; ++i ) {
				if ( nodes[ i ] < 0 ) break;
				result = 10 * result + nodes[ i ];
			}

			printf( "Case #%d: %d\n", ++now, result );
		}
	}
	catch ( ErrMsg err ) {
		printf( "ERROR : %s\n", err.msg );
	}

	if ( content != NULL )	delete [] content;
}