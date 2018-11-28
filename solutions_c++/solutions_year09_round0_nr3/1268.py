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

char a[1001];
int cases, caseno, len;

char A[30] = {"welcome to code jam"};

int dp[30][1001];
int state[30][1001];

int call( int i, int j ) {
	if( i == 19 ) return 1;
	if( j == len ) return 0;

	int &ret = dp[i][j];
	int &st = state[i][j];

	if( st == caseno ) return ret;
	st = caseno;

	ret = call( i, j + 1 );
	if( A[i] == a[j] ) ret += call( i + 1, j + 1 );

	ret %= 10000;
	return ret;
}

int main() {
	freopen("c2.in","r",stdin);
	freopen("c2.ans","w",stdout);

	scanf("%d", &cases);
	gets(a);
	while( cases-- ) {
		gets(a);
		len = strlen( a );
		++caseno;
		printf("Case #%d: %04d\n", caseno, call( 0, 0 ));
	}
	return 0;
}
