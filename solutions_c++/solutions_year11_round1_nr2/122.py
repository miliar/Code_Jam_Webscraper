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

const int NN = 10005;

int cases, caseno, n, q;
char word[NN][15], len[NN], order[30];

char s[NN][15];

void buildFlag( int k, bool fl[26] ) {
	for( int i = 0; i < 26; i++ ) fl[i] = false;
	for( int i = 0; i < k; i++ ) {
		for( int j = 0; s[i][j]; j++ ) fl[ s[i][j] - 'a' ] = true;
	}
}

int check( int x ) {
	int K = 0, res = 0;
	bool fl[26];
	for( int i = 0; i < n; i++ ) if( len[i] == len[x] ) {
		strcpy( s[K], word[i] );
		K++;
	}
	if( K == 1 ) return res;
	buildFlag( K, fl );
	char p[] = {"------------"};
	p[ len[x] ] = 0;
	int rev = 0, i = 0;
	while( rev < len[x] ) {
		if( fl[ order[i] - 'a' ] ) {
			bool found = false;
			for( int j = 0; j < len[x]; j++ ) if( word[x][j] == order[i] ) {
				found = true;
				p[j] = order[i];
				rev++;
			}
			if( !found ) {
				res++;
				int newK = 0;
				for( int z = 0; z < K; z++ ) {
					found = false;
					for( int k = 0; s[z][k]; k++ ) {
						if( s[z][k] == order[i] ) {
							found = true;
							break;
						}
					}
					if( !found ) {
						strcpy( s[newK], s[z] );
						newK++;
					}
				}
				K = newK;
				if( K == 1 ) return res;
				buildFlag( K, fl );
			}
			else {
				int newK = 0;
				for( int z = 0; z < K; z++ ) {
					found = false;
					for( int k = 0; s[z][k]; k++ ) {
						if( s[z][k] == order[i] ) {
							if( p[k] != order[i] ) {
								found = true;
								break;
							}
						}
						else if( p[k] == order[i] ) {
							found = true;
							break;
						}
					}
					if( !found ) {
						strcpy( s[newK], s[z] );
						newK++;
					}
				}
				K = newK;
				if( K == 1 ) return res;
				buildFlag( K, fl );
			}
		}
		i++;
	}
	return res;
}

int findResult() {
	int r = -1, p = -1;
	for( int i = 0; i < n; i++ ) {
		int x = check(i);
		if( x > r ) {
			r = x;
			p = i;
		}
	}
	return p;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.ans", "w", stdout);

	double cl = clock();
	scanf("%d", &cases);
	while( cases-- ) {
		printf("Case #%d:", ++caseno);

		scanf("%d %d", &n, &q);
		for( int i = 0; i < n; i++ ) {
			scanf("%s", word[i]);
			len[i] = strlen( word[i] );
		}
		while(q--) {
			scanf("%s", order);
			int x = findResult();
			printf(" %s", word[x]);
		}
		puts("");
	}

	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);

	return 0;
}
