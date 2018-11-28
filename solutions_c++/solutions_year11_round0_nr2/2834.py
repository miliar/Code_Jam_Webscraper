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
		int C,D,N;
		vector< vector<char> > combine( 26, vector<char>(26, 0) );
		vector< vector<char> > oppose( 26, vector<char>(26, 0) );
		fin >> C;
		REP(i,C){
			char a,b,c;
			fin >> a;
			fin >> b;
			fin >> c;
			combine[a-'A'][b-'A'] = c;
			combine[b-'A'][a-'A'] = c;
		}
		fin >> D;
		REP( i,D ){
			char a,b;
			fin >> a;
			fin >> b;
			oppose[a-'A'][b-'A'] = 1;
			oppose[b-'A'][a-'A'] = 1;
		}
		fin >> N;
		string s;
		fin >> s;

		vector<char> result;
		int pos = -1;
		for( i = 0; i < N; i++ ){
			if( pos == -1 ){
				result.push_back(s[i]);
				pos++;
				continue;
			}
			// combine
			if( combine[result[pos]-'A'][s[i]-'A'] != 0 ){
				result[pos] = combine[result[pos]-'A'][s[i]-'A'];
			}else{
				// oppose
				for( j = 0; j <= pos; j++ ){
					if( oppose[result[j]-'A'][s[i]-'A'] == 1 ){
						result.clear();
						pos = -1;
						break;
					}
				}
				if( pos == -1 )
					continue;

				// add
				result.push_back(s[i]);
				pos++;
			}
		}


	/////////////////////////////
		if( result.size() == 0 ){
			fprintf(fout,"Case #%d: []\n", test_case);
		}else{
			fprintf(fout,"Case #%d: [", test_case);
			for( i = 0; i < result.size(); i++ ){
				if( i == result.size()-1 ){
					fprintf( fout, "%c]\n", result[i] );
				}else{
					fprintf( fout, "%c, ", result[i] );
				}
			}
		}
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}