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
#include <string>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define CLR(x) memset((x),0,sizeof((x)))
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;

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
    for ( int i = 0 ; i != tok.size(); i++ )
        res.push_back( atoi( tok[i].c_str() ) );
    return res;
}

int s2i(string s) {
    stringstream ss;
    ss << s;
    int res;
    ss >> res;
    return res;
}

string i2s(int n) {
    stringstream ss;
    ss << n;
    string res;
    ss >> res;
    return res;
}

void run() {
    int n;
    scanf("%d", &n);
    vector<int> d(n), l(n);
    REP(i,n) {
        scanf("%d %d", &d[i], &l[i]);
    }
    int D;
    scanf("%d", &D);
    vector<int> mm(n);
    RFOR(i,n-1,0) {
        if (D - d[i] > l[i]) mm[i] = -1;
        else mm[i] = D - d[i];
        FOR(j,i+1,n-1) {
            if (mm[j] == -1) continue;
            int dd = d[j] - d[i];
            if (dd > l[i]) break;
            int tt = min(dd, l[j]);
            if (tt < mm[j]) continue;
            mm[i] = dd;
            break;
        }
    }
    if ((mm[0] == -1) || (d[0] < mm[0])) printf("NO\n");
    else printf("YES\n");
}

int main() {
    int k;
    scanf("%d", &k);
    FOR(c,1,k) {
        printf("Case #%d: ", c);
        run();
    }
    return 0;
}
