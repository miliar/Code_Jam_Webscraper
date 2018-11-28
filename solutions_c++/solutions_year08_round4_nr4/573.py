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

string compress(string x, int k, vector<int> v) {
	int n = x.length();
	stringstream ss;
	REP(i,n/k) {
		int off = i * k;
		REP(j,k) {
			ss << x[off + v[j]];
		}
	}
	return ss.str();
}

int analyze(string x) {
	int k = 0;
	char last = -1;
	int n = x.length();
	REP(i,n) {
		if (x[i] != last) k++;
		last = x[i];
	}
	return k;
}

int ntest = 0;
void solve() {
	char line[10000];
	int k; scanf("%d ",&k);
	gets(line);
	string x = line;
	vector<int> v;
	REP(i,k) v.push_back(i);
	int best = 0x7fffffff;
	do {
		string out = compress(x, k, v);
		best = min(best, analyze(out));
	} while (next_permutation(v.begin(), v.end()));
	printf("Case #%d: %d\n", ++ntest, best);
}

int main() {
	openfiles();
	int n; scanf("%d", &n);
	REP(i,n) solve();

	return 0;
}