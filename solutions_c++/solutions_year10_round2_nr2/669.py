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
int n, k, b, t;

struct info {
	int x, speed, flag;
};

info A[55];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i, j;
		scanf("%d %d %d %d", &n, &k, &b, &t);

		for( i = 0; i < n; i++ ) scanf("%d", &A[i].x);
		for( i = 0; i < n; i++ ) scanf("%d", &A[i].speed);

		int cnt = 0;
		for( i = 0; i < n; i++ ) {
			if( A[i].speed * t >= b - A[i].x ) A[i].flag = 1, cnt++;
			else A[i].flag = 0;
		}

		printf("Case #%d: ", ++caseno);
		if( cnt < k ) puts("IMPOSSIBLE");
		else {
			int res = 0;
			while( 1 ) {
				cnt = 0;
				for( i = n - 1; i >= 0; i-- ) {
					if( A[i].flag ) cnt++;
					else break;
				}
				if( cnt >= k ) break;
				for( i = 0; i < n - 1; i++ ) if( A[i].flag == 1 && A[i+1].flag == 0 ) {
					cnt = 0;
					for( j = i + 1; j < n; j++ ) if( A[j].flag == 1 ) cnt++;
					if( cnt >= k ) continue;
					swap( A[i], A[i+1] );
					res++;
					break;
				}
			}
			printf("%d\n", res);
		}
	}
	return 0;
}
