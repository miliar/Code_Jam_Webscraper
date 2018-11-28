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

string str[10];
int idx[10];

void run() {
    int n;
    cin >> n;
    REP(i,n) {
        cin >> str[i];
        idx[i] = 0;
        REP(j,n) {
            if (str[i][j] == '1') idx[i] = j;
        }
    }

    vector<int> mm;
    REP(i,n) mm.push_back(i);

    int res = 1000000000;
    do {
        bool flag = true;
        REP(i,n) {
            if (mm[i] < idx[i]) {
                flag = false;
                break;
            }
        }
        if (!flag) continue;

        vector<int> dd = mm;
        int cnt = 0;
        REP(j,n) {
            REP(k,n) {
                if (dd[k] == j) {
                    cnt += abs(k - j);
                    int tmp = dd[k];
                    RFOR(q,k-1,0) dd[q + 1] = dd[q];
                    dd[0] = tmp;
                    break;
                }
            }
        }
        res = min(res, cnt);
    } while (next_permutation(mm.begin(), mm.end()));

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
