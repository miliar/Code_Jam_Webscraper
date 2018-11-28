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
	static char* result[] = {"OFF", "ON"};

	for( int test_case = 1; test_case <= CASE; test_case++ ){
	/////////////////////////////
		__int64 N,K,w;
		fin >> N;
		fin >> K;
		__int64 c = 0;
		__int64 n = 0;
		__int64 ret = 0;

		if( K&1 == 0 )
			goto end;

		bool light = false;
		w = K;
		while(1){
			if( w == c ){
				if( light )
					ret = 1;
				break;
			} 
			w -= c;
			if( w < c ){
				break;
			}
			if( n <= N )
				n++;
			if( n >= N ){
				light = true;
			}
			c = 1 << (n-1);
		}

end:
	/////////////////////////////
		fprintf(fout,"Case #%d: %s\n", test_case, result[ret]);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}