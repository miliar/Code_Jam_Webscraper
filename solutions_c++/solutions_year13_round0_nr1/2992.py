#include <iostream>
#include <fstream>

using namespace std;

char J[4][4];

int Row ( int r, char ch ){

	int flg = 1;
	int i;

	for ( i = 0 ; i < 4 ; i++ ) 
		if ( ( J[r][i] == ch ) || ( J[r][i] == '.' ) ) flg = 0; 

	return flg;
} 

int Col ( int c , char ch ) {

	int flg = 1 ;
	int i;
	
	for ( i = 0 ; i < 4 ; i++ ) 
		if ( ( J[i][c] == ch ) || ( J[i][c] == '.') ) flg = 0;

	return flg;
}

int Dia ( char ch ) {

	int flg = 1;
	int i;

	for ( i = 0 ; i < 4 ; i++ ) 
		if ( ( J[i][i] == ch ) || ( J[i][i] == '.' ) ) flg = 0;

	if ( flg == 1 ) return flg;

	flg = 1;

	for ( i = 0 ; i < 4 ; i++ ) 
		if ( ( J[i][3-i] == ch ) || ( J[i][3-i] == '.') ) flg = 0;

	return flg;		
}

int Win ( char ch ) {

	int flg = 0 ;
	int i ;

	for ( i = 0 ; i < 4 && flg == 0 ; i++ ) { 
		flg = 1;
		flg=Row(i,ch);
	}

	for ( i = 0 ; i < 4 && flg == 0 ; i++ ) {

		flg = 1;
		flg=Col(i,ch);
	}

	if ( flg == 0 ) flg=Dia(ch);

	return flg;
}

int Full () {

	int i , j ;

	int flg = 1;

	for ( i = 0 ; i < 4 ; i++ ) 
		for ( j = 0 ; j < 4 ; j++ ) 
			if ( J[i][j] == '.' ) flg = 0;

	return flg;
}

void Readata(){

	ifstream fin("A.in");
	int T;
	fin >> T ;

	int i;
	for ( i = 1 ; i <= T ; i++ ) {

		int j , k ;
		for ( j = 0 ; j < 4 ; j++ ) 
			for ( k = 0 ; k < 4 ; k++ ) 
				fin >> J[j][k];

		int X = Win('O');
		if ( X == 1 )  {
			cout <<"Case #" << i << ": X won" << endl;
		}
		else {
			int O = Win('X');
			if ( O == 1 )  {
				cout <<"Case #" << i << ": O won" << endl; 
			}

		else {

			int F = Full();
			if ( F == 0 )  {
				cout <<"Case #" << i << ": Game has not completed" << endl;
			}

		else 
				cout <<"Case #" << i <<": Draw" << endl;
		}

		
		}
	}
}


int main()
{
	Readata();
	return 0;
}
