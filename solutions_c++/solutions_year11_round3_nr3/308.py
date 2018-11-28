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

unsigned __int64 gcd( unsigned __int64 a, unsigned __int64 b )
{
    unsigned __int64 t;
    if( a < b ){
        t = a; a = b; b = t;
    }
    while( b != 0 ){
        t = a % b;
        a = b;
        b = t;
    }
    return a;
}

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
		int N,L,H;
		fin >> N;
		fin >> L;
		fin >> H;
		vector<unsigned __int64> f(N);
		REP(i,N)
			fin >> f[i];

		sort(f.begin(), f.end());
////////////////////////////////
		int ret;
		for( ret = L; ret <= H; ret++ ){
			REP(i,N){
				if( f[i] < ret ){
					if( ret % f[i] !=  0 )
						break;
				}else{
					if( f[i] % ret != 0 )
						break;
				}
			}
			if( i >= N )
				break;
		}

	/////////////////////////////
		if( ret > H ){
			fprintf(fout,"Case #%d: NO\n", test_case);
		}else{
			fprintf(fout,"Case #%d: %d\n", test_case, ret);
			if( fin.eof() ){
				if( test_case != CASE ){
					OUTPUTLOG( "in-file error:eof" );
				}
				break;
			}
		}
	}

	OUTPUTLOG( "program end" );
}