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

#define i64 __int64

const int inf = 1000000000;

int cases, caseno, P, need[3000], n;
int state[3000][15];
i64 dp[3000][15];

i64 call( int i, int taken ) {
	if( i >= ( 1 << P ) ) {
		if( taken >= need[i] ) return 0;
		return inf;
	}

	i64 &ret = dp[i][taken];
	int &st = state[i][taken];
	if( st == caseno ) return ret;
	st = caseno;

	ret = inf;

	// take i
	ret = need[i] + call( 2 * i, taken + 1 ) + call( 2 * i + 1, taken + 1 );
	i64 r = call( 2 * i, taken ) + call( 2 * i + 1, taken );

	ret = min(ret, r);
	return ret;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i, j, x;
		scanf("%d", &P);
		for( i = 0; i < ( 1 << P ); i++ ) {
			scanf("%d", &need[i + ( 1 << P )]);
			need[i + ( 1 << P )] = P - need[i + ( 1 << P )];
		}
		int X = ( 1 << ( P - 1) );
		for( i = ( 1 << (P - 1) ); i >= 1; i /= 2, X /= 2 ) {
			for( j = i, x = 0; x < X; j++, x++ ) scanf("%d", &need[j]);
		}		
		++caseno;
		n = ( 1 << ( P + 1 ) );
		i64 res = call( 1, 0 );
		printf("Case #%d: %I64d\n", caseno, res);

	}
	return 0;
}
