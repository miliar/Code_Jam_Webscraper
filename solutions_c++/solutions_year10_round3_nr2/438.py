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

int cases, caseno, L, R, C;

int dp[1001][1001][11];
bool state[1001][1001][11];

int call( int L, int R ) {
	if( L * C >= R ) return 0;

	int &ret = dp[L][R][C];
	if( state[L][R][C] == true ) return ret;
	state[L][R][C] = true;

	int k, r1, r2;

	ret = 1000000000;
	for( k = L * C; k <= R; k++ ) {
		r1 = call( k, R );
		r2 = call( L, k );
		r1 = max(r1, r2);
		r1++;
		ret = min( ret, r1 );
	}
	return ret;
}

int main() {
	freopen("b1.in", "r", stdin);
	freopen("b1.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		scanf("%d %d %d", &L, &R, &C);
		printf("Case #%d: ", ++caseno);
		int res = call( L, R );
		printf("%d\n", res);
		cerr << caseno << endl;
	}
	return 0;
}
