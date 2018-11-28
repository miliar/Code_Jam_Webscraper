//============================================================================
// Name        : Speaking.cpp
// Author      : Shahab
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int main() {
	// cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	map <char, char> mapping;

	string inp [] = {
			"ejp mysljylc kd kxveddknmc re jsicpdrysi",
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
			"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};

	string out [] = {
			"our language is impossible to understand",
			"there are twenty six factorial possibilities",
			"so it is okay if you want to just give up"
	};

	for ( int i = 0; i < 3; i++ ) {
		for ( int j = 0; j < inp [i].size(); j++ ) {
			mapping [inp [i] [j]] = out [i] [j];
		}
	}


	// data test code
	/*
	for ( int i = 0; i < 26; i++ ) {
		printf ("%c : ", 'a' + i);
		if ( mapping ['a' + i] ) {
			printf ("%c\n", mapping ['a' + i]);
		} else {
			printf ("---\n");
		}
	}*/

	mapping ['q'] = 'z';
	mapping ['z'] = 'q';

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int testCase; scanf ("%d", &testCase); getchar ();
	int cases = 0;

	while ( testCase-- ) {
		char input [100 + 10];
		gets (input);
		int len = strlen (input);
		printf ("Case #%d: ", ++cases);

		for ( int i = 0; i < len; i++ ) {
			if ( input [i] >= 'a' && input [i] <= 'z' ) printf ("%c", mapping [input [i]]);
			else printf ("%c", input [i]);
		}

		printf ("\n");
	}

	return 0;
}
