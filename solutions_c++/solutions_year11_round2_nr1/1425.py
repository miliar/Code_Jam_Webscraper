#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define OUT(t) cerr<<#t" = "<<t<<" ";
#define OLN()  cerr<<endl;

char map[120][120];
int allCnt[120];
int winCnt[120];
int n;
double wp[120], owp[120], oowp[120];



int main( ) {
	freopen( "D:\\GoogleCodeJam\\A\\A-small-attempt0.in", "r", stdin );
	freopen( "D:\\GoogleCodeJam\\A\\A-small-attempt0.out", "w", stdout );

	int re, ri = 1;
	int i, j;

	scanf( "%d", &re );
	while( re-- ) {
		scanf( "%d", &n );
		for( i=0 ; i<n ; i++ ) {
			scanf( "%s", map[i] );
			allCnt[i] = winCnt[i] = 0;
			for( j=0 ; j<n ; j++ ) {
				if( map[i][j] != '.' ) {
					allCnt[i] ++;
				}
				if( map[i][j] == '1' ) {
					winCnt[i] ++;
				}
			}
			wp[i] = ( (double)winCnt[i] ) / allCnt[i];
		}

		for( j=0 ; j<n ; j++ ) {
			double sum = 0;
			int cnt = 0;
			for( i=0 ; i<n ; i++ ) {
				if( map[i][j] == '.' ) continue;

				int win = winCnt[i];
				int all = allCnt[i];
				if( map[i][j] == '0' ) {
					all--;
				} else if( map[i][j]=='1' ) {
					win--; all--;
				}

				if( all ) {
					sum += ((double)win)/all;
					// OUT( ((double)win)/all ); OLN();
				}
				cnt ++;
			}
			if( cnt ) sum /= cnt;
			owp[j] = sum;
			//OUT( owp[j] ); OLN();
		}

		for( j=0 ; j<n ; j++ ) {
			double sum = 0;
			int cnt = 0;
			for( i=0 ; i<n ; i++ ) {
				if( map[i][j] == '.' ) continue;

				sum += owp[i];
				cnt++;
			}
			if( cnt ) sum /= cnt;
			oowp[j] = sum;
			// OUT( oowp[j] ); OLN();
		}

		printf( "Case #%d:\n", ri++ );
		for( i=0 ; i<n ; i++ ) {
			printf( "%lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] );
		}
	}

	return 0;
}
