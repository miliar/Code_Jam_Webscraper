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

int mat[10][10];
int mas[10][10];
int tmp[10][10];

int n, m;

void run() {
    memset(mat, 0, sizeof(mat));
    memset(mas, 0, sizeof(mas));
    cin >> n;
    REP(i,n-1) {
        int a, b;
        cin >> a >> b;
        --a; --b;
        mat[a][b] = mat[b][a] = 1;
    }
    cin >> m;
    REP(i,m-1) {
        int a, b;
        cin >> a >> b;
        --a; --b;
        mas[a][b] = mas[b][a] = 1;
    }

    vector<int> mm;
    REP(i,n) mm.push_back(i);

    vector<int> aa;
    REP(i,m) {
        int s = 0;
        REP(j,m) {
            if (mas[i][j] == 1) ++s;
        }
        aa.push_back(s);
    }
    sort(aa.begin(), aa.end());

    do {
        memset(tmp, 0, sizeof(tmp));
        REP(i,m) {
            REP(j,m) {
                int ta = mm[i], tb = mm[j];
                if (mat[ta][tb] == 1) tmp[i][j] = 1;
            }
        }
        vector<int> bb;
        REP(i,m) {
            int s = 0;
            REP(j,m) {
                if (tmp[i][j] == 1) ++s;
            }
            bb.push_back(s);
        }
        sort(bb.begin(), bb.end());

        bool fl = true;
        REP(i,m) {
            if (aa[i] != bb[i]) {
                fl = false;
                break;
            }
        }
        if (fl) {
            cout << "YES" << endl;
            return;
        }
    } while (next_permutation(mm.begin(), mm.end()));
    cout << "NO" << endl;
}

int main() {
    int kase;
    cin >> kase;
    FOR(k,1,kase) {
        cout << "Case #" << k << ": ";
        run();
    }
}
