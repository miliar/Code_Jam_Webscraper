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

int l, p, C;

int main() {
	int casecount;

	ifstream in( "B-small-attempt0.in" );
	ofstream out( "out.txt" );

	in >> casecount;

	for( int c=1; c <= casecount; c++) {
		int result=0;
		in >> l >> p >> C;

		int taika = 0;
		int l2 = l;
		while( l2*C < p ) {
			l2*=C;
			taika++;
		}
		int foo = 0;
		while( foo < taika ) {
			result++;
			foo = foo*2 + 1;
		}

		out << "Case #" << c << ": " << result << "\n";
	}
}
