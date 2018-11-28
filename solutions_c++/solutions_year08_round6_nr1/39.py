#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <set>
#include <cmath>
using namespace std;

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
    if (!t.empty() ) {
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
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define CLR(x) memset((x),0,sizeof((x)))
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;

#define MAXN 2000000000

inline LL gcd(LL a,LL b){
    return b?gcd(b,a%b):a;
}

inline LL lcm(LL a,LL b){
    return a/gcd(a,b)*b;
}

LL s2ll(string s) {
    stringstream ss;
    ss << s;
    LL res;
    ss >> res;
    return res;
}

string ll2s(LL n) {
    stringstream ss;
    ss << n;
    string res;
    ss >> res;
    return res;
}

vector<int> birdh, birdw;
vector<int> nonbirdh, nonbirdw;

void run() {
    birdh.clear(), birdw.clear();
    nonbirdh.clear(), nonbirdw.clear();
    int n;
    int ha = -1, hb = -1, hc = -1, hd = -1;
    int wa = -1, wb = -1, wc = -1, wd = -1;
    cin >> n;
    REP(i,n) {
        int h, w;
        string x;
        bool flag = true;
        cin >> h >> w >> x;
        if (x == "NOT") {
            flag = false;
            cin >> x;
        }
        if (flag) {
            birdh.push_back(h);
            birdw.push_back(w);
        } else {
            nonbirdh.push_back(h);
            nonbirdw.push_back(w);
        }
    }
    REP(i,birdh.size()) {
        if (hb == -1) {
            hb = hc = birdh[i];
            wb = wc = birdw[i];
        } else {
            hb = min(hb, birdh[i]);
            hc = max(hc, birdh[i]);
            wb = min(wb, birdw[i]);
            wc = max(wc, birdw[i]);
        }
    }
    if (hb == -1) {
        int m;
        cin >> m;
        REP(j,m) {
            int hh, ww;
            bool mark = true;
            cin >> hh >> ww;
            REP(k,nonbirdh.size()) {
                if (hh == nonbirdh[k] && ww == nonbirdw[k]) {
                    mark = false;
                    break;
                }
            }
            if (!mark) cout << "NOT BIRD" << endl;
            else cout << "UNKNOWN" << endl;
        }
        return;
    }

    /*ha = -MAXN, hd = MAXN;
    wa = -MAXN, wd = MAXN;
    REP(j,nonbirdh.size()) {
        if (nonbirdh[j] < hb) {
            ha = max(ha, nonbirdh[j]);
        } else if (nonbirdh[j] > hd) {
            hd = min(hd, nonbirdh[j]);
        }

        if (nonbirdw[j] < wb) {
            if (wa == -1) wa = nonbirdw[j];
            else wa = max(wa, nonbirdw[j]);
        } else if (nonbirdw[j] > wc) {
            if (wd == -1) wd = nonbirdw[j];
            else wd = min(wd, nonbirdw[j]);
        }
    }*/

    int m;
    cin >> m;
    REP(j,m) {
        int hh, ww;
        bool mark = true;
        cin >> hh >> ww;

        int thb, thc, twb, twc;
        if (hh >= hb && hh <= hc && ww >= wb && ww <= wc) cout << "BIRD" << endl;
        else {
            bool fl = true;
            thb = min(hb, hh);
            thc = max(hc, hh);
            twb = min(wb, ww);
            twc = max(wc, ww);

            REP(ii,nonbirdh.size()) {
                if (nonbirdh[ii] >= thb && nonbirdh[ii] <= thc && nonbirdw[ii] >= twb && nonbirdw[ii] <= twc) {
                    fl = false;
                    break;
                }
            }
            if (fl) cout << "UNKNOWN" << endl;
            else cout << "NOT BIRD" << endl;
        }

        /*if (hh >= hb && hh <= hc && ww >= wb && ww <= wc) cout << "BIRD" << endl;
        else if ((hh >= hb && hh <= hc && (ww <= wa || ww >= wd)) || (ww >= wb && ww <= wc && (hh <= ha || hh >= hd))) cout << "NOT BIRD" << endl;
        else cout << "UNKNOWN" << endl;*/
    }
}

int main() {
    int kase;
    cin >> kase;
    FOR(k,1,kase) {
        cout << "Case #" << k << ":" << endl;
        run();
    }
}
