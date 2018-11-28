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

#define i64 long long

int cases, caseno;
int fl[11000005];
i64 n;

void calc() {
	for( int i = 2; i < 11000000; i++ ) if( !fl[i] ) for( int j = i + i; j < 11000000; j += i ) fl[j] = 1;
}

i64 case1() {
	i64 mx = 1, mn = 0;
	for( int i = 2; i <= n; i++ ) if( !fl[i] ) {
		i64 k = n, cnt = 0, x = 1;
		while( k >= i ) {
			cnt++, k /= i;
		}
		mx += cnt;
		mn++;
		if( cnt == 1 ) break;
	}
	if( n == 1 ) mx = mn = 0;
	return mx - mn;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.ans", "w", stdout);

	double cl = clock();
	calc();
	scanf("%d", &cases);
	while( cases-- ) {
		scanf("%lld", &n);
		i64 res;
		res = case1();
		printf("Case #%d: %lld\n", ++caseno, res);

		cerr << caseno << endl;
	}

	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
