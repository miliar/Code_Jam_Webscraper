// Google_Code_Jam_R1_2011_A_RPI.cpp : Defines the entry point for the console application.
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
int   table[100][103] = { 0 };
double result[100][4] = { 0 };

bool readSingleCase( int caseindex, ifstream& in, ofstream& out){
	
	int  teams = 0;
	in  >> teams;
	
	int  j = 0;
	char inchar[100]={0};
	
	for( int i = 0; i < teams; ++i ){
			double win    = 0;
			double lose   = 0;
			double nogame = 0;
		for( int j = 0 ; j < teams; ++j ){
			in >> inchar[j];
			switch( inchar[j] ){
			case '.':
				nogame++;
				table[i][j] = -1;
				break;
			case '1':
				win++;
				table[i][j] = 1;
				break;
			case '0':
				lose++;
				table[i][j] = 0;
				break;
			}
		}
		// WP
		result[i][0] = win / ( teams - nogame );
		
		table[i][100] = win;
		table[i][101] = lose;
		table[i][102] = nogame;
	}


	// OWP, OOWP
	for( int i = 0 ; i < teams; ++i ){
		double OWP = 0; 
		int op = 0;
		for( int j = 0; j < teams; ++j ){
			if( table[i][j] != -1 ){
				if( table[i][j] == 0 ){
					OWP += (double)( table[j][100] - 1 ) / (double) ( teams - table[j][102] - 1 );
				} else {
					OWP += (double) table[j][100] / (double) ( teams - table[j][102] - 1 );
				}
				op++;
			}
		}

		result[i][1] = OWP / op;
	}

	for( int i = 0 ; i < teams; ++i ){
		double OOWP = 0; 
		int op = 0;
		for( int j = 0; j < teams; ++j ){
			if( table[i][j] != -1 ){
				OOWP += result[j][1];
				op++;
			}
		}

		result[i][2] = OOWP / op;

		// RSI 
		result[i][3] = 0.25 * result[i][0] + 0.50 * result[i][1] + 0.25 * result[i][2];
	}


	// output
	out << "Case #" << caseindex << ":"<< endl;
	for( int i = 0; i < teams; ++i ){		
		out << result[i][3] << endl;
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

bool writeOutput( wchar_t* filename ){
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//wchar_t inputName[]  = L"c:\\googleCodeJam_R1\\A\\smallinput\\A-small-attempt0.in";
	//wchar_t outputName[] = L"c:\\googleCodeJam_R1\\A\\smallinput\\A-small-attempt0.out";

	wchar_t inputName[]  = L"c:\\googleCodeJam_R1\\A\\largeinput\\A-large.in";
	wchar_t outputName[] = L"c:\\googleCodeJam_R1\\A\\largeinput\\A-large.out";


	readInput( inputName, outputName );
	
	return 0;
}

