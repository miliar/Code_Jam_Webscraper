#define FILENAME "c"

#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string.h>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CTO500 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()
#define VI vector<int>
#define VII vector<VI >
#define CL(a,b) memset(a,b,sizeof(a))  
#define UN(v) SORT(v),v.erase(unique(ALL(v)),v.end())  

typedef pair<int, int> PII;
typedef long long i64; 

void init(string file) {
    string ifile = file + ".in";
    string ofile = file + ".out";
	freopen(ifile.c_str(), "rt", stdin);
	freopen(ofile.c_str(), "wt", stdout);
}

void solve() {
    int T; cin>>T;
    REP(test,T){
        int n,l,h; cin>>n>>l>>h;
        VI a(n); REP(i,n)cin>>a[i];
        int res = 0;
        FOR(k,l,h+1){
            bool ok=1;
            REP(i,n) ok &= (a[i]%k == 0 || k%a[i] == 0);
            if (ok) { res = k; break; }
        }
        printf("Case #%d: ", test+1);
        if (!res) cout << "NO" << endl;
        else cout << res << endl;
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
