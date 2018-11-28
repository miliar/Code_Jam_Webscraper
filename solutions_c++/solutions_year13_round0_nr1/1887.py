#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <string>

char *checkGame( char map[4][4], const int mapSize ){
	for( int v = 0; v < mapSize; v++ ){
		for( int u = 0; u < mapSize; u++ ){
			printf("%c ", map[v][u] );
		}
		printf("\n");
	}
	bool xWin = false;
	bool oWin = false;
	bool draw = false;
	bool nCom = false;

	// check Hor Ver
	if( xWin == false && oWin == false ){
		for( int v = 0; v < mapSize; v++ ){
			int x = 0;
			int o = 0;
			for( int u = 0; u < mapSize; u++ ){
				if( map[u][v] == 'X' || map[u][v] == 'T' ) x++;
				if( map[u][v] == 'O' || map[u][v] == 'T' ) o++;
			}
			if( x == mapSize ) xWin = true;
			if( o == mapSize ) oWin = true;
		}
		for( int u = 0; u < mapSize; u++ ){
			int x = 0;
			int o = 0;
			for( int v = 0; v < mapSize; v++ ){
				if( map[u][v] == 'X' || map[u][v] == 'T' ) x++;
				if( map[u][v] == 'O' || map[u][v] == 'T' ) o++;
			}
			if( x == mapSize ) xWin = true;
			if( o == mapSize ) oWin = true;
		}
		{
			int x = 0;
			int o = 0;
			for( int i = 0; i < mapSize; i++ ){
				if( map[i][i] == 'X' || map[i][i] == 'T' ) x++;
				if( map[i][i] == 'O' || map[i][i] == 'T' ) o++;
			}
			if( x == mapSize ) xWin = true;
			if( o == mapSize ) oWin = true;
		}
		{
			int x = 0;
			int o = 0;
			for( int i = 0; i < mapSize; i++ ){
				if( map[mapSize-i-1][i] == 'X' || map[mapSize-i-1][i] == 'T' ) x++;
				if( map[mapSize-i-1][i] == 'O' || map[mapSize-i-1][i] == 'T' ) o++;
			}
			if( x == mapSize ) xWin = true;
			if( o == mapSize ) oWin = true;
		}
	}

	//draw
	if( xWin == false && oWin == false ){
		for( int v = 0; v < mapSize; v++ ){
			for( int u = 0; u < mapSize; u++ ){
				if( map[u][v] == '.' ) nCom = true;
			}
		}
	}
	char *ret = NULL;

	if( xWin == true) {
		ret = "X won";
	}
	else if( oWin == true ){
		ret = "O won";
	}
	else if( nCom == true ){
		ret = "Game has not completed";
	}
	else{
		ret = "Draw";
	}
	return ret;
}


int main( int argc, char *argv[] )
{
	char input[512];
#if 1
	strcpy( input, argv[1] );
#else if
	strcpy( input, "A-small-attempt1.in" );
#endif
	printf( "input = %s\n", input );
	FILE *fp = fopen( input, "r" );
	if( fp != NULL ){
		char buff[256] = {0};
		int dataNum = 0;

		fgets( buff, 256-1, fp );
		sscanf( buff, "%d", &dataNum );
		printf( "dataNum = %d\n", dataNum );

		char (*out)[256] = new char[dataNum][256];

		const int mapSize = 4;
		char map[mapSize][mapSize];
		for( int i = 0; i < dataNum; i++ ){
			printf( "data %d\n", i );
			int count = 0;
			while( fgets( buff, 256-1, fp ) ){
				if( strlen( buff ) > 1 ){
					for( int j = 0; j < mapSize; j++ ){
						map[count][j] = buff[j];
					}
					count++;
				}
				if( count == mapSize )
					break;
			}

			char *ret = checkGame( map, mapSize );
			sprintf( out[i], "Case #%d: %s", i+1, ret );
			printf( "%s\n", out[i] );
		}
		fclose(fp);

		fp = fopen( "TicTacToeTomek.out", "w" );
		for( int i = 0; i < dataNum; i++ ){
			fprintf( fp, "%s", out[i] );
			if( i < dataNum - 1 ) fprintf( fp, "\n" );
		}
		fclose(fp);
		delete []out;
	}
	return 0;
}