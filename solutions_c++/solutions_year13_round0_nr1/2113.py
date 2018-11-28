//#include "stdafx.h"

#include <iostream>

using namespace std;

char c[4][4] = {}, cX[4][4] = {}, cO[4][4] = {};
bool winX = false, winO = false, isFree = false, flag;

bool checkX(){

	for( int i = 0; i < 4; i++ ) {
		flag = true;
		for( int j = 0; j < 4; j++ ) {
			if( cX[i][j] != 'X' ) { flag = false; break; }
		}
		if( flag ) { winX = true; return true; }
	}
	

	
	for( int i = 0; i < 4; i++ ) {
		flag = true;
		for( int j = 0; j < 4; j++ ) {
			if( cX[j][i] != 'X' ) { flag = false; break; }
		}
		if( flag ) { winX = true; return true; }
	}
	

	flag = true;
	for( int i = 0; i < 4; i++ ) {
		if( cX[i][i] != 'X' ) { flag = false; break; }
	}
	if( flag ) { winX = true; return true; }

	flag = true;
	for( int i = 0; i < 4; i++ ) {
		if( cX[i][3-i] != 'X' ) { flag = false; break; }
	}
	if( flag ) { winX = true; return true; }

	return false;


}


bool checkO(){

	for( int i = 0; i < 4; i++ ) {
		flag = true;
		for( int j = 0; j < 4; j++ ) {
			if( cO[i][j] != 'O' ) { flag = false; break; }
		}
		if( flag ) { winO = true; return true; }
	}
	

	
	for( int i = 0; i < 4; i++ ) {
		flag = true;
		for( int j = 0; j < 4; j++ ) {
			if( cO[j][i] != 'O' ) { flag = false; break; }
		}
		if( flag ) { winO = true; return true; }
	}
	

	flag = true;
	for( int i = 0; i < 4; i++ ) {
		if( cO[i][i] != 'O' ) { flag = false; break; }
	}
	if( flag ) { winO = true; return true; }

	flag = true;
	for( int i = 0; i < 4; i++ ) {
		if( cO[i][3-i] != 'O' ) { flag = false; break; }
	}
	if( flag ) { winO = true; return true; }

	return false;

}


int main() {

	int t;
	
	cin >> t;
	for( int k = 0; k < t; k++ ) {
		
		winX = false; winO = false; isFree = false;
		
		for( int i = 0; i < 4; i++ ) {
			for( int j = 0; j < 4; j++ ) {
				cin >> c[i][j];
				if( c[i][j] == 'O' || c[i][j] == 'X' ) { cX[i][j] = c[i][j]; cO[i][j] = c[i][j]; }
				else if ( c[i][j] == '.' ) { isFree = true; cX[i][j] = c[i][j]; cO[i][j] = c[i][j]; }
				else if ( c[i][j] == 'T' ) { cX[i][j] = 'X'; cO[i][j] = 'O'; }
			}
		}
		
		if( !checkX() ) 
			checkO();

		if( winX ) cout << "Case #" << k+1 << ": X won" << endl;
		else if ( winO ) cout << "Case #" << k+1 << ": O won" << endl;
		else if ( isFree ) cout << "Case #" << k+1 << ": Game has not completed" << endl;
		else cout << "Case #" << k+1 << ": Draw" << endl;
	}
		


	return 0;
}
