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
	Chars['.'] = NUMBER;

	for ( int i = 0; i < 26; ++i )
		Chars[ i + 'a' ] = LETTER;
	Chars[ ' ' ] = LETTER;

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

inline double GetFloat ( char*& word ) {
	char* literal = word;
	while( Chars[ *word ] == NUMBER ) ++word;

	bool flag = *word == ')' ? true : false;
	*(word++) = '\0';

	GetDelims( word );

	double result = (double)atof ( literal );
	if ( flag == true ) { word--; *word = ')'; }

	return result;
}


inline char* GetString( char*& word ) {
	char* string = word;
	while ( Chars[ *word ] == LETTER ) ++word;
	*(word++) = '\0';
	GetDelims( word );

	return string;
}


struct Node {
	char* name;
	double weight;
	Node *_true,
		 *_false;

	Node() : name(NULL), weight(0), _true(NULL), _false(NULL) {}
	~Node() {
		if ( _true != NULL ) delete _true;
		if ( _false != NULL ) delete _false;
	}
};

void Build ( char*& current, Node*& root ) {
	if ( *current == '(' ) {
		++current;
		GetDelims( current );
		root = new Node();
		root->weight = GetFloat( current );
		if ( Chars[ *current ] == LETTER ) {
			root->name = GetString( current );
			Build( current, root->_true );
			Build( current, root->_false );
		}
		GetDelims( current );
		if ( *current == ')' ) {
			++current;
			GetDelims( current );
		}
		else 
			throw ErrMsg( "unmatched parenthesis" );
	}
	else 
		throw ErrMsg ( "unmatched parenthesis in Build" );
}

double Calc ( Node* root, char* property_list[ 100 ], int size ) {
	if ( root->_false == NULL && root->_true == NULL ) return root->weight;

	for ( int i = 0; i < size; ++i ) {
		if ( strcmp( root->name, property_list[ i ]) == 0 ) {
			return root->weight * Calc( root->_true, property_list, size );
		}
	}
	return root->weight * Calc( root->_false, property_list, size );
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
			/* trees */
			int lines = GetNumber( current );

			Node* root = NULL;
			Build( current, root );

			printf( "Case #%d:\n", ++now );

			/* animals */
			lines = GetNumber( current );
			for ( int j = 0; j < lines; ++j ) {
				char* animal = GetString( current );
				char* property_name[ 100 ];
				int size = GetNumber( current );
				for ( int i = 0 ; i < size; ++i ) {
					property_name[ i ] = GetString( current );
				}
				double result = Calc( root, property_name, size );

				printf( "%1.7f\n", result );
			}
		}
	}
	catch ( ErrMsg err ) {
		printf( "ERROR : %s\n", err.msg );
	}

	if ( content != NULL )	delete [] content;
}