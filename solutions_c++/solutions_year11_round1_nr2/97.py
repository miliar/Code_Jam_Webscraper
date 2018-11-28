#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <iterator>
#include <utility>
#include <algorithm>
#include <numeric>
#include <functional>
#include <complex>

using namespace std;

#define fi first
#define se second
#define sz size()
#define pb push_back
#define ins insert
#define clr clear()
#define FOR(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define FORE(i,a,b) for(typeof(a) i=(a);i<=(b);i++)
#define EACH(it,A) for(typeof(A.begin()) it=A.begin(); it!=A.end(); it++)
#define ALL(A) A.begin(), A.end()
#define REP(i,n) for(typeof(n) i=0;i<(n);i++)
#define REP1(i,n) for(typeof(n) i=1;i<=(n);i++)

typedef vector<int> VI;
typedef pair<int,int> ip;
typedef long long ll;
typedef vector<ip> VP;
typedef vector<string> VS;

VS D;
set<ll> H;

ll enc(string w) {
    ll b = 0;
    REP(i,w.sz) {
        b *= 30;
        if(w[i] == '*') b += 27;
        else b += 1 + (w[i] - 'a');
    }
    return b;
}

void do_case(int cn) {
    int N, M;
    cin >> N >> M;
    D.clear();
    D.resize(N);
    REP(i,N) cin >> D[i];
    cout << "Case #" << cn << ":";
    REP(it,M) {
        string d;
        cin >> d;
        H.clr;
        REP(i,N) {
            int n = D[i].sz;
            string b(n,'*');
            REP(j,26) {
                REP(k,n) if(D[i][k] == d[j]) {
                    b[k] = d[j];
                    H.ins(enc(b));
                }
            }
        }
        int ma = -1;
        string res = "zzzzzzzzzzz";
        REP(i,N) {
            int s = 0;
            string g(D[i].sz,'*');
            REP(j,26) {
                bool found = false;
                REP(p,g.sz) if(g[p] == '*') {
                    g[p] = d[j];
                    if(H.find(enc(g)) != H.end()) found = true;
                    g[p] = '*';
                    if(found) break;
                }
                if(found) {
                    bool updates = false;
                    REP(p,g.sz) if(D[i][p] == d[j]) {
                        updates = true;
                        g[p] = d[j];
                    }
                    if(!updates) s++;
                }
            }
            assert(g == D[i]);
            if(s > ma) {
                ma = s;
                res = D[i];
            }
        }
        cout << " " << res;
    }
    cout << endl;
}

#define fname "B-large"

int main() {
    freopen(fname ".in", "r", stdin);
    freopen(fname ".out", "w", stdout);
    int T;
    cin >> T;
    REP1(it,T) do_case(it);
    return 0;
}
