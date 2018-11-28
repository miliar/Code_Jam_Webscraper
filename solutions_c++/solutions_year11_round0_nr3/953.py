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

int cases, caseno;

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.ans", "w", stdout);

	double cl = clock();

	scanf("%d", &cases);
	while( cases-- ) {
		int x = 0, s = 0, mn = 1000000000, k, n;
		scanf("%d", &n);
		for( int i = 0; i < n; i++ ) {
			scanf("%d", &k);
			x ^= k;
			s += k;
			mn = min( mn, k );
		}
		printf("Case #%d: ", ++caseno);
		if( x ) puts("NO");
		else printf("%d\n", s - mn);
	}
	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
