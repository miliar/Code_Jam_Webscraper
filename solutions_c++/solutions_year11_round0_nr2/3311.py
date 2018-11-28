#define FILENAME "b"

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
    int tests; cin>>tests;
    REP(test,tests){
        int c, o, n;
        char C[255][255]; CL(C, 0);
        char O[255][255]; CL(O, 0);
        string s;
        cin>>c; REP(i,c) cin >> s, C[s[0]][s[1]] = C[s[1]][s[0]] = s[2];
        cin>>o; REP(i,o) cin >> s, O[s[0]][s[1]] = O[s[1]][s[0]] = 1;
        cin>>n>>s;
        string res;
        REP(i,s.sz){
            if (!res.sz) {res += s[i]; continue;}
            if (C[res[res.sz-1]][s[i]]) {
                res = res.substr(0,res.sz-1) + C[res[res.sz-1]][s[i]];
            } else {
                bool ok = 0;
                REP(j,res.sz) if (O[res[j]][s[i]]) ok = 1;
                if (ok) res = ""; else res += s[i];
            }
        }
        cout << "Case #" << (test+1) << ": [";
        REP(i,res.sz) cout << res[i] << ((i==res.sz-1)?"":", ");
        cout << "]" << endl;
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
