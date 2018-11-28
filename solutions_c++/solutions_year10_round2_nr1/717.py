// 2010_Q2_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <fstream>
#include <vector>

#include <iostream>



using namespace std;

char term = '/';

struct dir {
	string names;
	vector<dir> subs;

	int find( string s ) {
		string name = '#' + s + '$';
		size_t pos = names.find( name );
		if ( pos != string::npos ) {
			pos += name.length();
			return (int)( names[ pos ] - 1 );
		}
		else
			return -1;
	}

	dir& insert( string s ) {
		subs.push_back( dir() );
		if ( subs.size() > 255 ) {
			cout << "Warning : more than 128 subs" << endl;
			cin.get();
		}
		int end = subs.size() - 1;
		names += '#' + s + '$' + char( end + 1 );
		return subs[ end ];
	}

	void build ( string path, int* count = NULL ) {
		int start = 0;
		if( path[ 0 ] == term )
			start = 1;

		size_t pos = path.find( &term, start );

		string d, r;
		if ( pos == string::npos ) {
			if ( path.length() > 0 )
				d = path.substr( start, path.length());			// final part
			else
				return;
		}
		else {
			d = path.substr( 1, pos - 1 );
			r = path.substr( pos, path.length() - pos );
		}
		
		int i = find( d );

		if ( i >= 0 ) {
			subs[ i ].build( r, count );
		}
		else {
			insert( d ).build( r, count );
			if ( count != NULL )		// count operations;
				*count += 1;
		}
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	fstream in( "d:\\input.log", ios::in ),
		out( "d:\\output.log", ios::out );

	int cases;
	in >> cases;

	for ( int i = 0; i < cases; ++i ) {
		dir root;
		int n, m;
		in >> n >> m;

		/* build n path */
		for ( int j = 0; j < n; ++j ) {
			string path;
			in >> path;
			root.build( path );
		}

		/* build m path */
		int cmd = 0;
		for ( int j = 0; j < m; ++j ) {
			string path;
			in >> path;
			root.build( path, &cmd );
		}

		out << "Case #" << (i + 1) << ": " << cmd << endl;
	}

	return 0;
}

