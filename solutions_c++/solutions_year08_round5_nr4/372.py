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

const int MOD = 10007;

int di[] = {1, 2};
int dj[] = {2, 1};
int RES[105][105];

void recur(int i, int j, int N, int M) {
	if (i <= 0 || i > N || j <= 0 || j > N) {
		return;
	}
	REP(k,2) {
		int ii = i + di[k];
		int jj = j + dj[k];

	}
}

bool valid(int i, int j, int N, int M, vector<pair<int, int> >& v) {
	if (i <= 0 || i > N || j <= 0 || j > M) return false;
	REPSZ(k,v) if (i == v[k].first && j == v[k].second) return false;
	return true;
}

void solve() {
	int N, M; scanf("%d %d",&N,&M);
	int R; scanf("%d",&R);
	vector<pair<int, int> > rooks(R);
	REP(i,R) scanf("%d %d",&rooks[i].first, &rooks[i].second);
	queue<pair<int, int> > q;
	q.push(MP(1,1));
	memset(RES,0,sizeof(RES));
	set<pair<int, int> > s;
	RES[1][1] = 1;
	while (!q.empty()) {
		pair<int, int> P = q.front();
		q.pop();
		int i = P.first, j = P.second;
		REP(k,2) {
			int ii = i + di[k];
			int jj = j + dj[k];
			if (valid(ii, jj, N, M, rooks)) {
				RES[ii][jj] = (RES[i][j] + RES[ii][jj]) % MOD;
				if (s.find(MP(ii,jj)) == s.end()) {
					q.push(MP(ii,jj));
					s.insert(MP(ii,jj));
				}
			}
		}
	}
	static int test = 0;
	printf("Case #%d: %d\n", ++test, RES[N][M]);
}

int main() {
	openfiles();
	int n; scanf("%d",&n);
	REP(i,n) solve();

	return 0;
}