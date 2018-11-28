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

void main(int argc, char*argv[])
{
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
		int cell[10002];
		vector<int> release;
		int P,Q;
		fin >> P;
		fin >> Q;
		release.resize(Q);
		for( int i = 0; i < Q; i++ ){
			fin >> release[i];
		}

		int ret;
		int min_ret = 0x7fffffff;

		do{
			for( int i = 1; i <= P; i++ ){
				cell[i] = 1;
			}
			cell[0] = 0;
			cell[P+1] = 0;

			int ret = 0;
			for( int day = 1; day <= Q; day++ ){
				int cp = release[Q-day];
				cell[cp] = 0;
				int *p,*s;
				p = &cell[cp-1];
				s = &cell[cp+1];
				while(1){
					if( *p == 0 )
						break;
					p--;
				}
				while(1){
					if(*s == 0)
						break;
					s++;
				}
				ret += (s-&cell[cp]) - 1;
				ret += (&cell[cp]-p) - 1;
			}

			if( min_ret > ret ){
				min_ret = ret;
			}
		}while( next_permutation(release.begin(), release.end()) );

	/////////////////////////////
		fprintf(fout,"Case #%d: %d\n", test_case, min_ret);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
		printf("%d,%d\n",P,Q);
	}

	OUTPUTLOG( "program end" );
}