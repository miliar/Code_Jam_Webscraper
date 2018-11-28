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
		int N;
		fin >> N;
		vector<int> c(N);
		REP(i,N)
			fin >> c[i];
		
		int ans = -1;
		vector<int> s(N);
		for( i = 1; i < N; i++ ){
			fill( s.begin(), s.end(), 0 );
			for( j = N-1; j >= i; j-- ){
				s[j] = 1;
			}
			do{
				int a = 0, sa = 0;
				int b = 0, sb = 0;
				for( j = 0; j < N; j++ ){
					if( s[j] == 0 ){
						a ^= c[j];
						sa += c[j];
					}
					else{
						b ^= c[j];
						sb += c[j];
					}
				}
				if( a == b ){
					if( sa > ans )
						ans = sa;
					if( sb > ans )
						ans = sb;
				}
			}while(next_permutation(s.begin(), s.end()));
		}


	/////////////////////////////
		if( ans >= 0 )
			fprintf(fout,"Case #%d: %d\n", test_case, ans);
		else
			fprintf(fout,"Case #%d: NO\n", test_case);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}