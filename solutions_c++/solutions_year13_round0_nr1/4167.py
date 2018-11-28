// ProATic-Tac-Toe-Tomek.cpp -MysticBoy

#include <iostream>
#include <string>
//#include <cstdlib>
//#include <cstdio>

using namespace std;

int main(int cmdcount, char **cmdlist)
{
	int T; 			//number of test cases, T: 1 <= N <= 50 :: 1 ≤ T ≤ 1000. 
	//char Board[4][4]; 	//4 x 4 square board

	int long i, j, k, l, m;
	int cross = 0;
	


	// input
	cin >> T;
	char Board[T+1][4][4];
	string result[T+1];
	char blank;

	for(k = 1; k <= T; ++k) {
		for(i = 0; i < 4; ++i) {
			for(j = 0; j < 4; ++j) {
				cin >> Board[k][i][j];
			}
			//cin >> blank;
		}
		//cin >> blank;
	}

	/*/
	//print input
	cout << T << endl;
	for(k = 1; k <= T; ++k) {
		for(i = 0; i < 4; ++i) {
			for(j = 0; j < 4; ++j) {
				cout << Board[k][i][j];
			}
			cout << endl;
		}
		cout << endl;
	}
	/* */



	//*/
	int xwon = 0;	
	int owon = 0;
	int draw = 0;
	int inmiddle = 0;
	int valid = 1;
	int tvalue = 0;

	// processing
	for(k = 1; k <= T; ++k) {
		xwon = 0;	
		owon = 0;
		draw = 0;
		inmiddle = 0;
		valid = 1;
		tvalue = 0;

		//cout <<"T: " << k << endl;
		for(i = 0; i < 4 && valid; ++i) {		//Horizontal
			xwon = 0;
			owon = 0;
			tvalue = 0;	
			for(j = 0; j < 4 && valid; ++j) {
				
				if( Board[k][i][j] == 'X')	//"X won"
				{
					++xwon;
					
				}
				else if( Board[k][i][j] == 'O')	//"O won"
				{
					++owon;
					
				}
				else if( Board[k][i][j] == '.')	//"Game has not completed"
				{
					++inmiddle;
					
				}
				else if( Board[k][i][j] == 'T')	//
				{
					++tvalue;
					
				}
			}

			if( xwon == 4 || ( xwon == 3 && tvalue == 1 ) )
			{
				result[k] = "X won";
				valid = 0;	
			}
			else if( owon == 4 || (owon == 3 && tvalue == 1 ) )
			{
				result[k] = "O won";
				valid = 0;	
			}

		}

		if(valid) {
			for(i = 0; i < 4 && valid; ++i) {		//Vertical 
				xwon = 0;
				owon = 0;
				tvalue = 0;	
				for(j = 0; j < 4 && valid; ++j) {
				
					if( Board[k][j][i] == 'X')	//"X won"
					{
						++xwon;
					
					}
					else if( Board[k][j][i] == 'O')	//"O won"
					{
						++owon;
					
					}
					else if( Board[k][j][i] == '.')	//"Game has not completed"
					{
						++inmiddle;
					
					}
					else if( Board[k][j][i] == 'T')	//
					{
						++tvalue;
					
					}
				}

				if( xwon == 4 || ( xwon == 3 && tvalue == 1 ) )
				{
					result[k] = "X won";
					valid = 0;	
				}
				else if( owon == 4 || (owon == 3 && tvalue == 1 ) )
				{
					result[k] = "O won";
					valid = 0;	
				}
			}
		}


		if(valid)	//Diagonal cases TL->BR
		{
			xwon = 0;	
			owon = 0;
			tvalue = 0;

			for(i = 0; i < 4 && valid; ++i) {
				for(j = 0; j < 4 && valid; ++j) {
					if( i == j && Board[k][i][j] == 'X')	//"X won"
					{
						++xwon;
					
					}
					else if(  i == j && Board[k][i][j] == 'O')	//"O won"
					{
						++owon;
						
					}
					else if( i == j &&  Board[k][i][j] == 'T')
					{
						++tvalue;
					
					}
				}
			}
			if( xwon == 4 || ( xwon == 3 && tvalue == 1 ) )
			{
				result[k] = "X won";
				valid = 0;	
			}
			else if( owon == 4 || (owon == 3 && tvalue == 1 ) )
			{
				result[k] = "O won";
				valid = 0;	
			}
		}

		if(valid)	//Diagonal cases BL->TR
		{
			xwon = 0;	
			owon = 0;
			tvalue = 0;

			for(i = 0; i < 4 && valid; ++i) {
				for(j = 0; j < 4 && valid; ++j) {
					if((i + j == 3) && Board[k][j][i] == 'X')	//"X won"
					{
						++xwon;
					
					}
					else if((i + j == 3) && Board[k][j][i] == 'O')	//"O won"
					{
						++owon;
						
					}
					else if((i + j == 3) &&  Board[k][j][i] == 'T')
					{
						++tvalue;
					
					}
				}
			}
			if( xwon == 4 || ( xwon == 3 && tvalue == 1 ) )
			{
				result[k] = "X won";
				valid = 0;	
			}
			else if( owon == 4 || (owon == 3 && tvalue == 1 ) )
			{
				result[k] = "O won";
				valid = 0;	
			}
		}

		if(valid)	//Case: "Draw" or "Game has not completed"
		{
			if(inmiddle)
				result[k] = "Game has not completed";
			else	
				result[k] = "Draw";

			valid = 0;
		}


		/*
		if( xwon )
			result[k] = "		";
		else if( owon )
			result[k] = "		";
		else if( draw )
			result[k] = "		";
		else if( inmiddle )
			result[k] = "Game has not completed";	//string("Game has not completed");
		*/
	}

	//cout << "-------------------------" << endl;
	for(k = 1; k <= T; ++k) 
		cout <<"Case #"<< k <<": "<< result[k] << endl;
	/* */
	return 0;
}	//End main


