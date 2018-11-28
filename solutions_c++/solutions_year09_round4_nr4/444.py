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

bool is_inside ( int X, int Y, int radius, int X2, int Y2 )
{
	if ( hypot ( (double)(X2 - X), (double)(Y2 - Y) ) < (double)radius + EPS )
		return true;
	return false;
}

void solve() {
	int n;
	scanf("%d",&n);

	vector<int> X ( n ), Y ( n );
	vector<int> radius ( n );
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d",&X[i],&Y[i],&radius[i]);
	}

	vector <int> inside ( n, 0 );

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if ( is_inside ( X[i], Y[i], radius[i], X[j], Y[j] ) ) {
				inside [ j ] = 1;
			}
		}
	}

	for (int j = n - 1; j >= 0; j--) {
		if ( inside [ j ] ) {
			X.erase ( X.begin() + j );
			Y.erase ( Y.begin() + j );
			radius.erase ( radius.begin() + j );
		}
	}

	n = X.size();

	static int test = 0;
	printf("Case #%d: ", ++test);

	if (n == 1) {
		printf("%.8lf\n", (double)radius[0]);
	}
	else if (n == 2) {
		printf("%.8lf\n", (double)max(radius[0], radius[1]));
	}
	else if (n == 3) {
		double best = 1e10;
		if ( max ( 0.5 * ( hypot ( (double)(X[0] - X[1]), (double)(Y[0] - Y[1]) ) + radius[0] + radius[1]), (double) radius [2] ) < best ) {
			best = max ( 0.5 * ( hypot ( (double)(X[0] - X[1]), (double)(Y[0] - Y[1]) ) + radius[0] + radius[1]), (double) radius [2] );
		}
		if ( max ( 0.5 * ( hypot ( (double)(X[2] - X[1]), (double)(Y[2] - Y[1]) ) + radius[2] + radius[1]), (double) radius [0] ) < best ) {
			best = max ( 0.5 * ( hypot ( (double)(X[2] - X[1]), (double)(Y[2] - Y[1]) ) + radius[2] + radius[1]), (double) radius [0] );
		}		
		if ( max ( 0.5 * ( hypot ( (double)(X[0] - X[2]), (double)(Y[0] - Y[2]) ) + radius[0] + radius[2]), (double) radius [1] ) < best ) {
			best = max ( 0.5 * ( hypot ( (double)(X[0] - X[2]), (double)(Y[0] - Y[2]) ) + radius[0] + radius[2]), (double) radius [1] );
		}
		printf("%.8lf\n", (double)best);
	}
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}