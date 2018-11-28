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

int n, cases, caseno;

struct info {
	char a[50];
	int mx;
}A[50];

int B[50];

bool canSolve( int i, int j ) {
	int k, p = 0;
	for( k = i; k < n; k++ ) if( k != j ) {
		B[p++] = A[k].mx;
	}
	sort( B, B + p );

	for( k = i + 1, p = 0; k < n; k++, p++ ) {
		if( B[p] > k ) return false;
	}
	return true;
}

int main() {
	freopen("a2.in","r",stdin);
	freopen("a2.ans","w",stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i, j;

		scanf("%d", &n);
		for( i = 0; i < n; i++ ) {
			scanf("%s", A[i].a);
			A[i].mx = 0;
			for( j = 0; j < n; j++ ) if( A[i].a[j] == '1' ) A[i].mx = j;
		}

		int res = 0, k;

		for( i = 0; i < n; i++ ) {
			for( j = i; j < n; j++ ) if( A[j].mx <= i ) {
				if( canSolve( i , j ) ) {
					res += (j-i);

					for( k = j; k > i; k-- ) {
						A[k] = A[k-1];
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", ++caseno, res);
	}
	return 0;
}
