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

int cases, caseno, n;
pair <int, int> A[1005];


int main() {
	freopen("a2.in", "r", stdin);
	freopen("a2.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i, j;
		scanf("%d", &n);
		for( i = 0; i < n; i++ ) {
			scanf("%d %d", &A[i].first, &A[i].second);
		}
		sort( A, A + n );
		int res = 0;
		for( i = 0; i < n; i++ ) {
			for( j = i + 1; j < n; j++ ) {
				if( A[i].second > A[j].second ) res++;
			}
		}
		printf("Case #%d: %d\n", ++caseno, res);
	}
	return 0;
}
