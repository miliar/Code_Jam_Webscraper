#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream in;
	if ( argc >=1 )
		in.open(argv[1]);
	else
		in.open("A-small.in");

	if (!in) {
		cout << "file open failed" << endl;
		exit(1);
	}
	
	long problems = 0;

	in >> problems;

	int r, c;
	char col[100][100];

	for ( long p = 1; p <= problems; p++ ) {
		in >> r;
		in >> c;

		for ( int i = 0; i < r; i++ ) {
			in >> col[i];
		}

		char possible = 1;

		for ( int i = 0; i < r; i++ ) {
			for ( int j = 0; j < c; j++ ) {
				if ( col[i][j] == '#' ) {
					if ( 
						i + 1 < r &&
						j + 1 < c &&
						col[i+1][j] == '#' &&
						col[i][j+1] == '#' &&
						col[i+1][j+1] == '#'
					) {
						col[i][j] = '/';
						col[i+1][j] = '\\';
						col[i][j+1] = '\\';
						col[i+1][j+1] = '/';
						j++;
					} else {
						possible = 0;
						break;
					}
				}
			}
			if ( possible == 0 ) break;
		}
		
		cout << "Case #" << p << ":" << endl;
		if ( possible == 0 )
			cout << "Impossible" << endl;
		else {
			for ( int i = 0; i < r; i++ ) {
				cout << col[i] << endl;
			}
		}
	}
}
