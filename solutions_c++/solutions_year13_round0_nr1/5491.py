//============================================================================
// Name        : Tic-Tac-Toe-Tomek.cpp
// Author      : Anmol Ahuja
//============================================================================

#include <cstdio>
using namespace std;

char* check( char board[4][5] )
{
	int i,j, o, x, t, dot=0;

	for( i=0; i<4; ++i )
	{
		//check rows
		o=x=t=0;
		for(j=0;j<4;++j)
		{
			if( board[i][j] == 'O' )
				++o;
			else if( board[i][j] == 'X' )
				++x;
			else if( board[i][j] == 'T' )
				++t;
			else
				++dot;
		}
		if( o+t == 4  )
			return "O won";
		if( x+t == 4  )
			return "X won";
		//check columns
		o=x=t=0;
		for(j=0;j<4;++j)
		{
			if( board[j][i] == 'O' )
				++o;
			else if( board[j][i] == 'X' )
				++x;
			else if( board[j][i] == 'T' )
				++t;
		}
		if( o+t == 4  )
			return "O won";
		if( x+t == 4  )
			return "X won";
	}
	if( dot == 0 )
		return "Draw";
	//check diagonals
	o=x=t=0;
	for( i=0; i<4; ++i )
	{
		if( board[i][i] == 'O' )
				++o;
		else if( board[i][i] == 'X' )
				++x;
		else if( board[i][i] == 'T' )
				++t;
	}
	if( o+t == 4  )
		return "O won";
	if( x+t == 4  )
		return "X won";
	//other diagonal
	o=x=t=0;
	for( i=0; i<4; ++i )
	{
		if( board[i][3-i] == 'O' )
			++o;
		else if( board[i][3-i] == 'X' )
			++x;
		else if( board[i][3-i] == 'T' )
			++t;
	}
	if( o+t == 4  )
		return "O won";
	if( x+t == 4  )
		return "X won";
	return "Game has not completed";
}
int main() {
	int t,x;
	scanf("%d",&t);
	char board[4][5];
	int i;
	for( x=1; x<=t; ++x)
	{
		for( i=0; i<4; ++i )
			scanf("%s",board[i]);
		printf( "Case #%d: %s\n", x, check( board ) );
	}
	return 0;
}
