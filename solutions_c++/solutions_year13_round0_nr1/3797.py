
#include <stdio.h>
#include <tchar.h>
#include <string.h>

const unsigned short winTable[] = {
		0xF000, 
		0x0F00,
		0x00F0,
		0x000F,
		0x8888,
		0x4444,
		0x2222,
		0x1111,
		0x8421,
		0x1248
};

const unsigned short winTableSize = 10;

void convert( char entry[17], unsigned short &resultX, unsigned short &resultO ) {
	resultX = resultO = 0;
	for ( int i = 0; i < 16; i++ ) {
		switch ( entry[ i] ) {
			case 'X' : {
				resultX |= 1 << ( 15 - i );
			} break;
			case 'O' : {
				resultO |= 1 << ( 15 - i );
			} break;
			case 'T' : {
				resultX |= 1 << ( 15 - i );
				resultO |= 1 << ( 15 - i );
			} break;
		};
	};
}

bool didWin ( unsigned short result ) {
	for ( int i = 0; i < winTableSize; i++ ) {
		if ( ( result & winTable[ i] ) == winTable[ i] ) {
			return true;
		}
	}
	return false;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int nTestCases = 0;
	scanf( "%u", &nTestCases );
	for ( int i = 0; i < nTestCases; i++ ) {
		char entry[ 17] = {0};
		for ( int j = 0; j < 4; j++ ) {
			scanf( "%s", entry + ( j * 4 ) );
		}
		unsigned short resultX;
		unsigned short resultO;

		convert( entry, resultX, resultO );

		bool wonX = didWin( resultX );
		bool wonO = didWin( resultO );

		if ( wonX || wonO ) {
			printf( "Case #%u: %c won\n", i+1, wonX?'X':'O' );
		} else {
			char *c = strchr( entry, '.' );
			if ( c == NULL ) {
				printf( "Case #%u: Draw\n", i+1 );
			} else {
				printf( "Case #%u: Game has not completed\n", i+1 );
			}
		}
	}

	return 0;
}

