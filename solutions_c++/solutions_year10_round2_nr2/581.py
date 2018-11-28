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
		int N,K,B,T;
		fin >> N;
		fin >> K;
		fin >> B;
		fin >> T;
		vector<int> X(N);
		vector<int> V(N);
		REP(i,N)
			fin >> X[i];
		REP(i,N)
			fin >> V[i];

		vector<int> p(N);
		int ok = 0;
		REP(i,N){
			if( ((double)(B-X[i]) / (double)V[i]) <= (double)T ){
				p[i] = 1;
				ok++;
			}else{
				p[i] = 0;
			}
		}
		bool impossible = false;
		if( ok < K ){
			impossible = true;
			goto end;
		}

		int result = 0;
		int check = N-1;
		for( i = 0; i < K; i++ ){
			for( j = check; j >=0; j-- ){
				if( p[j] == 1 )
					break;
			}
			int cnt = 0;
			for( k = j+1; k < N; k++ ){
				if( p[k] == 0 )
					cnt++;
			}
			result += cnt;
			check = j-1;
		}

	/////////////////////////////
end:
		if( impossible )
			fprintf(fout,"Case #%d: IMPOSSIBLE\n", test_case );
		else
			fprintf(fout,"Case #%d: %d\n", test_case, result);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}