// 2010_Q2_3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <string>
#include <fstream>

#include <iostream>

using namespace std;

int N[ 100 ], K[100];
int MinSpeed[ 100 ];

int _tmain(int argc, _TCHAR* argv[])
{
	fstream in( "d:\\input.log", ios::in ),
		out( "d:\\output.log", ios::out );

	int cases;
	in >> cases;

	for ( int i = 0; i < cases; ++i ) {
		int n, m, b, t;
		in >> n >> m >> b >> t;

		/* init */
		for ( int j = 0; j < n; ++j ) {
			in >> N[ j ];
			MinSpeed[ j ] = (b - N[ j ])/t;
			if ( (b - N[ j ])%t != 0 ) MinSpeed[ j ] += 1;
		}

		for ( int j = 0; j < n; ++j ) {
			in >> K[ j ];
		}

		unsigned long long op = 0;
		for ( int j = n - 1; j >= 0; --j ) {
			if ( K[ j ] >= MinSpeed[ j ] ) {
				m--;
				if( m == 0 ) 
					break;
			}
			else {
				op += m;
			}
		}

		if ( m > 0 ) {
			out << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			out << "Case #" << (i + 1) << ": " << op << endl;
		}
	}

	return 0;
}

