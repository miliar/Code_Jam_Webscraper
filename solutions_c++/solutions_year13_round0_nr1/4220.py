#include <iostream>
#include <fstream>

using namespace std;

bool check_vertical( char[][4] , char );
bool check_horizontal( char[][4], char );
bool check_diagonal( char[][4], char );
bool check_empty( char[][4] );

int main()
{
	ifstream infl( "A-large.in" );
	ofstream outfl( "tic_tac_toe_large.txt" );

	int num_of_tests;
	char board [4][4];

	int case_num = 0;

	char player_X = 'X';
	char player_O = 'O';
	char input;

	infl >> num_of_tests;

	while( case_num < num_of_tests )
	{
		for( int row = 0; row < 4; row++ )
		{
			for( int col = 0; col < 4; col++ )
			{  
				infl >> input;
				board[row][col] = input;  
			}
		}

		case_num++;

		if( check_vertical( board, player_X ) || check_horizontal( board, player_X ) || check_diagonal( board, player_X ))
		{  outfl << "Case #" << case_num << ": X won" << endl;  }
		else if( check_vertical( board, player_O ) || check_horizontal( board, player_O ) || check_diagonal( board, player_O ))
		{  outfl << "Case #" << case_num << ": O won" << endl;  }
		else if( check_empty( board ))
		{  outfl << "Case #" << case_num << ": Game has not completed" << endl;  }
		else
		{  outfl << "Case #" << case_num << ": Draw" << endl;  }


		//for( int row = 0; row < 4; row++ )
		//{
		//	for( int col = 0; col < 4; col++ )
		//	{
		//		cout << board[row][col];
		//	}
		//	cout << endl;
		//}

	}
}



bool check_vertical( char board[][4], char player )
{
	bool four_in_a_row;

	for( int col = 0; col < 4; col++ )
	{
		four_in_a_row = true;

		for( int row = 0; row < 4; row++ )
		{  
			if(( board[row][col] != player ) && ( board[row][col] != 'T' ))
			{  four_in_a_row = false;  }				
		}

		if( four_in_a_row )
		{  return true;  }
	}

	return false;
}

bool check_horizontal( char board[][4], char player)
{
	bool four_in_a_row;

	for( int row = 0; row < 4; row++ )
	{
		four_in_a_row = true;

		for( int col = 0; col < 4; col++ )
		{  
			if(( board[row][col] != player ) && ( board[row][col] != 'T' ))
			{  four_in_a_row = false;  }				
		}

		if( four_in_a_row )
		{  return true;  }
	}

	return false;
}

bool check_diagonal( char board[][4], char player )
{
	bool four_in_a_row = true;

	for( int ndx = 0; ndx < 4; ndx++ )
	{
		if(( board[ndx][ndx] != player ) && ( board[ndx][ndx] != 'T' ))
		{  four_in_a_row = false;  }	
	}

	if( four_in_a_row )
	{  return true;  }

	four_in_a_row = true;

	for( int ndx = 0; ndx < 4; ndx++ )
	{
		if(( board[( 3-ndx )][ ndx ] != player ) && ( board[( 3-ndx )][ ndx ] != 'T' ))
		{  four_in_a_row = false;  }	
	}

	if( four_in_a_row )
	{  return true;  }

	return false;
}

bool check_empty( char board[][4] )
{
	for( int row = 0; row < 4; row++ )
	{
		for( int col = 0; col < 4; col++ )
		{  
			if( board[row][col] == '.' )
			{  return true;  }	
		}
	}

	return false;
}