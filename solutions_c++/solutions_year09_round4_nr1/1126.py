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

#define rep(r,a,b) for(r=(a); r<(b); r++)
#define rep0(r,b) for(r=0; r<(b); r++)
#define trv(type,cnt,it) for(type::iterator it=(cnt).begin(); it!=(cnt).end(); it++)

void main(int argc, char*argv[])
{
	int i,j,k;

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
		string l;
		vector<int> op;
		op.resize(N+1);
		rep0(i,N){
			fin >> l;
			int pos = 0;
			for( j = N-1; j >= 0; j-- ){
				if( l[j] == '1' ){
					pos = j+1;
					break;
				}
			}
			op[i] = pos;
		}
		op[N] = 0x7fffffff;
		//////
		int swap = 0;
		int s = 0;
		int min;
		int tmp;

		// isOK
		bool bOK = true;
		rep(k,0,N){
			if( op[k] > k+1 )
				bOK = false;
		}
		if( bOK )
			goto end;

		while(1){
			s = 0;
			while(1){
				if( op[s] > s+1 ){ // NG
					for( i = s+1; i < N; i++ ){
						if( op[i] <= s+1 )
							break;
					}
					// swap
					for( j = i; j >= s+1; j-- ){
						//swap
						tmp = op[j-1];
						op[j-1] = op[j];
						op[j] = tmp;
						swap++;
					}
					break;
				}
				s++;
				if( s >= N ){
					goto end;
				}
			}
		}
end:

	/////////////////////////////
		fprintf(fout,"Case #%d: %d\n", test_case, swap);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}