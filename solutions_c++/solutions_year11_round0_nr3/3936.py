// Google_Code_Jam_2011_C_CandySplitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <list>

using namespace std;
const int charBufSize = 1024;

int patrickCalc( int x, int y ){
	return ( x ^ y );
}

list<int> mass;


bool compare_dec (int first, int second){
	if( first > second ) return true;
	return false;
}

bool readSingleCase( int index, ifstream& in, ofstream& out ){

	mass.clear();

	int number;
	in >> number;

	int sortedVal = 0 ;
	while( (number > 0) && in.good() ){
		in >> sortedVal;
		mass.push_front( sortedVal );
		--number;
	}

	mass.sort(compare_dec);

	int seanVal = 0;
	int patrickVal = 0;

	for( list<int>::iterator itr = mass.begin(); itr != mass.end() ; ++itr ){
	    patrickVal = patrickCalc( patrickVal, (*itr) );
		if( patrickVal == 0 ) continue;
		seanVal    = seanVal + (*itr);
	}

	if( patrickVal == 0 ){
		out << " Case #" << (index+1) << ": " << seanVal << endl;
	} else {
		out << " Case #" << (index+1) << ": NO" << endl;
	}


	return true;
}


bool readInputAndProceedAndWriteOutput( wchar_t* filename, wchar_t* outfilename ){
	ifstream in( filename );
	ofstream out( outfilename );
	
	if( in.is_open() ){

		char tmp[charBufSize];
		
		// Input
		//in.getline( tmp, charBufSize );
		
		// empty
		//in.getline( tmp, charBufSize );

		// Samples
		int sampleCount = 0;
		in >> sampleCount; 
		
		// out. 
		//out << "Output" << endl;
		//out << endl;

		// action
		int i = 0;

		while( ( i < sampleCount ) && !in.eof() ){
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
	wchar_t inputName[]  = L"c:\\googleCodeJam\\C\\smallinput\\C-small-attempt1.in";
	wchar_t outputName[] = L"c:\\googleCodeJam\\C\\smallinput\\smalloutput.txt";

	readInputAndProceedAndWriteOutput( inputName, outputName );
	
	return 0;
}

