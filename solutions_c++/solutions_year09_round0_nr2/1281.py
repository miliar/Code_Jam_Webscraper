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

#define MM 105

int cases, caseno, m, n, A[MM][MM], N;

int move[4][2] = { -1, 0, 0, -1, 0, 1, 1, 0 };
int visited[MM][MM];

bool valid( int x, int y ) {
	return x >= 0 && x < m && y >= 0 && y < n;
}

int call( int i, int j ) {
	if( visited[i][j] != -1 ) return visited[i][j];

	int mn = 1000000, cnt = 0, k;
	for( k = 0; k < 4; k++ ) {
		int x, y;

		x = i + move[k][0];
		y = j + move[k][1];
		if( valid(x, y) ) mn = min( mn, A[x][y] );
	}
	if( mn >= A[i][j] ) {
		visited[i][j] = N++;
		return N - 1;
	}
	for( k = 0; k < 4; k++ ) {
		int x, y;

		x = i + move[k][0];
		y = j + move[k][1];
		if( valid(x, y) ) {
			if( A[x][y] == mn ) {
				visited[i][j] = call( x, y );
				break;
			}
		}
	}
	return visited[i][j];
}

int main() {
	freopen("b2.in","r",stdin);
	freopen("b2.ans","w",stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i, j;
		scanf("%d %d", &m, &n);
		for( i = 0; i < m; i++ ) {
			for( j = 0; j < n; j++ ) scanf("%d", &A[i][j]);
		}
		memset( visited, -1, sizeof(visited) );
		N = 0;
		for( i = 0; i < m; i++ ) for( j = 0; j < n; j++ ) call( i, j );
		int used[30];
		memset( used, -1, sizeof(used) );
		int M = 0;
		for( i = 0; i < m; i++ ) for( j = 0; j < n; j++ ) {
			if( used[ visited[i][j] ] == -1 ) used[ visited[i][j] ] = M++;
		}
		printf("Case #%d:\n", ++caseno);
		for( i = 0; i < m; i++ ) {
			for( j = 0; j < n; j++ ) {
				if( j ) putchar(' ');
				putchar( used[ visited[i][j] ] + 97 );
			}
			puts("");
		}
	}
	return 0;
}
