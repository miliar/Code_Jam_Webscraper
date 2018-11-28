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
#include <assert.h>

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
	//char line[1024];
	int CASE;
	fin >> CASE;
	for( int test_case = 1; test_case <= CASE; test_case++ ){
	/////////////////////////////
		int M,N;
		fin >> M;
		fin >> N;
		vector<vector<int>> board(M, vector<int>(N));
		REP(i,M){
			string line;
			fin >> line;
			REP(j,N/4){
				int val;
				if( line[j] <= '9' ){
					val = line[j] - '0';
				}else{
					val = line[j] - 'A' + 10;
				}
				REP(k,4){
					board[i][j*4+k] = ((val & (1 << (3-k))) != 0);
				}
			}
		}

		/////
		int ret_size = min(M,N);
		vector<int> result(ret_size+1, 0);
		int total = 0;
		while(1){
			int max_x, max_y, max_s = 0;
			int x, y;
			int parity;
			REP(y,M){
				REP(x, N){
					parity = board[y][x];
					if( parity == -1 )
						continue;
					int sq = 1;
					int nx = x+1;
					int ny = y+1;
					int nsq = 2;
					while( nx < N && ny < M ){
						int check;
						if( (nsq&1) == 0 )
							check = 1-parity;
						else
							check = parity;
						for( int px = x; px < x+nsq; px++ ){
							if( board[ny][px] != check )
								goto out;
							check = 1-check;
						}
						if( (nsq&1) == 0 )
							check = 1-parity;
						else
							check = parity;
						for( int py = y; py < y+nsq; py++ ){
							if( board[py][nx] != check )
								goto out;
							check = 1-check;
						}
						sq++;
						nsq++;
						nx++;
						ny++;
					}
out:
					if( max_s < sq ){
						max_s = sq;
						max_x = x;
						max_y = y;
					}
				}
			}

			/////
			assert(max_s>0);
			result[max_s]++;
			for( int y = max_y; y < max_y + max_s; y++ )
				for( int x = max_x; x < max_x + max_s; x++ )
					board[y][x] = -1;

			total += max_s*max_s;
			if( total >= M*N ){
				assert( total == M*N );
				break;
			}
		}

	/////////////////////////////
		int num = 0;
		REP(i, ret_size+1)
			if(	result[i] != 0 )
				num++;
		fprintf(fout,"Case #%d: %d\n", test_case, num);
		for( int i = ret_size; i >=0; i-- )
			if(	result[i] != 0 )
				fprintf(fout,"%d %d\n", i, result[i]);

		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}