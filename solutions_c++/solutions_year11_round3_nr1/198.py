#define FILENAME "a"

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
        int n,m; scanf("%d %d\n",&n,&m);
        vector<string> a(n+2);
        string s; REP(i,m+2) s += '.';
        a[0] = a[n+1] = s;
        REP(i,n) getline(cin, s), a[i+1] = '.' + s + '.';
        REP(j,m+1){
            REP(i,n+1){
                if (a[i][j] == a[i][j+1] && a[i][j] == a[i+1][j] && a[i][j] == a[i+1][j+1] && a[i][j] == '#') {
                    a[i][j] = '/', a[i][j+1] = '\\', a[i+1][j] = '\\', a[i+1][j+1] = '/';
                }
            }
        }
        bool ok = 1;
        REP(i,a.sz)REP(j,a[0].sz)if(a[i][j]=='#') ok=0;
        printf("Case #%d:\n", test+1);
        if (!ok) cout<<"Impossible"<<endl;
        else {
            FOR(i,1,n+1){
                FOR(j,1,m+1)cout<<a[i][j];
                cout<<endl;
            }
        }
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
