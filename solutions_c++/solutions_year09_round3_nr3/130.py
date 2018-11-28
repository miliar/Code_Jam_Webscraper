#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
#define FILL(a,b) memset(a, (b), sizeof(a));
typedef long long ll; 
const double EPS = 1e-7;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("C-large.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

void solve() {
	int n, q;
	scanf("%d %d ", &n, &q);
	int position[110];
	for (int i = 0; i < q; i++) {
		scanf("%d ",&position[i]);
		position[i]--;
	}
	
	pair<int, int> adj[110];
	for (int i = 0; i < q; i++) {
		int p = position[i];
		if (i == 0) {
			adj [ i ].first = -1;
		}
		else {
			adj [ i ].first = position [ i - 1 ];
		}

		if ( i == q - 1 ) {
			adj [ i ].second = n;
		}
		else {
			adj [ i ].second = position [ i + 1 ];
		}
	}

	const int MAX = 1000000000;
	vector < vector < int > > dp ( q, vector<int> ( q, MAX ) );

	for (int l = 0; l < q; l++) {
		for (int i = 0; i < q - l; i++) {
			int j = i + l;
			for (int k = i; k <= j; k++) {
				int a = position [ k ] - adj [ i ].first - 1;
				int b = adj [ j ].second - position [ k ] - 1;
				int c = ( k == i ? 0 : dp [ i ] [ k - 1 ] );
				int d = ( k == j ? 0 : dp [ k + 1 ] [ j ] );
				int sum = a + b + c + d;
				dp [ i ] [ j ] = min ( dp [ i ] [ j ], sum );
			}
		}
	}

	static int test = 0;
	printf("Case #%d: %d\n", ++test, dp [ 0 ] [ q - 1 ] );
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}