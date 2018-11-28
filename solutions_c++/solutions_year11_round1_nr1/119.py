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

typedef long long i64;

int cases, caseno;

i64 gcd( i64 a, i64 b ) {
	return !b ? a : gcd( b, a % b );
}

bool solveCase( i64 n, i64 perToday, i64 perTotal ) {
	if( perToday < 100 && perTotal == 100 ) return false;
	if( perToday > 0 && perTotal == 0 ) return false;

	if( perToday == 100 && perTotal == 100 ) return true;
	if( perToday == 0 && perTotal == 0 ) return true;

	i64 wtoday = perToday / gcd( perToday, 100 );
	i64 ptoday = 100 / gcd( perToday, 100 );

	fprintf(stderr, "%lld %lld\n", wtoday, ptoday);

	if( ptoday > n ) return false;

	i64 wtotal = perTotal / gcd( perTotal, 100 );
	i64 ptotal = 100 / gcd( perTotal, 100 );

	fprintf(stderr, "%lld %lld\n", wtotal, ptotal);
	return true;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.ans", "w", stdout);

	double cl = clock();
	scanf("%d", &cases);
	while( cases-- ) {
		printf("Case #%d: ", ++caseno);

		i64 n, perToday, perTotal;
		scanf("%lld %lld %lld", &n, &perToday, &perTotal);

		if( !solveCase( n, perToday, perTotal ) ) puts("Broken");
		else puts("Possible");
	}

	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
