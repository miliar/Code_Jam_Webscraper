#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define OVAL  1
#define XVAL  2
#define TVAL  3
#define EMPTY 4

int board[4][4] ;
int empty =0;

int row()
{
	int i,j ;
	int k ;
	for ( i = 0 ; i < 4 ; i ++ ) {
		k=-1;
		for ( j =0 ; j < 4 ; j ++ )
		{
			if ( k == -1 ){
				k = board[i][j] ;
				continue;
			}
			if ( k == TVAL ){
				k = board[i][j] ;
				continue;
			}

			if ( board[i][j] != TVAL && board[i][j] != k ){
				break;
			}
		}
		if ( j == 4 )  {
		if ( k == OVAL || k == XVAL )
			return k;
		}
	}
	return -1;
}

int col()
{
	int i,j ;
	int k;
	for ( i = 0 ; i < 4 ; i ++ ) {
		k = -1;
		for ( j =0 ; j < 4 ; j ++ )
		{
			if ( k == -1 ){
				k = board[j][i] ;
				continue;
			}

			if ( k == TVAL ){
				k = board[i][j] ;
				continue;
			}

			if ( board[j][i] != TVAL && board[j][i] != k )
				break;
		}
		if ( j == 4 ) 
		if ( k == OVAL || k == XVAL )
			return k;
	}
	return -1;
}

int diagonal()
{
	int i;
	int k=-1;
	for ( i = 0 ; i < 4; i ++ )
	{
		if ( k == -1 ){
			k = board[i][i] ; 
			continue;
		}
		if ( k == TVAL ){
				k = board[i][i] ;
				continue;
			}


		if ( board[i][i] != TVAL &&board[i][i] != k )
			break;
	}
	if ( i == 4 ) {
		if ( k == OVAL || k == XVAL )
		 return k;
	}

	k = -1;
	for ( i = 3 ; i >= 0; i -- )
	{
		if ( k == -1 ){
			k = board[i][3-i] ; 
			continue;
		}
		if ( k == TVAL ){
				k = board[i][3-i] ;
				continue;
		}


		if ( board[i][3-i] != TVAL &&board[i][3-i] != k ) {
			break;
		}
	}
	if ( i < 0 )
		if ( k == OVAL || k == XVAL )
		return k;

	return -1;	
}

void fillboard(char *buffer, int row )
{
	int i;
	for ( i = 0 ;i < 4 ;i ++ )
	{
		switch(buffer[i])
		{
			case 'X' :
				board[row][i] = XVAL ;
				break;
			case 'O' :
				board[row][i] = OVAL ;
				break;			
			case '.' :
				board[row][i] = EMPTY ;
				++empty;
				break;

			case 'T' :
				board[row][i] = TVAL ;
				break;
		}
	}

}

void printwin(int i, int val)
{
	char buffer[256] ;
	sprintf(buffer, "Case #%d: ",i+1 ) ; 	
	switch( val )
	{
		case OVAL:
			strcat(buffer, "O won") ;
			break;
		case XVAL:
			strcat(buffer, "X won") ; 
			break;
		default:
			printf("%d error \n" , val ) ; 
	}

	printf("%s\n" , buffer ) ; 
}


int main()
{
	int cnt;
	scanf("%d\n" ,&cnt) ; 
	for ( int i = 0 ; i < cnt ; i ++ )
	{
		memset( board, 0, sizeof(board)) ; 	
		char buffer[16];	
		int r=0;
		empty = 0;
		for ( r = 0 ; r < 4 ; ++r )
		{
			scanf("%c%c%c%c\n" , &buffer[0], &buffer[1] , &buffer[2] , &buffer[3] ) ;
			buffer[4] = 0;
			fillboard(buffer, r ) ; 
		}	
		int win = row();	
		if ( win == XVAL || win == OVAL   ) {
			printwin(i,win ) ; 
			continue;
		}
		win = col() ;
		if ( win == XVAL || win == OVAL  )
		{
			printwin(i,win) ;
			continue;
		}
		win = diagonal() ;
		if ( win == XVAL || win == OVAL  )
		{
			printwin(i,win) ;
			continue;
		}

		if ( empty >= 1 )
		{
			printf("Case #%d: Game has not completed\n" , i+1 ) ; 
			continue;
		}


		printf("Case #%d: Draw\n", i+1 ) ; 	
	}

	return 0;
}

