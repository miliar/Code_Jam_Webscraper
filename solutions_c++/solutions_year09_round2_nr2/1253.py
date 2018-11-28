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
		string fig;
		string::iterator start;
		string::iterator next;
		string low_num;
		string org;
		fin >> fig;
		org = fig;
		int digit = fig.length();
		string cand;
		char tmp;
		int pos = digit-1;
		int s;
		if( digit == 1 ){
			fig.resize(2);
			fig[1] = '0';
			cand = fig;
			goto finish;
		}
		bool bSame = true;
		for( int i = 1; i < digit; i++ ){
			if( fig[0] != fig[i] )
				bSame =false;
		}
		if(bSame){
			cand.resize( fig.size()+1 );
			next = cand.begin();
			next++;
			copy(fig.begin(),fig.end(),next);
			cand[0] = cand[1];
			cand[1] = '0';
			goto finish;
		}

	//////
		bool hasLow = false;
		low_num.clear();
		for( pos = digit-1; pos >= 0; pos-- ){
			for( s = pos-1; s >= 0; s-- ){
				cand = fig;
				tmp = cand[s];
				cand[s] = cand[pos];
				cand[pos] = tmp;
				if( strcmp(org.c_str(), cand.c_str()) < 0 ){
					start = cand.begin();
					start += s+1;
					sort(start, cand.end());
					if( low_num.empty() || strcmp( cand.c_str(), low_num.c_str() ) < 0 ){
						low_num = cand;
					}
					hasLow = true;
				}
			}
		}
		if( hasLow == false ){
	/////
			cand.resize( cand.size()+1 );
			next = cand.begin();
			next++;
			copy(fig.begin(),fig.end(),next);
			cand[0] = '0';
			char low = 'a';
			int low_pos;
			for( pos = 1; pos <= digit; pos++ ){
				if( cand[pos] < low && cand[pos] != '0' ){
					low = cand[pos];
					low_pos = pos;
				}
			}
			cand[0] = cand[low_pos];
			cand[low_pos] = '0';
			start = cand.begin();
			start++;
			sort(start, cand.end());
		}else{
			cand = low_num;
		}
out:
finish:

	/////////////////////////////
		fprintf(fout,"Case #%d: %s\n", test_case, cand.c_str());
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}
