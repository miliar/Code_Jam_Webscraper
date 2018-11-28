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

void solve() {
	vector<int> arr;
	int n;
	scanf("%d ",&n);
	char line[100];

	for (int i = 0; i < n; i++) {
		gets(line);
		int mx = -1;
		for (int j = 0; j < n; j++) {
			if ( line [ j ] == '1' )
				mx = j;
		}

		arr.push_back( mx );
	}

	int swaps = 0;

	for (int i = 0; i < n; i++) {
		if ( arr [ i ] > i ) {
			for (int j = i + 1; j < n; j++) {
				if ( arr [ j ] <= i ) {
					swaps += j - i;
					for (int k = j; k > i; k--) {
						arr [ k ] = arr [ k - 1 ];
					}
					break;
				}
			}
		}
	}

	static int test = 0;
	printf("Case #%d: %d\n", ++test, swaps);
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}