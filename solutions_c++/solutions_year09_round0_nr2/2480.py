//============================================================================
// Name        : GCJ2.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

const int MAXW = 100, MAXH=100;
int w, h;

const int pitch = 104;

int map[ 104*104 ];
int* ms = &map[208+1];

vector<int> sinks;

void findsinks() {
    sinks.clear();
    for( int i=0; i<w; i++ )
	for( int j=0; j<h; j++ ) {
	    int v = ms[i+j*pitch];
	    int lv = ms[i+j*pitch-1];
	    int rv = ms[i+j*pitch+1];
	    int uv = ms[i+j*pitch+pitch];
	    int dv = ms[i+j*pitch-pitch];

	    if( v <= lv && v <= rv && v <= uv && v <= dv )
		sinks.push_back( i+j*pitch );
	}
}

int stackp[11000];
int stackv[11000];
int stackpp[11000];
int stacktop=0;

int basinmap[104*104];
bool filled[104*104];


void fillBasin( int sink, int basin_number ) {
    stackp[0]=sink;
    stackv[0]=ms[sink]-1;
    stackpp[0]=sink;
    stacktop=0;
    while( stacktop >= 0) {
	int p = stackp[stacktop];
	int v = stackv[stacktop];
	int pp = stackpp[stacktop];
	stacktop--;

	bool conti = false;

	int lv = ms[p-1];
	int rv = ms[p+1];
	int uv = ms[p-pitch];
	int dv = ms[p+pitch];



	if( !filled[p] && v<ms[p] ) {
	    if( pp == p+pitch ) {
		if( v<lv && v<rv && v<uv )
		    conti=true;
	    } else if( pp == p+1 ) {
		if( v<lv && v<=dv && v<uv )
		    conti=true;
	    } else if( pp == p-1 ) {
		if( v<=rv && v<=dv && v<uv )
		    conti=true;
	    } else if( pp == p-pitch ) {
		if( v<=lv && v<=rv && v<=dv )
		    conti=true;
	    }
	    else if( pp==sink ) conti=true;
	    else throw;

	    if( !conti )
		continue;

	    basinmap[p] = basin_number;
	    filled[p] = true;
	    int thisv = ms[p];

	    stacktop++;
	    stackp[stacktop] = p-1;
	    stackv[stacktop] = thisv;
	    stackpp[stacktop] = p;
	    stacktop++;
	    stackp[stacktop] = p+1;
	    stackv[stacktop] = thisv;
	    stackpp[stacktop] = p;
	    stacktop++;
	    stackp[stacktop] = p-pitch;
	    stackv[stacktop] = thisv;
	    stackpp[stacktop] = p;
	    stacktop++;
	    stackp[stacktop] = p+pitch;
	    stackv[stacktop] = thisv;
	    stackpp[stacktop] = p;


	}
    }
}

int initmap[] = {
	1, 2, 3, 4, 5,
	2, 9, 3, 9, 6,
	3, 3, 0, 8, 7,
	4, 9, 8, 9, 8,
	5, 6, 7, 8, 9
};

char basinLetters[26];

void flushmap() {
    for( int i=0; i<104*104; i++ ) {
	map[i] = 200000;
	filled[i] = false;
    }
    sinks.clear();
}

int main() {

	ifstream ifs("b-small.in");
	int num_cases;
	ifs >> num_cases;

	for( int c=0; c<num_cases; c++ ) {
	    flushmap();
	    ifs >> h;
	    ifs >> w;


	    for( int j=0; j<h; j++ )
		for( int i=0; i<w; i++ )
		    ifs >> ms[i+j*pitch];

	    findsinks();
	    for( unsigned int i=0; i<sinks.size(); i++) {
		//cout << "sink: " << sinks[i] << "\n";
		fillBasin( sinks[i], i );
	    }

	    for( int i=0; i<26; i++ )
		basinLetters[i]='å';
	    char aa = 'a';
	    for( int j=0; j<h; j++ )
		for( int i=0; i<w; i++ ) {
		    int b = basinmap[i+j*pitch];
		    if( basinLetters[b] == 'å' )
			basinLetters[b] = aa++;
		}

	    cout << "Case #" << (c+1) << ": \n";

	    for( int i=0; i<h; i++ ) {
		for( int j=0; j<w; j++ )
		    cout << basinLetters[basinmap[j+i*pitch]] << " ";
		cout << "\n";
	    }
	}

}
