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

#define UNLABLEED '*'
class ElevationMap  {
	struct Cell {
		int   altitude;
		char  lable;
		Cell* drain;
		Cell () : altitude( 0 ), lable( UNLABLEED ), drain( NULL ) {}
	};

public:
	ElevationMap();
	~ElevationMap();

	void InitMap	( char* & content, int rows, int lines );
	void BuildMap	();
	void Clean		();
	void PrintMap	();

private:
	inline void _DrainWater( int rowth, int lineth );
	inline void _SetLable  ( Cell* cell, char& lable );

private:
	int		row,
			line;
	Cell*	map;
};


void main( int argc, char* argv[] )
{
	char*		content = NULL;
	try {
		char* current = content = Loading( argv[ 1 ] );
		Init();

		int lines = GetNumber( current ),
			i	  = 0;
		ElevationMap Map;

		while ( i < lines ) {
			int rows  = GetNumber( current ),
				lines = GetNumber( current );
			Map.InitMap ( current, rows, lines );
			Map.BuildMap();
			printf( "Case #%d:\n", ++i );
			Map.PrintMap();
			Map.Clean();
		}
	}
	catch ( ErrMsg err ) {
		printf( "ERROR : %s\n", err.msg );
	}

	if ( content != NULL )	delete [] content;
}



ElevationMap::ElevationMap() : row( 0 ), line( 0 ), map(NULL) { }
ElevationMap::~ElevationMap() {
	try {	map != NULL ? delete [] map : void( 0 ); }
	catch ( bad_alloc ) {
		throw ErrMsg ( "failed to release map of ElevationMap in its destructor" );
	}
}


void ElevationMap::InitMap( char* & content, int rows, int lines ) {
	try {
		row = rows;  line = lines;
		map = new Cell[ row * line ];

		for ( int i = 0, size = row * line; i < size; ++i )
			(map + i)->altitude = GetNumber( content );
	}
	catch ( bad_alloc ) {
		throw ErrMsg ( "failed to allocate map of ElevationMap");
	}
}


void ElevationMap::BuildMap () {
	for ( int i = 0; i < row; ++i ) {
		for ( int j = 0; j < line; ++j ) {
			_DrainWater( i, j );
		}
	}

	char lable = 'a';
	for ( int i = 0, size = row * line; i < size; ++i )
		_SetLable( map + i, lable );
}

void ElevationMap::Clean() {
	try {
		map != NULL ? delete [] map : void( 0 );
		map = NULL;
		row = line = 0;
	}catch ( bad_alloc ) {
		throw ErrMsg ( "failed to Clean ElevationMap" );
	}
}


void ElevationMap::PrintMap() {
	for ( int i = 0; i < row; ++i ) {
		for ( int j = 0; j < line; ) {
			printf( "%c", (map + line * i + j)->lable );
			++j < line ? printf( " " ) : void( 0 );
		}
		printf( "\n" );
	}
}


void ElevationMap::_DrainWater( int rowth, int lineth ) {
	Cell	*cell			= map + line * rowth + lineth,
			*sink			= cell;
	int		lowest_altitude	= cell->altitude;

	if ( rowth  > 0			&& (cell - line)->altitude < sink->altitude ) {		// north
		sink = cell - line; 
	}
	if ( lineth > 0			&& (cell - 1)->altitude   < sink->altitude ) {		// west
		sink = cell - 1;
	}
	if ( lineth + 1 < line	&& (cell + 1)->altitude   < sink->altitude ) {		// east
		sink = cell + 1;
	}
	if ( rowth  + 1 < row	&& (cell + line)->altitude < sink->altitude ) {		// south
		sink = cell + line;
	}

	cell->drain = sink != cell ? sink : NULL;
}

void ElevationMap::_SetLable ( Cell* cell, char& lable ) {
	if ( cell->drain != NULL ) {
		Cell* sink = cell->drain;
		while ( sink->drain != NULL ) sink = sink->drain;
		sink->lable == UNLABLEED ? sink->lable = lable++ : void( 0 );
		cell->lable = sink->lable;
	}
	else 
		cell->lable == UNLABLEED ? cell->lable = lable++ : void( 0 );
}
