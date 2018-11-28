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

#define NN 105

int cases, caseno;
int p, q, n;
char comb[NN][5], opp[NN][5], a[NN], b[NN];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.ans", "w", stdout);

	double cl = clock();

	scanf("%d", &cases);
	while( cases-- ) {
		scanf("%d", &p);
		for( int i = 0; i < p; i++ ) scanf("%s", comb[i]);

		scanf("%d", &q);
		for( int i = 0; i < q; i++ ) scanf("%s", opp[i]);

		scanf("%d %s", &n, a);
		int i = 0;
		for( int j = 0; j < n; j++ ) {
			bool foundComb = false;
			b[i++] = a[j];
			if( i > 1 ) {
				for( int k = 0; k < p; k++ ) if( ( comb[k][0] == b[i-2] && comb[k][1] == b[i-1] ) || ( comb[k][1] == b[i-2] && comb[k][0] == b[i-1] ) ) {
					b[i-2] = comb[k][2];
					i--;
					foundComb = true;
					break;
				}
			}
			if( !foundComb && i > 1 ) {
				for( int k = 0; k < q; k++ ) {
					int c = -1;
					if( opp[k][0] == b[i-1] ) c = opp[k][1];
					else if( opp[k][1] == b[i-1] ) c = opp[k][0];
					if( c != -1 ) {
						for( int l = 0; l < i - 1; l++ ) {
							if( b[l] == c ) {
								i = 0;
								break;
							}
						}
					}
				}
			}
		}
		printf("Case #%d: [", ++caseno);
		for( int k = 0; k < i; k++ ) {
			if( k ) printf(", ");
			printf("%c", b[k]);
		}
		puts("]");
	}

	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
