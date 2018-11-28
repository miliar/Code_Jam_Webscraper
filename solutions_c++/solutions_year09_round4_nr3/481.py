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
		freopen("test.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

bool inter ( vector < int > A, vector < int > B ) {
	int n = A.size();

	for (int i = 0; i < n; i++) {
		if ( A [ i ] == B [ i ] )
			return true;
	}

	for (int i = 0; i < n - 1; i++) {
		if ( ( A [ i ] > B [ i ] && A [ i + 1 ] < B [ i + 1 ] ) || ( A [ i ] < B [ i ] && A [ i + 1 ] > B [ i + 1 ] ) )
			return true;
	}

	return false;
}

int count_ones ( int n ) {
	int s = 0;
	while ( n ) {
		s += n & 1;
		n >>= 1;
	}
	return s;
}

void solve() {
	int n, k;
	scanf("%d %d ", &n, &k);

	vector < vector < int > > P ( n , vector < int > ( k , 0 ) );

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < k; j++) {
			scanf ( "%d", &P[i][j] );
		}
	}

	vector < vector < int > > G ( n, vector < int > ( n, 0 ) );
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			G [ i ] [ j ] = G [ j ] [ i ] = inter ( P [ i ], P [ j ] );
		}
	}

	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < n; j++) {
	//		cout << G [ i ] [ j ] << " ";
	//	}
	//	cout << endl;
	//}

	int worst = 0;
	
	for (int i = 0; i < (1 << n); i++) {
		bool clique = true;
		for (int ii = 0; ii < n && clique; ii++) if ( (i >> ii) & 1 ) {
			for (int jj = ii + 1; jj < n && clique; jj++) if ( ( i >> jj ) & 1 ){
				if ( G [ ii ] [ jj ] == 0 ) {
					clique = false;
				}
			}
		}
		if ( clique ) {
			worst = max ( count_ones ( i ), worst );
		}
	}

	static int test = 0;
	printf("Case #%d: %d\n", ++test, worst);
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}