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
typedef long long ll; 
const double EPS = 1e-7;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("test.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

int ntest = 0;
void solve() {
	int n, m, r;
	scanf("%d %d %d",&n,&m,&r);
	REPE(x1, n) REPE(x2, n) REPE(y1, m) REPE(y2, m) {
		if (x1 == 0 && y1 == 0) continue;
		if (x2 == 0 && y2 == 0) continue;
		if (x1 == x2 && y1 == y2) continue;
		int res = x1 * y2 - x2 * y1;
		if (res == r) {
			printf("Case #%d: %d %d %d %d %d %d\n", ++ntest, 0, 0, x1, y1, x2, y2);
			return;
		}
	}
	printf("Case #%d: IMPOSSIBLE\n", ++ntest);
}

int main() {
	openfiles();
	int n; scanf("%d", &n);
	REP(i,n) solve();

	return 0;
}