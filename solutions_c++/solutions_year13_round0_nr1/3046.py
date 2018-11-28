// ttt.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

string xwins() { return "X won"; }
string owins() { return "O won"; }
string draw() { return "Draw"; }
string incomplete() { return "Game has not completed"; }
bool CheckAllRows( vector<string>& table, char ch ) {
	for( int r = 0; r < 4; r++ ) {
		bool allmatch = true;
		for( int c = 0; c < 4; c++ ) {
			if( table[r][c] != ch && table[r][c] != 'T' ) allmatch = false;
		}
		if( allmatch ) return true;
	}
	return false;
}
bool CheckAllCols( vector<string>& table, char ch ) {
	for( int c = 0; c < 4; c++ ) {
		bool allmatch = true;
		for( int r = 0; r < 4; r++ ) {
			if( table[r][c] != ch && table[r][c] != 'T' ) allmatch = false;
		}
		if( allmatch ) return true;
	}
	return false;
}
bool CheckAllDiags( vector<string>& table, char c ) {
	bool allmatch = true;
	for( int d = 0; d < 4; d++ )
		if( table[d][d] != c && table[d][d] != 'T' ) allmatch = false;
	if( allmatch ) return true;
	allmatch = true;
	for( int d = 0; d < 4; d++ )
		if( table[3-d][d] != c && table[3-d][d] != 'T' ) allmatch = false;
	return allmatch;
}
bool HasMoves( vector<string>& table ) {
	for( int r = 0; r < 4; r++ ) 
		for( int c = 0; c < 4; c++ )
			if( table[r][c] == '.' ) return true;
	return false;
}
string GetTableState( vector<string> & table ) {
	if( CheckAllRows( table, 'X' ) ) return xwins();
	if( CheckAllRows( table, 'O' ) ) return owins();
	if( CheckAllCols( table, 'X' ) ) return xwins();
	if( CheckAllCols( table, 'O' ) ) return owins();
	if( CheckAllDiags( table, 'X' ) ) return xwins();
	if( CheckAllDiags( table, 'O' ) ) return owins();
	if( HasMoves( table ) ) return incomplete();
	return draw();
}
int _tmain(int argc, _TCHAR* argv[])
{
	string infilename = "../large.txt";
	string outfilename = "../outlarge.txt";
	ifstream data( infilename );
	ofstream outdata( outfilename );
	int T;
	data >> T;
	vector<string> table( 4, "" );
	for( int t = 1; t <= T; t++ ) {
		for( int r = 0; r < 4; r++ ) data >> table[r];
	//	for( int i = 0; i < 4; i++ ) cout << table[i] << endl;
		string result = GetTableState( table );
		//cout << result << endl;
		outdata << "Case #" << t << ": " << result << endl;
	}
	outdata.close();
	return 0;
}

