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

#define DEBUG true

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<double, double> pdd;
typedef stringstream ss;

int INMODE = 0; // 0 specify cases, 1 single run, 2 indefinite runs

bool solve(int cn){
    int bp = 1, op = 1, bt = 0, ot = 0, t = 0;
    int n;
    cin >> n;

    rep(i,0,n) {
        char x;
        int b;
        cin >> x >> b;
        if(x == 'O') {
            t += max(1,ot-t + abs(b - op) + 1);
            ot = t;
            op = b;
        }
        if(x == 'B')  { 
            t += max(1,bt-t + abs(b - bp) + 1);
            bt = t;
            bp = b;
        }
    }

    cout << "Case #" << cn << ": " << t << endl;

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
