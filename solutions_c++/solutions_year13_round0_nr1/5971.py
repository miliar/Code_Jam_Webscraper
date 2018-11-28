// GooglCodeJamProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

const char* INPUT_FILE_NAME = "A-small-attempt1.in";

using namespace std;

const int MATRIX_SIZE = 4;
const int DIAGONAL_SIZE = 2;

const string STR_X_WON = "X won";
const string STR_O_WON = "O won";
const string STR_DRAW = "Draw";
const string STR_NOT_COMPLETED = "Game has not completed";

template <typename T>
T StringToNumber ( string &Text )
{
	istringstream ss(Text);
	T result;
	return ss >> result ? result : 0;
}

const string& TestLine( const const string& line , bool& bContinue ) 
{
	bContinue = false;
	if( 0 == line.compare( "OOOO" ) ) {
		return STR_O_WON;
	}
	if( 0 == line.compare( "XXXX" ) ) {
		return STR_X_WON;
	}
	//bool bHasT = false;
	//int nPosT = -1;
	//for( unsigned int i = 0 ; i < line.size() ; i++ ) {
	//	if( 'T' == line[i] ) {
	//		bHasT = true;
	//		nPosT = i;
	//		break;
	//	}
	//}
	//if( bHasT ) {
	//	bool bDotFound = false;
	//	for each( char c in line ) {
	//		if( '.' == c ) {
	//			bDotFound = true;
	//			break;
	//		}
	//	}
	//	if( !bDotFound ) {
	//		int nTestPos = (nPosT+1) % MATRIX_SIZE;
	//		if( line[nTestPos] == 'O' ) {
	//			return STR_O_WON;
	//		}
	//		else {
	//			return STR_X_WON;
	//		}
	//	}
	//}

	bContinue = true;
	return STR_NOT_COMPLETED;
}

const string& TestMatrix( vector<string>& matrix ) 
{
	vector<string> columns(MATRIX_SIZE);
	vector<string> diagonals(DIAGONAL_SIZE);
	for( vector<string>::iterator it = columns.begin() ; it != columns.end() ; ++it ) { 
		it->resize(MATRIX_SIZE); 
	}
	for( vector<string>::iterator it = diagonals.begin() ; it != diagonals.end() ; ++it ) { 
		it->resize(MATRIX_SIZE); 
	}

	// count O and X
	int nCountO = 0;
	int nCountX = 0;
	int nCountDot = 0;
	int nPosT_Col = -1;
	int nPosT_Low = -1;
	for ( unsigned int i = 0; i < matrix.size() ; i++ ) {
		const string& str = matrix[i];
		for( unsigned int j = 0; j < str.size() ; j++ ) {
			char c = str[j];
			switch( c ) {
			case 'O' :
				++nCountO;
				break;
			case 'X' :
				++nCountX;
				break;
			case 'T' :
				nPosT_Col = j;
				nPosT_Low = i;
				break;
			case '.' :
				++nCountDot;
				break;
			default:
				break;
			}
			columns[j][i] = c;
		}
	}
	if( nPosT_Col != -1 ) {
		if( nCountX == nCountO ) {
			matrix[nPosT_Low][nPosT_Col] = 'X';
		}
		else {
			matrix[nPosT_Low][nPosT_Col] = 'O';
		}
	}

	diagonals[0][0] = matrix[0][0];
	diagonals[0][1] = matrix[1][1];
	diagonals[0][2] = matrix[2][2];
	diagonals[0][3] = matrix[3][3];

	diagonals[1][0] = matrix[3][0];
	diagonals[1][1] = matrix[2][1];
	diagonals[1][2] = matrix[1][2];
	diagonals[1][3] = matrix[0][3];

	// check lows
	bool bContinue = false;
	for( unsigned int i = 0; i < matrix.size() ; i++ ) {
		const string& result = TestLine( matrix[i] , bContinue );
		if( !bContinue ) {
			cout << "Decide lows [" << i << "]" << endl;
			return result;
		}
	}
	// check columns
	if( bContinue ) {
		for( unsigned int i = 0; i < columns.size() ; i++ ) {
			const string& result = TestLine( columns[i] , bContinue );
			if( !bContinue ) {
				cout << "Decide columns [" << i << "]" << endl;
				return result;
			}
		}				
	}
	// check diagonals
	if( bContinue ) {
		for( unsigned int i = 0; i < diagonals.size() ; i++ ) {
			const string& result = TestLine( diagonals[i] , bContinue );
			if( !bContinue ) {
				cout << "Decide diagonals [" << i << "]" << endl;
				return result;
			}
		}				
	}

	if( bContinue ) {
		if( nCountDot == 0 ) {
			return STR_DRAW;
		}
	}

	return STR_NOT_COMPLETED;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs( INPUT_FILE_NAME );
	ofstream ofs( "out.txt" );

	string buf;

	// process each lines
	int nLineCount = 0;

	vector<string> lows(MATRIX_SIZE);
	for( vector<string>::iterator it = lows.begin() ; it != lows.end() ; ++it ) { 
		it->resize(MATRIX_SIZE); 
	}

	int nNumT;
	int nCountTest = 0;
	int nLowsCount = 0;
	while(ifs) {
		buf.clear();
		if( !getline(ifs, buf) ) {
			break;
		}
		++nLineCount;

		cout << "[" << nLineCount << "] " << buf << endl;

		if( buf.size() == 0 ) {
			continue;
		}
		// first line
		if( 1 == nLineCount ) {
			nNumT = StringToNumber<int>(buf);
			continue;
		}
		else {
			// each T
			if( buf.size() == 0 )  {
				continue;
			}

			lows[nLowsCount++] = buf;

			if( nLowsCount == MATRIX_SIZE ) {

				const string& result = TestMatrix( lows );

				nLowsCount = 0;
				cout << "Case #" << ++nCountTest << ": " << result << endl;
				ofs << "Case #" << nCountTest << ": " << result << endl;
			}
		}

	}

	cout << "fin" << endl;

	ifs.close();
	ofs.close();

	char in;
	cin.get(in);

	return 0;
}

