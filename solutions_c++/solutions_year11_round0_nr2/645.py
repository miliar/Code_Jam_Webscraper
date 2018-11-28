#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <deque>
#include <iomanip>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;

#define rep(i, b, n) for(int i=(b); i<(n); ++i)
#define repd(i, b, n) for(int i=(b); i>(n); --i)
#define trav(it, col) for(typeof((col).begin()) it = (col).begin(); it != (col).end(); ++it)
#define clr(pt) memset((pt), 0, sizeof(pt))
#define EPS 1e-8
#define IFD if(DEBUG)
#define dbg(x) DEBUG && cerr << __LINE__ << ": " << x << endl
#define DL cerr << __LINE__ << endl;
#define mp make_pair 

#define DEBUG true

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<double, double> pdd;
typedef stringstream ss;

int INMODE = 0; // 0 specify cases, 1 single run, 2 indefinite runs

bool solve(int cn){
    map<pair<char,char>,char> comb;
    set<pair<char,char> > del;

    int c,d,n;
    cin >> c;

    rep(i,0,c) {
        string s;
        cin >> s;
        comb.insert(mp(mp(s[0], s[1]), s[2]));
        comb.insert(mp(mp(s[1], s[0]), s[2]));
    }

    cin >> d;
    rep(i,0,d) {
        string s;
        cin >> s;
        del.insert(mp(s[0],s[1]));
        del.insert(mp(s[1],s[0]));
    }

    string list, final;
    cin >> n;
    cin >> list;

    final += list[0];
    int j = 0;
    rep(i,1,n+1) {
        j++;
        final += list[i];

        if(comb.count(mp(final[j-1], final[j]))) {
            //dbg("Comb " << final << " " << list[j-1] << " " << list[j]);
            final += comb[mp(final[j-1], final[j])];
            final.erase(j-1,2);
            j--;
            //dbg("  ---> " << final);
        }

        rep(x,0,j+1) {
            rep(y,x+1,j+1) {
                if(del.count(mp(final[x], final[y]))) {
                    //dbg("Kill " << final);
                    final.clear();
                    j = -1;
                }
            }
        }
    }

    cout << "Case #" << cn << ": [";
    rep(i,0,j) {
        if(i) cout << ", ";
        cout << final[i];
    }
    cout << "]" << endl;

    return 1;
}

int main(){
    //cout << setiosflags(ios::fixed) << setprecision(10);
    int cases = 1 << 30;
    if(INMODE == 0) cin >> cases;
    if(INMODE == 1) cases = 1;
    for(int cn = 1; cn <= cases; ++cn)
        if(!solve(cn) && INMODE == 2) break;
    return 0;
}
