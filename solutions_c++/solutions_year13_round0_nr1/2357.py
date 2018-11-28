#include <iostream>
#include <fstream>
using namespace std;

ifstream in("date.in");
ofstream out("date.out");

char El[5][5];
bool WinO, WinX, Dot;
int T, i, j;

int DX[8]={ 0, 0, 1, 1, 1,-1,-1,-1};
int DY[8]={ 1,-1, 0, 1,-1, 0, 1,-1};

bool valid( int x ){
	if( 1 <= x && x <= 4 )
		return true;
	return false;
}

bool win( char c ){
	int i, j, d, p, Nr;
	for( i=1; i<=4; ++i )
		for( j=1; j<=4; ++j )
			for( d=0; d<8; ++d ){
				Nr = 0;
 				p = 0;
				while( valid( i+DX[d]*p ) && valid( j+DY[d]*p ) ){
					if( El[ i+DX[d]*p ][ j+DY[d]*p ] == c || 
						El[ i+DX[d]*p ][ j+DY[d]*p ] == 'T' )
						Nr++;
					++p;
				}
				if( Nr == 4 )
					return true;
			}
	return false;
}

bool check_dot(){
	int i,j;
	for( i=1; i<=4; ++i )
		for( j=1; j<=4; ++j )
			if( El[i][j] == '.' )
				return true;
	return false;
}

int main(){
	in>>T;
	for( int t=1; t<=T; ++t ){
		WinO=WinX=Dot=0;
		for( i=1; i<=4; ++i )
			for( j=1; j<=4; ++j )
				in>>El[i][j];
		Dot = check_dot();
		WinO = win( 'O' );
		WinX = win( 'X' );
		if( WinO )
			out<<"Case #"<<t<<": O won\n";
		else if( WinX )
			out<<"Case #"<<t<<": X won\n";
		else if( Dot )
			out<<"Case #"<<t<<": Game has not completed\n";
		else 
			out<<"Case #"<<t<<": Draw\n";
	}
	return 0;
}
