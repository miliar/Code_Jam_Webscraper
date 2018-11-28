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
		string num;
		fin >> num;

		string uniq = num;
		sort(uniq.begin(), uniq.end());
		string::iterator it = unique(uniq.begin(), uniq.end());
		int n = distance(uniq.begin(), it);

		vector<int> target;
		target.resize(num.size());
		int pos = 0;
		for( it = num.begin(); it != num.end(); it++ ){
			if( *it <= '9' ){
				target[pos] = *it-'0';
			}else{
				target[pos] = *it-'a' + 10;
			}
			pos++;
		}

		vector<int> index;
		index.resize(40);
		fill(index.begin(), index.end(), -1);

		vector<int>::iterator veci;
		int val = 0;
		for( veci = target.begin(); veci != target.end(); veci++ ){
			if( veci == target.begin() ){
				index[*veci] = 1;
			}else{
				if( index[*veci] == -1 ){
					index[*veci]= val;
					val++;
					if( val == 1 ) val++;
				}
			}
		}

		__int64 ret = 0;
		__int64 base = 1;
		if(n == 1){
			n = 2;
		}
		for( int i = target.size()-1; i >= 0; i-- ){
			ret += ((__int64)index[target[i]]) * base;
			base *= n;
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %I64d\n", test_case, ret);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}