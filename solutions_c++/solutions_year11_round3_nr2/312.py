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
		int L,N,C;
		unsigned __int64 t;
		fin >> L;
		fin >> t;
		fin >> N;
		fin >> C;
		vector<int> a(C);
		REP(i,C)
			fin >> a[i];
		vector<int> dis(N);
		j = 0;
		REP(i,N){
			dis[i] = a[j];
			j++;
			if( j >= C )
				j = 0;
		}
		/////////////////
		unsigned __int64 ret = 0, distance = 0;
		int star = 0;
		while( 1 ){
			unsigned __int64 d = dis[star];
			if( d*2 + ret > t ){
				d = dis[star] - (t-ret)/2;
				ret = t;
				dis[star] = d;
				break;
			}
			distance += dis[star];
			ret +=  dis[star]*2;
			star++;
			if( star >= N )
				goto finish;
		}
		if( star > 0 ){
			vector<int>::iterator s = dis.begin();
			vector<int>::iterator e = dis.begin();
			advance(e, star);
			dis.erase(s,e);
		}
		sort(dis.begin(), dis.end(), greater<int>());
		REP(i, dis.size()){
			if( L > 0 ){
				ret += dis[i];
			}else{
				ret += dis[i]*2;
			}
			L--;
		}

finish:
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