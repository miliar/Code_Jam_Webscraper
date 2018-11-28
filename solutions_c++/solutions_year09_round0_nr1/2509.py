// Qualification1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "stdlib.h"
#include "string.h"
#include <new>

using std::bad_alloc;

#pragma warning(disable:4996)

enum { INVALID = 0, NUMBER = 1, LETTER = 2, DELIMS = 3 };
enum { UNACCESSED = 0, ACCESSED = 1 };
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
	Chars[ '(' ] = Chars[ ')' ] = LETTER;

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


inline char* GetString( char*& word ) {
	char* string = word;
	while ( Chars[ *word ] == LETTER ) ++word;
	*(word++) = '\0';
	GetDelims( word );

	return string;
}


class AlienWord {
public:
	AlienWord() : size ( 0 ), word(NULL) { }

	~AlienWord() { 
		try {	word != NULL ? delete [] word : void( 0 );	}
		catch( bad_alloc ) {
			throw ErrMsg( "failed to release allocated memory in destructor of AlienWord" );
		}
	}

	void AppendWord( char* str ) {
		size = strlen(str);
		try {
			word = new int[size];
			for ( size_t i = 0; i < size; ++i ) word[ i ] = 1 << ( str[i] - 'a' );
		}
		catch( bad_alloc ) {
			throw ErrMsg( "failed to init a class AlienWord" );
		}
	}

	void AppendPattern( char* str, int len ) {
		size = len;
		try {
			word = new int[size];
			for ( size_t i = 0; i < size; ++i ) {
				word[ i ] = 0;
				if ( *str == '(' ) {
					++str;
					while ( *str != ')' ) { word[ i ] += 1 << ( *str - 'a' ); ++str; }
					++str;
				}
				else {
					word[ i ] += 1 << ( *str++ - 'a' );
				}

			}
		}
		catch( bad_alloc ) {
			throw ErrMsg( "failed to init a class AlienWord" );
		}
	}

	bool Match ( const AlienWord& rhs ) {
		if ( rhs.size != size ) throw ErrMsg( "unmatched size of both matching AlienWord" );
		for ( size_t i = 0; i < size; ++i ) {
			if ( ( rhs.word[ i ] & word[ i ] ) == 0 ) 
				return false;
		}
		return true;
	}

	void Clean () {
		try {
			word != NULL ? delete [] word : void( 0 );
			size = 0;	word = NULL;
		}
		catch ( bad_alloc ) {
			throw ErrMsg( "failed to clean a AlienWord" );
		}
	}

private:
	size_t  size;
	int*    word;
};


void main( int argc, char* argv[] )
{
	char*		content = NULL;
	AlienWord*	dict	= NULL;
	try {
		char* current = content = Loading( argv[ 1 ] );
		Init();

		int	wordlen	 = GetNumber(current),
			dictsize = GetNumber(current),
			lines	 = GetNumber(current);
		
		try {
			dict = new AlienWord[dictsize];
		}
		catch ( bad_alloc ) {
			throw ErrMsg( "failed to allocate AlienWords Dictionary" );
		}

		int			i	   = 0;
		AlienWord	pattern;
		while ( i < dictsize ) { dict[ i ].AppendWord( GetString( current) ); ++i; }

		i = 0;
		while ( i < lines ) {
			int result = 0;
			pattern.AppendPattern( GetString( current ), wordlen );
			for ( int j = 0; j < dictsize; ++j ) 
				result += pattern.Match( dict[ j ] ) == true ? 1 : 0;
			pattern.Clean();
			printf( "Case #%d: %d\n", ++i, result );
		}
	}
	catch ( ErrMsg err ) {
		printf( "ERROR : %s\n", err.msg );
	}

	if ( content != NULL )	delete [] content;
	if ( dict != NULL )		delete [] dict;
}

