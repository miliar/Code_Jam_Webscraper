#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
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

vector<int> primes(int n, int p) {
	vector<int> v;
	for (int i = 2; i * i <= n; i++) {
		if (n % i == 0 && i >= p) v.push_back(i);
		while (n % i == 0) n /= i;
	}
	if (n > 1 && n >= p) v.push_back(n);
	return v;
}

int ntest = 0;
void solve() {
	int A, B, P;
	scanf("%d %d %d",&A,&B,&P);
	int r = 0;
	map<int, set<int> > mp;
	FORE(i,A,B) {
		vector<int> p = primes(i, P);
		mp[i].insert(i);
		REPSZ(j,p) {
			mp[i].insert(p[j]);
			mp[p[j]].insert(i);
		}
	}
	set<int> visited;
	for (map<int, set<int> >::iterator ii = mp.begin(); ii != mp.end(); ++ii) if (visited.find(ii->first) == visited.end()) {
		r++;
		queue<int> q;
		q.push(ii->first);
		visited.insert(ii->first);
		while (!q.empty()) {
			int vert = q.front(); q.pop();
			for (set<int>::iterator jj = mp[vert].begin(); jj != mp[vert].end(); ++jj) if (visited.find(*jj) == visited.end()) {
				visited.insert(*jj);
				q.push(*jj);
			}
		}
	}
	printf("Case #%d: %d\n",++ntest,r);
}

int main() {
	openfiles();

	int n; scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}
