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
#include <assert.h>

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
		int N,W,H;
		fin >> N;
		fin >> W;
		fin >> H;
		vector<int> r(N);
		FOR( i, 0, N )
			fin >> r[i];
		vector<int> org(r.begin(), r.end());

		sort( r.begin(), r.end(), greater<int>() );
		vector<int> x(N);
		vector<int> y(N);
		int xx = 0, yy = 0;
		x[0] = xx;
		y[0] = yy;

		int left_r = r[0];
		xx += r[0];

		FOR( i, 1, N ){
			xx += r[i]+1;
			if( xx > W ){
				xx = 0;
				yy += left_r + r[i]+1;
				left_r = r[i];
				assert( yy < H );
			}
			x[i] = xx;
			y[i] = yy;
			xx += r[i];
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: ", test_case);
		FOR( i, 0, N ){
			FOR( j, 0, N ){
				if( org[i] == r[j] ){
					r[j] = -1;
					break;
				}
			}
			fprintf(fout,"%d %d ", x[j], y[j]);
		}
		fprintf(fout,"\n");
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}