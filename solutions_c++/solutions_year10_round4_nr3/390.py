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

int cases, caseno, R, A[105][105], B[105][105], m1, n1, m2, n2;

bool isEmpty() {
	for( int i = m1; i <= m2; i++ ) {
		for( int j = n1; j <= n2; j++ ) if( A[i][j] ) return false;
	}
	return true;
}

void Update() {
	int i, j;
	for( i = m1; i <= m2; i++ ) {
		for( j = n1; j <= n2; j++ ) {
			B[i][j] = A[i][j];
			bool flag = false;
			if( (i > m1 && A[i-1][j] == 0) || i == m1 ) {
				if( (j > n1 && A[i][j-1] == 0) || j == n1 ) {
					B[i][j] = 0;
					flag = true;
				}
			}
			if( !flag && A[i][j] == 0 ) {
				if( i > m1 && A[i-1][j] == 1 ) {
					if( j > n1 && A[i][j-1] == 1 ) {
						B[i][j] = 1;
						flag = true;
					}
				}				
			}
		}
	}
	for( i = m1; i <= m2; i++ ) {
		for( j = n1; j <= n2; j++ ) {
			A[i][j] = B[i][j];
		}
	}
}

void print() {
	int i, j;
	for( i = m1; i <= m2; i++ ) {
		for( j = n1; j <= n2; j++ ) {
			printf("%d", A[i][j]);
		}
		puts("");
	}
	puts("");
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		m2 = n2 = 0;
		m1 = n1 = 100;
		scanf("%d", &R);
		int i, j;
		memset( A, 0, sizeof(A) );
		while( R-- ) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
			//x1--, y1--, x2--, y2--;

			for( i = x1; i <= x2; i++ ) {
				for( j = y1; j <= y2; j++ ) A[i][j] = 1;
			}
			m1 = min( m1, x1 );
			n1 = min( n1, y1 );
			m2 = max( m2, x2 );
			n2 = max( n2, y2 );
		}
		//printf("%d %d %d %d\n", m1, m2, n1, n2);
		m1--, n1--, m2++, n2++;
		int res;
		
		for( res = 1; ;res++ ) {
			Update();
			if( isEmpty() ) break;
		}
		printf("Case #%d: %d\n", ++caseno, res);
		cerr << caseno << endl;
	}
	return 0;
}
