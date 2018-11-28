//============================================================================
// Name        : GCJ1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int MAXL = 16;
int wordl;

struct Pattern {
    bool match[ MAXL*256 ];
    int matches;
};

const int MAXPATTERNS = 500;
Pattern patterns[MAXPATTERNS];
int patternscount=0;

void initPatterns() {
    for( int i=0; i<MAXPATTERNS; i++ )
	for( int j=0; j<MAXL*256; j++ ) {
	    patterns[i].match[j] = false;
	    patterns[i].matches = 0;
	}
}

void addPattern( const std::string& s ) {
    int j=0;
    for( int i=0; i<wordl; i++ ) {
	unsigned char a = s[j++];
	if( a != '(' )
	    patterns[patternscount].match[256*i+a] = true;
	else while((a=s[j++]) != ')') {
	    patterns[patternscount].match[256*i+a] = true;
	}
    }
    patternscount++;
}

const int MAXWORDS=6000;
std::string Words[MAXWORDS];
int wordcount;

bool match( const Pattern& pattern, const std::string& word, bool watch ) {
    for( int i=0; i<wordl; i++ ){
	unsigned char c = word[i];
	//if( watch )
	//    cout << "!! " << i << " " << c << " " << (int)c << " " << (256*i+c) << "\n";
	if( !pattern.match[256*i+c] ) {
	    return false;
	}
    }
    return true;
}

int main() {
	std::ifstream ifs( "aa.in" );
	//if( !ifs.is_open() )
	//    cout << "!!!\n";
	ifs >> wordl;
	ifs >> wordcount;
	int patternscount;
	ifs >> patternscount;
	ifs >> ws;
	std::string line;

	//cout << wordl << " " << wordcount << " " << patternscount << "\n";

	for( int i=0; i<wordcount; i++ ) {
	    std::getline( ifs, Words[i] );
	}
	for( int i=0; i<patternscount; i++ ) {
	    std::getline( ifs, line );
	    addPattern(line);
	}

	for( int i=0; i<wordcount; i++ ) {
	    for( int j=0; j<patternscount; j++ ) {
		if( match( patterns[j], Words[i], j==5 && i == 21) )
		    patterns[j].matches++;
		//else
		//	if( j==5 && i == 21 )
		//	    cout << j << " " << Words[i] << "\n";
	    }
	}

	for( int i=0; i<patternscount; i++ )
	    cout << "Case #" << (i+1) << ": " <<patterns[i].matches << "\n";


	return 0;
}
