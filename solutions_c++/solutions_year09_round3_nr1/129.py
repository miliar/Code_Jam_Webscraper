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
		freopen("A-large.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

void solve() {
	char input[100];
	gets ( input );

	int len = strlen(input);
	set<char> uniq;
	for (int i = 0; i < len; i++) {
		uniq.insert ( input[i] );
	}

	int base = uniq.size();
	base = max ( base, 2 );

	char meaning[256];
	int latest = 0;
	memset ( meaning, -1, sizeof( meaning ) );
	meaning[ input [ 0 ] ] = 1;

	int minnumber[100];

	for (int i = 0; i < len; i++) {
		if ( meaning [ input [ i ] ] == -1 ) {
			meaning [ input [ i ] ] = latest;
			if ( latest == 0 ) latest += 2;
			else latest++;
		}
		minnumber [ i ] = meaning [ input [ i ] ];
		//cout << minnumber[i];
	}
	//cout << endl;

	long long decimal = 0;
	long long mult = 1;

	for (int i = len - 1; i >= 0; i--) {
		decimal += minnumber [ i ] * mult;
		mult *= base;
	}
	
	static int test = 0;
	printf("Case #%d: %lld\n", ++test, decimal );
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}