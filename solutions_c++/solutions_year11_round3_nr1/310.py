#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <windows.h>

using namespace std;
#pragma warning(disable: 4996)

#define OUTPUTLOG2(X,Y)\
{\
	char msg[1024];\
	sprintf( msg, X, Y );\
	OutputDebugString(msg);\
}
#define OUTPUTLOG OutputDebugString

#define FOR(r,a,b) for(r=(a); r<(b); r++)
#define REP(r,b) for(r=0; r<(b); r++)
#define TRV(type,cnt,it) for(type::iterator it=(cnt).begin(); it!=(cnt).end(); it++)

void main(int argc, char*argv[]) // usage: main.exe in.txt out.txt
{
	int i,j,k,l,m,n;

	ifstream fin(argv[1]);
	if( fin == NULL ){
		OUTPUTLOG2("cannot open in-file : %s\n", argv[1]);
		return;
	}
	FILE* fout = fopen(argv[2],"w");
	if( fin == NULL ){
		OUTPUTLOG2("cannot open out-file : %s\n", argv[2]);
		return;
	}

/////////////////////////////
	char line[1024];
	int CASE;
	fin >> CASE;
	for( int test_case = 1; test_case <= CASE; test_case++ ){
	/////////////////////////////
		int R,C;
		fin >> R;
		fin >> C;
		vector<string> b(R);
		REP(i, R)
			fin >> b[i];

		int x,y;
		REP( y, R ){
			REP( x, C ){
				if( b[y][x] == '#' ){
					if( y == R-1 || x == C-1 )
						goto IMPOSSIBLE;
					if( b[y][x+1] == '#' && b[y+1][x] == '#' && b[y+1][x+1] == '#' ){
						b[y][x] = '/';
						b[y][x+1] = '\\';
						b[y+1][x] = '\\';
						b[y+1][x+1] = '/';
					}else
						goto IMPOSSIBLE;

				}
			}
		}

	/////////////////////////////
		fprintf(fout,"Case #%d:\n", test_case);
		REP(i,R)
			fprintf(fout,"%s\n", b[i].c_str());
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
		continue;

IMPOSSIBLE:
		fprintf(fout,"Case #%d:\n Impossible\n", test_case);
	}

	OUTPUTLOG( "program end" );
}