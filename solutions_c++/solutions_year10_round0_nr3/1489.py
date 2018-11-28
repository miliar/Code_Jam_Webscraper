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
		int R, k, N;
		fin >> R;
		fin >> k;
		fin >> N;
		vector<int> g(N);
		for( int i = 0; i < N; i++ )
			fin >> g[i];

		vector<int> next(N);
		vector<int> person(N);

		for( int i = 0; i < N; i++ ){
			int p = 0;
			int pos = i;
			int gnum = 0;
			while(1){
				if( p+g[pos] > k || gnum >= N ){
					next[i] = pos;
					person[i] = p;
					break;
				}
				p += g[pos];
				pos++;
				if( pos >= N )
					pos = 0;
				gnum++;
			}
		}

		__int64 euros = 0;
		int pos = 0;
		for( int i = 0; i < R; i++ ){
			euros += person[pos];
			pos = next[pos];
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %I64d\n", test_case, euros);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}