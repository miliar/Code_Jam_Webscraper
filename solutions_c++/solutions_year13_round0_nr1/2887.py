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
		vector<string> b(4, string());
		fin >> b[0];
		fin >> b[1];
		fin >> b[2];
		fin >> b[3];

		bool OWin = false;
		bool XWin = false;
		bool empty = false;
		for( int y = 0; y < 4; y++ ){
			bool OLineX = true;
			bool XLineX = true;
			bool OLineY = true;
			bool XLineY = true;
			for( int x = 0; x < 4; x++ ){
				if( b[y][x] != 'O' &&  b[y][x] != 'T'  ){
					OLineX = false;
				}
				if( b[y][x] != 'X' &&  b[y][x] != 'T'  ){
					XLineX = false;
				}
				if( b[x][y] != 'O' &&  b[x][y] != 'T'  ){
					OLineY = false;
				}
				if( b[x][y] != 'X' &&  b[x][y] != 'T'  ){
					XLineY = false;
				}
				if( b[x][y] == '.' )
					empty = true;
			}
			OWin |= OLineX | OLineY;
			XWin |= XLineX | XLineY;
		}
		bool OLineX = true;
		bool XLineX = true;
		bool OLineY = true;
		bool XLineY = true;
		for( int i = 0; i < 4; i++ ){
			if( b[i][i] != 'O' &&  b[i][i] != 'T'  ){
				OLineX = false;
			}
			if( b[i][i] != 'X' &&  b[i][i] != 'T'  ){
				XLineX = false;
			}
			if( b[i][3-i] != 'O' &&  b[i][3-i] != 'T'  ){
				OLineY = false;
			}
			if( b[i][3-i] != 'X' &&  b[i][3-i] != 'T'  ){
				XLineY = false;
			}
		}
		OWin |= OLineX | OLineY;
		XWin |= XLineX | XLineY;


	/////////////////////////////
		string ret;
		if( OWin && XWin )
			ret = "Draw";
		else if( OWin )
			ret = "O won";
		else if( XWin )
			ret = "X won";
		else if(empty)
			ret = "Game has not completed";
		else
			ret = "Draw";

		fprintf(fout,"Case #%d: %s\n", test_case, ret.c_str());
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}