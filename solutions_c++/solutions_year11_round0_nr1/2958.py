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
		int N;
		fin >> N;
		typedef struct {
			char R;
			int P;
		}C;
		vector<C> order;
		REP(i,N){
			C c;
			fin >> c.R;
			fin >> c.P;
			order.push_back(c);
		}
		int time = 0;
		int pos_O = 1, pos_B = 1;

		int work_time = 0;
		char cur_BOT, prev_BOT = ' ';
		for( i = 0; i < order.size(); i++ ){
			cur_BOT = order[i].R;
			if( cur_BOT == prev_BOT ){
				if( cur_BOT == 'O' ){
					work_time += abs(order[i].P - pos_O) + 1;
					pos_O = order[i].P;
				}else{
					work_time += abs(order[i].P - pos_B) + 1;
					pos_B = order[i].P;
				}
			}else{
				time += work_time;
				if( cur_BOT == 'O' ){
					work_time = abs(order[i].P - pos_O) - work_time;
					pos_O = order[i].P;
				}else{
					work_time = abs(order[i].P - pos_B) - work_time;
					pos_B = order[i].P;
				}
				if( work_time < 0 )
					work_time = 0;
				work_time += 1;
			}
			prev_BOT = cur_BOT;
		}
		time += work_time;

	/////////////////////////////
		fprintf(fout,"Case #%d: %d\n", test_case, time);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}