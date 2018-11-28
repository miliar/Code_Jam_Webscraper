// Google_Code_Jam_R1C_2011_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <wchar.h>
#include <assert.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;
const int charBufSize = 1024;
char  picture[50][50] = {' '};

bool Replace( int row, int col, int blueCount ){
	
	int count = blueCount;
	
	if( count == 0 ) return true;

	if( ( count % 4) != 0 ) return false;

	for( int i = 0; i < (row-1); ++i ){
		for( int j = 0 ; j < (col-1); ){
			if( picture[i][j]    == '#' && 
				picture[i+1][j]  == '#' &&
				picture[i][j+1]  == '#' && 
				picture[i+1][j+1]== '#' ){
				count -= 4;
				picture[i][j] = picture[i+1][j+1] = '/';
				picture[i+1][j] = picture[i][j+1] = '\\';
				j = j+2;
			}else{
				++j;
			}
		}
	}

	return (count == 0) ? true : false;
}

bool IsReplaceable(){
	return true;
}

bool readSingleCase( int caseindex, ifstream& in, ofstream& out){
	
	// input
	int row, col = 0;
	in  >> row >> col ;
	int  blueCount = 0;
	char inChar;

	for( int i = 0; i < row; ++i ){
		for( int j = 0; j < col; ++j ){
			in >> inChar;
			picture[i][j] = inChar ;
			if( inChar == '#' ){
				blueCount++;
			}
		}
	}

	bool isReplacable = Replace( row, col, blueCount );

	// output
	out << "Case #" << caseindex << ":"<< endl;
	if( !isReplacable ){
		out << "Impossible" << endl;
	} else {
		
		for( int i = 0; i < row ; ++i ){
			for( int j = 0; j < col; ++j ){
				out << picture[i][j];
				if( j == (col - 1) ){
					out << endl;
				}
			}
		}
	}
	return true;
}

bool readInput( wchar_t* filename, wchar_t* outputName ){
	ifstream in ( filename );
	ofstream out( outputName);

	if( in.is_open() ){
		// Samples
		int sampleCount = 0;
		in >> sampleCount; 

		// 
		int i = 1;
		while( ( i <= sampleCount ) && !in.eof() ){
			readSingleCase( i, in, out );
			++i;
		}

		in.close();
		out.close();

		return true;
	}
	
	in.close();
	out.close();

	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//wchar_t inputName[]  = L"C:\\googleCodeJam_R1_C\\A\\A-test.in";
	//wchar_t outputName[] = L"c:\\googleCodeJam_R1_C\\A\\A-test.out";

	//wchar_t inputName[]  = L"C:\\googleCodeJam_R1_C\\A\\A-small-attempt0.in";
	//wchar_t outputName[] = L"c:\\googleCodeJam_R1_C\\A\\A-small-attempt0.out";

	wchar_t inputName[]  = L"C:\\googleCodeJam_R1_C\\A\\A-large.in";
	wchar_t outputName[] = L"C:\\googleCodeJam_R1_C\\A\\A-large.out";
	
	readInput( inputName, outputName );
	
	return 0;
}

