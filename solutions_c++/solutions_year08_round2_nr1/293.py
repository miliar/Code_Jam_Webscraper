#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <set>
#include <map>
#include <sstream>
#include <math.h>
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
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
	#endif
}

bool ok (long long a, long long b, long long c) {
	return (a + b + c) % 3 == 0;
}

int ntest = 0;
void solve() {
	long long n, A, B, C, D, x0, y0, M;
	scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n, &A, &B, &C, &D, &x0, &y0, &M);
	vector<pair<long long, long long> > P;
	long long X = x0, Y = y0;
	P.PB(MP(X,Y));
	FOR(i,1,n) {
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		P.PB(MP(X,Y));
	}

	long long d[3][3]; memset(d, 0, sizeof(d));
	long long r = 0;
	REP(i,n) d[P[i].first % 3][P[i].second % 3]++;
	REP(i,9) FOR(j,i+1,9) FOR(k,j+1,9) if (ok(i/3,j/3,k/3) && ok(i%3,j%3,k%3))
		r += d[i/3][i%3] * d[j/3][j%3] * d[k/3][k%3];
	REP(i,9) FOR(j,i+1,9) if (ok(i/3,i/3,j/3) && ok(i%3,i%3,j%3))
		r += d[i/3][i%3] * (d[i/3][i%3] - 1) * d[j/3][j%3] / 2;
	REP(i,9)
		r += d[i/3][i%3] * (d[i/3][i%3] - 1) * (d[i/3][i%3] - 2) / 6;

	printf("Case #%d: %lld\n",++ntest,r);
}

int main() {
	openfiles();

	int n; scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}
