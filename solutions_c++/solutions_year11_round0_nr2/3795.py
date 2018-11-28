// Google_Code_Jam_2011_B_Magicka.cpp : Defines the entry point for the console application.
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

struct replace{
	char av;
	char bv;
	char rv; //result
	replace(char a, char b, char r) : av(a), bv(b), rv(r) {};
	bool equal(char a, char b) { return ( av==a && bv==b ) || ( av==b && bv==a ) ; }
	bool in( char a, char& another ) { 
		if( av == a ){ 
			another = bv;
			return true;
		}
		if( bv == a ){
			another = av;
			return true;
		}
		return false; 
	} 
};

vector<replace> replaceTable;
vector<replace> oppositeTable;


bool merge(string& s){
	// assert s.size() >= 2 
	int pos = s.size() - 1;
	char a = s[pos];
	char b = s[pos-1];

	for( vector<replace>::iterator itr = replaceTable.begin(); 
		 itr != replaceTable.end(); ++itr ){

		if( (*itr).equal( a, b ) ){
			s.erase( pos-1, 2 );
			s.push_back( (*itr).rv );
			return true;
		}
	}
	return false;
}

bool clear(string& s){
	int pos = s.size() - 1;
	char a = s[pos];
	char b = ' ';
	string magic;

	for( vector<replace>::iterator itr = oppositeTable.begin(); 
		 itr != oppositeTable.end(); ++itr ){
		if( (*itr).in( a,  b ) ){
			magic.push_back( b );
		}
	}

	if( magic.size() == 0 ) return false;

	size_t found = s.find_first_of( magic );
	if( found != string::npos )
		s.clear();

	return true;
}

bool readSingleCase( int index, ifstream& in, ofstream& out ){
	
	replaceTable.clear();
	oppositeTable.clear();

	int  composeCount  = 0;
	char composeString[16]; 

	int oppositeCount = 0;
	char oppositeString[16];

	int elementCount  = 0;
	char elementString[128];

	in >> composeCount ;
	if( composeCount > 0 ){
		int i = composeCount; 
		while( i > 0 ){
			in >> composeString;
			replaceTable.push_back( replace( composeString[0], composeString[1], composeString[2] ) );
			--i;
		}
	}

	in >> oppositeCount ;
	if( oppositeCount > 0 ){
		int i = oppositeCount; 
		while( i > 0 ){
			in >> oppositeString;
			oppositeTable.push_back( replace( oppositeString[0], oppositeString[1], ' ' ) );
			--i;
	
		}
	}

	in >> elementCount;
	in >> elementString;


	//////////////////////////////////////////////////////////////////////
	// Process
	//////////////////////////////////////////////////////////////////////
	string outputString;
	for( int i = 0; i < elementCount; ++i ){
		outputString.push_back( elementString[i] );
		if( outputString.size() < 2 ) continue;

		merge( outputString );
		clear( outputString );
		
	}

	//////////////////////////////////////////////////////////////////////
	// Output
	//////////////////////////////////////////////////////////////////////
	out << " Case #" << (index+1) << ": [";
	if( outputString.size() >= 1 ){
		out << outputString.at(0);
	}

	for( size_t i = 1 ; i < outputString.size(); ++i ){
		out << ", " << outputString.at(i);
	}
    out << "]" << endl;

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
	wchar_t inputName[]  = L"c:\\googleCodeJam\\B\\smallinput\\B-large.in";
	wchar_t outputName[] = L"c:\\googleCodeJam\\B\\smallinput\\LargeOutput.txt";

	readInputAndProceedAndWriteOutput( inputName, outputName );
	return 0;
}

