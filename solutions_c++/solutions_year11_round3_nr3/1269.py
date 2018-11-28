#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <boost/math/common_factor.hpp>
#include <algorithm>
#include <iterator>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream in;
	if ( argc >=1 )
		in.open(argv[1]);
	else
		in.open("B-small.in");

	if (!in) {
		cout << "file open failed" << endl;
		exit(1);
	}
	
	long problems = 0;

	in >> problems;

	int n;
	unsigned long long int l, h;
	unsigned long long int nn[10000];

	for ( long p = 1; p <= problems; p++ ) {
		in >> n;
		in >> l;
		in >> h;

		for ( int i = 0; i < n; i++ ) {
			in >> nn[i];
		}

		unsigned long long int f = 0;

		if ( l == 1 )
			f = 1;
		else {
			for ( unsigned long long int i = l; i <= h; i++ ) {
				char ok = 1;
				for ( int j = 0; j < n; j++ ) {
					unsigned long long int max = i > nn[j] ? i : nn[j];
					unsigned long long int min = i < nn[j] ? i : nn[j];
					unsigned long long int ch = max % min;
					//cout << i << " " << nn[j] << " " << ch << endl;
					if ( ch > 0 ) {
						ok = 0;
						break;
					}
				}
				if ( ok == 1 ) {
					f = i;
					break;
				}
			}
		}
		
		if ( f > 0 )
			cout << "Case #" << p << ": " << f << endl;
		else
			cout << "Case #" << p << ": NO" << endl;
	}
}
