/*
	Author       :	Jan
	Problem Name :
	Algorithm    :
	Complexity   :
*/

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define NN 1005

int cases, caseno;
int a[NN], n;
bool taken[NN];

int call( int i ) {
	if(taken[i]) return 0;

	taken[i] = true;
	return 1 + call( a[i] );
}

int main() {
	freopen("d.in", "r", stdin);
	freopen("d.ans", "w", stdout);

	double cl = clock();

	scanf("%d", &cases);
	while( cases-- ) {
		scanf("%d", &n);
		for( int i = 1; i <= n; i++ ) scanf("%d", &a[i]);

		int res = 0;

		memset( taken, 0, sizeof(taken) );
		for( int i = 1; i <= n; i++ ) {
			int k = call(i);
			if( k > 1 ) res += k;
		}
		printf("Case #%d: %d\n", ++caseno, res);
	}

	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
