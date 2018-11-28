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

int cases, n, caseno;

struct circle {
	int x, y, r;
}C[10];

double Distance( int x1, int y1, int x2, int y2 ) {
	return sqrt( ( x1 - x2) * ( x1 - x2) + ( y1 - y2) * ( y1 - y2)  );
}

double findResult( circle c1, circle c2 ) {
	double d = Distance( c1.x, c1.y, c2.x, c2.y ) + c1.r + c2.r;
	return d/2;
}

int main() {
	freopen("d1.in","r",stdin);
	freopen("d1.ans","w",stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i;
		scanf("%d", &n);

		for( i = 0; i < n; i++ ) {
			scanf("%d %d %d", &C[i].x, &C[i].y, &C[i].r);
		}

		printf("Case #%d: ", ++caseno);
		if( n == 1 ) printf("%d\n", C[0].r);
		else if( n == 2 ) printf("%d\n", max( C[0].r, C[1].r ) );
		else {
			double res = max(findResult( C[0], C[1] ), double( C[2].r ) );
			double res1 = max(findResult( C[1], C[2] ), double( C[0].r ) );
			if( res > res1 ) res = res1;
			res1 = max(findResult( C[0], C[2] ), double( C[1].r ) );
			if( res > res1 ) res = res1;

			printf("%lf\n", res);
		}
	}
	return 0;
}
