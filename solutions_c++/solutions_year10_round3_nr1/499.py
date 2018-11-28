//============================================================================
// Name        : GCJ_10_R1C_A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int wcount;
int a[10000];
int b[10000];

int main() {
	int casecount;

	ifstream in( "A-large.in" );
	ofstream out( "out.txt" );

	in >> casecount;

	for( int c=1; c <= casecount; c++) {
		int result=0;
		in >> wcount;
		for( int i=0; i<wcount; i++ ) {
			in >> a[i];
			in >> b[i];
		}
		for( int i=0; i<wcount; i++ ) {
			for( int j=0; j<i; j++ ) {
				if( a[i] < a[j] && b[i] > b[j] ||
						a[i] > a[j] && b[i] < b[j] ) {
					result++;
				}

			}
		}
		out << "Case #" << c << ": " << result << "\n";
	}
}
