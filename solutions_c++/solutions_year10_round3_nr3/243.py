/*
	Author       :	Jan
	Problem Name :
	Algorithm    :
	Complexity   :
*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <sstream>

using namespace std;

int cases, caseno;
int A[33][33], m, n, K;
char a[1000];
char info[][5] =
{
"0000",
"0001",
"0010",
"0011",
"0100",
"0101",
"0110",
"0111",
"1000",
"1001",
"1010",
"1011",
"1100",
"1101",
"1110",
"1111"};

int value( int x ) {
	if( x <= '9' ) return x - '0';
	return x - 'A' + 10;
}

void fillA( int r, int x, int c ) {
	c = value(c);

	for( int i = 0; i < 4; i++ ) A[r][i+x] = info[c][i] - 48;
}

int cnt[33] = {0};

bool OK( int x1, int y1, int x2, int y2 ) {
	int i, j;
	for( i = x1; i <= x2; i++ ) {
		for( j = y1; j <= y2; j++ ) {
			if( A[i][j] == 2 ) return false;
		}
	}
	for( i = x1; i <= x2; i++ ) {
		for( j = y1; j < y2; j++ ) {
			if( A[i][j] + A[i][j+1] != 1 ) return false;
		}
	}
	for( i = x1; i < x2; i++ ) {
		for( j = y1; j <= y2; j++ ) {
			if( A[i][j] + A[i+1][j] != 1 ) return false;
		}
	}
	return true;
}

void fillA( int x1, int y1, int x2, int y2 ) {
	int i, j;
	for( i = x1; i <= x2; i++ ) {
		for( j = y1; j <= y2; j++ ) {
			A[i][j] = 2;
		}
	}
}

void printBoard() {
	int i, j;

	for( i = 0; i < m; i++ ) {
		for( j = 0; j < n; j++ ) 
			printf("%d", A[i][j]);
			puts("");
	}
}

int main() {
	freopen("c1.in", "r", stdin);
	freopen("c1.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i, j, k, l;
		scanf("%d %d", &m, &n);

		for( i = 0; i < m; i++ ) {
			scanf("%s", a);
			for( j = 0, k = 0; a[j]; j++, k += 4 ) {
				fillA( i, k, a[j] );
			}
		}
		memset( cnt, 0, sizeof(cnt) );
		for( K = min( m, n ); K >= 1; K-- ) { // 32
			bool found = false;
			for( i = 0; i + K <= m && !found; i++ ) {
				for( j = 0; j + K <= n; j++ ) {
					k = i + K - 1;
					l = j + K - 1;

					if( OK( i, j, k, l ) ) {
						cnt[K]++;
						fillA( i, j, k, l );
						found = true;
						break;
					}
				}
			}
			if( found ) K++;
		}
		printf("Case #%d: ", ++caseno);
		int res = 0;
		for( i = min( m, n ); i >= 1; i-- ) if( cnt[i] ) res++;
		printf("%d\n", res);
		for( i = min( m, n ); i >= 1; i-- ) if( cnt[i] ) printf("%d %d\n", i, cnt[i]);
	}
	return 0;
}
