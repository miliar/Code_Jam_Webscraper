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
        int n; scanf("%d\n", &n);
        vector<string> a;
        vector<double> x(n), y(n);
        REP(i,n){
            string s; getline(cin,s);
            a.pb(s);
            REP(j,n){
                x[i] += (a[i][j] == '1');
                y[i] += isdigit(a[i][j]);
            }
        }
        vector<double> owp(n);
        REP(i,n){
            REP(j,n){
                if (a[i][j] == '.') continue;
                owp[i] += (x[j]-(a[j][i]=='1'))/(y[j]-1);
            }
            owp[i] /= y[i];
        }
        vector<double> oowp(n);
        REP(i,n){
            REP(j,n){
                if (a[i][j] == '.') continue;
                oowp[i] += owp[j];
            }
            oowp[i] /= y[i];
        }
        printf("Case #%d:\n", test+1);
        REP(i,n){
            printf("%.8f\n", 0.25*(x[i]/y[i]) + 0.5*owp[i] + 0.25*oowp[i]);
        }
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
