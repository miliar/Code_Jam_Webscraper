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

	char map[26];
	char use[26];
	string sample_in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
						   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
						   "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string sample_out[3] = {"our language is impossible to understand",
							"there are twenty six factorial possibilities",
							"so it is okay if you want to just give up"};
	memset( map, 0, sizeof(map) );
	memset( use, 0, sizeof(use) );
	for( int i = 0; i < 3; i++ ){
		for( int j = 0; j < sample_in[i].size(); j++ ){
			if( sample_in[i][j] != ' ' ){
				map[sample_in[i][j]-'a'] = sample_out[i][j];
				use[sample_out[i][j]-'a'] = 1;
			}
		}
	}
	//hint
	map['z'-'a'] = 'q';
	use['q'-'a'] = 1;

	i = 0;
	for( ;i < 26; i++ ){
		if(use[i] == 0)
			break;
	}
	map[16] = i + 'a';



/////////////////////////////
	char line[1024];
	int CASE;
	fin >> CASE;
	fin.getline(line,1024);
	for( int test_case = 1; test_case <= CASE; test_case++ ){
	////////////////////////////
		string in;
		fin.getline(line,1024);
		in = line;
		string out;
		out.resize(in.size());
		for( int i = 0; i < in.size(); i++ ){
			if( in[i] == ' ' ){
				out[i] = ' ';
			}else{
				out[i] = map[in[i]-'a'];
			}
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %s\n", test_case, out.c_str());
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}