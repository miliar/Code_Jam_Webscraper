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
char ch[NN], dt[NN], n;
char symbol[] = {"OB"};

int findNext( int k, int covered ) {
	for( int i = covered; i < n; i++ ) if( ch[i] == symbol[k] ) return dt[i];
	return -1;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.ans", "w", stdout);

	double cl = clock();

	scanf("%d", &cases);
	while( cases-- ) {
		scanf("%d", &n);
		for( int i = 0; i < n; i++ ) {
			scanf(" %c %d", &ch[i], &dt[i]);
		}
		int pos[2];
		pos[0] = pos[1] = 1;
		int covered = 0, cnt = 0;

		while( covered < n ) {
			int k[2], ins = 0;
			k[0] = findNext( 0, covered );
			k[1] = findNext( 1, covered );

			if( k[0] != -1 ) {
				if( pos[0] == k[0] ) {
					if( ch[covered] == 'O' ) {
						covered++;
						ins = 1;
					}
				}
				else {
					pos[0] += (pos[0] < k[0]) ? +1 : -1;
				}
			}
			if( k[1] != -1 ) {
				if( pos[1] == k[1] ) {
					if( ch[covered] == 'B' && !ins ) {
						covered++;
					}
				}
				else {
					pos[1] += (pos[1] < k[1]) ? +1 : -1;
				}
			}
			cnt++;
		}
		printf("Case #%d: %d\n", ++caseno, cnt);
	}


	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
