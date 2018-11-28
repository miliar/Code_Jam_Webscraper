#include <iostream>
#include <fstream>

using namespace std;
char b[5][5];

ifstream fin( "A-large.in" );
ofstream fout( "A2.out" );

#define cin fin
#define cout fout

int check(){
	bool dot = false;
	for( int i = 0; i < 4; i++ ){
		bool x = false, o = false, tie = false;
		for( int j = 0; j < 4; j++ ){
			if( b[i][j] == '.' )
				tie = true, dot = true;
			else if( b[i][j] == 'X' )
				x = true;
			else if( b[i][j] == 'O' )
				o = true;
		}
		if( !tie ){
			if( x && !o ){
				return 0;
			}
			if( o && !x )
				return 1;
		}
	}
	for( int i = 0; i < 4; i++ ){
		bool x = false, o = false, tie = false;
		for( int j = 0; j < 4; j++ ){
			if( b[j][i] == '.' )
				tie = true;
			else if( b[j][i] == 'X' )
				x = true;
			else if( b[j][i] == 'O' )
				o = true;
		}
		if( !tie ){
			if( x && !o ){
				return 0;
			}
			if( o && !x )
				return 1;
		}
	}
	{
		bool x = false, o = false, tie = false;
		for( int i = 0; i < 4; i++ ){
				if( b[i][i] == '.' )
					tie = true;
				else if( b[i][i] == 'X' )
					x = true;
				else if( b[i][i] == 'O' )
					o = true;
		}
		if( !tie ){
			if( x && !o )
				return 0;
			if( o && !x )
				return 1;
		}
	}

	{
		bool x = false, o = false, tie = false;
		for( int i = 0; i < 4; i++ ){
				if( b[i][3 - i] == '.' )
					tie = true;
				else if( b[i][3 - i] == 'X' )
					x = true;
				else if( b[i][3 - i] == 'O' )
					o = true;
		}
		if( !tie ){
			if( x && !o )
				return 0;
			if( o && !x )
				return 1;
		}
	}
	if( dot )
		return 2;
	return 3;
}

int test, T = 1;

int main()
{
	for( cin >> test; test--; ){
		for( int i = 0; i < 4; i++ )
			for( int j = 0; j < 4; j++ )
				cin >> b[i][j];
		int sg = check();
		if( sg == 0 )
			cout << "Case #" << T++ << ": X won" << endl;
		else if( sg == 1 )
			cout << "Case #" << T++ << ": O won" << endl;
		else if( sg == 2 )
			cout << "Case #" << T++ << ": Game has not completed" << endl;
		else cout << "Case #" << T++ << ": Draw" << endl;
	}
	return 0;
}