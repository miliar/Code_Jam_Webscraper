#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define OUT(t) cerr<<#t" = "<<t<<" ";
#define OLN()  cerr<<endl;

char map[100][100];
int N, M;

bool one( ) {
	int i, j;

	for( i=0 ; i<N ; i++ ) {
		for( j=0 ; j<M ; j++ ) {
			if( map[i][j] == '#' ) {
				if( i+1>=N || j+1>=M ) return false;
				if( map[i][j+1] != '#' ) return false;
				if( map[i+1][j] != '#' ) return false;
				if( map[i+1][j+1] != '#' ) return false;

				map[i][j] = '/';
				map[i][j+1] = '\\';
				map[i+1][j] = '\\';
				map[i+1][j+1] = '/';

				return true;
			}
		}
	}

	return true;
}

int main( ) {
	freopen( "D:\\GoogleCodeJam\\A\\A-small-attempt0.in", "r", stdin );
	freopen( "D:\\GoogleCodeJam\\A\\A-small-attempt0.out", "w", stdout );

	int re, ri = 1;
	int i, j;

	scanf( "%d", &re );
	while( re-- ) {
		scanf( "%d%d", &N, &M );
		int bCnt = 0;
		for( i=0 ; i<N ; i++ ) {
			scanf( "%s", &map[i] );
			for( j=0 ; j<M ; j++ ) {
				if( map[i][j] == '#' ) {
					bCnt++;
				}
			}
		}

		bool flag = true;

		if( bCnt % 4 != 0 ) {
			flag = false;
			goto _end;
		}

		while( bCnt > 0 ) {
			if( !one() ) {
				flag = false;
				break;
			}
			bCnt -= 4;
		}

_end:
		printf( "Case #%d:\n", ri++ );
		if( flag ) {
			for( i=0 ; i<N ; i++ ) {
				puts( map[i] );
			}
		} else {
			puts( "Impossible" );
		}

	}

	return 0;
}
