

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define EX( msg )		do { printf( "%s\n", msg ); result = -1; goto _end; }while(0)
#define LINELEN			0x1000


bool IsWordInPossibleCase( char *dicword, char *misinterpreted, int L );


int main( int argc, char **argv )
{
	FILE *fp = NULL;
	FILE *output = NULL;

	int result = 0;
	char *line = NULL;			// buffer to read each line

	char **dic = NULL;

	int L;						// length of words
	int D;						// words count
	int N;						// question cases

	int i, j;

	int count;

	if( argc != 2 )
		EX( "need argument : inputfile" );

	fp = fopen( argv[1], "rt" );
	if( fp == NULL )
		EX( "file not found" );

	output = fopen( "output.txt", "wt" );
	if( output == NULL )
		EX( "file write error" );

	line = (char*)malloc( LINELEN );				// "(ab)b(bc)" length not specified
	if( line == NULL )
		EX( "malloc" );

	// read L, D, N
	// is input trustable?
	if( fscanf( fp, "%d %d %d\n", &L, &D, &N ) != 3 )
		EX( "error in input file" );

	// alloc dic
	dic = (char**)malloc( D * sizeof(char*) );
	if( dic == NULL )
		EX( "malloc" );

	memset( dic, 0, D * sizeof(char*) );

	// alloc dic -> second ptr
	dic[0] = (char*)malloc( ( L + 1 ) * ( D + 1 ) );
	if( dic[0] == NULL )
		EX( "malloc" );

	memset( dic[0], 0, ( L + 1 ) * ( D + 1 ) );

	for( i = 1; i < D; i ++ )
	{
		dic[i] = dic[0] + ( ( L + 1 ) * i );
	}

//	for( i = 0; i < D; i ++ )
//	{
//		dic[i] = (char*)malloc( L + 1 );
//		if( dic[i] == NULL )
//			EX( "malloc" );
//	}

	// read dictionary
	for( i = 0; i < D; i ++ )
	{
		if( fscanf( fp, "%s\n", line ) == NULL )
			EX( "error in input file" );

		strncpy( dic[i], line, L );

	}



	// now count each cases.
	for( i = 0; i < N; i ++ )
	{
		if( fscanf( fp, "%s\n", line ) == (int)-1 )
			EX( "error in input file" );


		count = 0;
		for( j = 0; j < D; j ++ )
		{
			if( IsWordInPossibleCase( dic[j], line, L ) == true )
				count ++;
		}

		// output
		printf( "Case #%d: %d\n", i + 1, count );
		fprintf( output, "Case #%d: %d\n", i + 1, count );

	}


_end:

	if( dic != NULL )
	{
		free( dic[0] );

		free( dic );
	}

	if( fp != NULL )
		fclose( fp );

	if( output != NULL )
		fclose( output );

	if( line != NULL )
		free( line );

	return result;

}







bool IsWordInPossibleCase( char *dicword, char *misinterpreted, int L )
{
	bool result = true;
	int indexdicword;
	int indexmisint;
	bool found;
	int lengthmisint;


	char *inpar = NULL;				// string inside parenthesis "(abc)"b...

	lengthmisint = strlen( misinterpreted ); 

	inpar = (char*)malloc( lengthmisint );		// can't be longer than this
	if( inpar == NULL )
		EX( "malloc" );


	for( indexdicword = 0, indexmisint = 0; indexdicword < L && indexmisint <= lengthmisint; indexdicword ++, indexmisint ++ )
	{
		// misinterpreted[indexdicword] has parenthesis
		if( misinterpreted[indexmisint] == '(' )
		{
			// check if "(abc)" has "a"
			found = false;
			for( indexmisint ++; misinterpreted[indexmisint] != ')'; indexmisint ++ )
			{
				if( misinterpreted[indexmisint] == dicword[indexdicword] )
				{
					found = true;
					break;
				}
			}
			// not found
			if( found == false )
			{
				result = false;
				goto _end;
			}

			// let indexmisint point after ')'
			while( misinterpreted[indexmisint] != ')' &&
				   indexmisint < lengthmisint )
				   indexmisint ++;
//			if( misinterpreted[indexmisint] == ')' )
//				indexmisint ++;


		}

		// misinterpreted[indexdicword] doesn't have parenthesis
		else
		{
			if( dicword[indexdicword] != misinterpreted[indexmisint] )
			{
				result = false;
				goto _end;
			}
		}
	}


_end:

	return result;

}




