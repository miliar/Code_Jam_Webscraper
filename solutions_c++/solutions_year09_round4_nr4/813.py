#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)

vector<string> split( const string& s, const string& delim =" " ) {
    vector<string> res;
    string t;
    for ( int i = 0 ; i != s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
                res.push_back( t );
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
        res.push_back(t);
    }
    return res;
}

vector<int> splitInt( const string& s, const string& delim =" " ) {
    vector<string> tok = split( s, delim );
    vector<int> res;
    for ( int i = 0 ; i != tok.size(); i++ ) {
        int m = atoi(tok[i].c_str());
        res.push_back(m);
    }
    return res;
}

int n;
double x[10], y[10], r[10];

double doit(int i1, int i2, int i3) {
    if (r[i1] > r[i2]) swap(i1, i2);

    double res = 0.0;

    double dis = sqrt((x[i1] - x[i2]) * (x[i1] - x[i2]) + (y[i1] - y[i2]) * (y[i1] - y[i2]));
    if (dis + r[i1] <= r[i2]) res = r[i2];
    else res = (dis + r[i1] + r[i2]) / 2.0;

    res = max(res, r[i2]);

    return res;
}

void run() {
    cin >> n;
    REP(i,n) cin >> x[i] >> y[i] >> r[i];
    
    double res = 2000000000.0;

    if (n == 1) res = r[0];
    else if (n == 2) {
        res = max(r[0], r[1]);
    } else if (n == 3) {
        res = min(res, doit(0, 1, 2));
        res = min(res, doit(1, 2, 0));
        res = min(res, doit(0, 2, 1));
    }

    cout << res << endl;
}

int main() {
    int K;
    cin >> K;
    FOR(k,1,K) {
        cout << "Case #" << k << ": ";
        run();
    }
    return 0;
}
