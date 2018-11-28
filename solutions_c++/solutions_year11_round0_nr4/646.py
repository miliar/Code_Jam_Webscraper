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
    int n;
    cin >> n;

    double ops[n+1];
    clr(ops);

    // Precalc expected ops for every permutation length
    ops[1] = 0;
    rep(i,2,n+1) {
        double s = 0, sa = 0;
        rep(k,1,i) sa += 1.0/i * (ops[k] + max(ops[i-k] - 1, 0.0));
        // Run alot for convergance (hack?)
        rep(j,0,1000) s = 1 + 1.0/i * s + sa;
        ops[i] = s;
    }

    //rep(i,1,n+1) dbg(i << ": " << ops[i]);

    vi seq(n);
    bool visited[n];
    clr(visited);

    rep(i,0,n) cin >> seq[i];

    // Sum ops for all permutation lengths
    double sum = 0;
    rep(i,0,n) {
        int k = i;
        int len = 0;
        while(!visited[k]) {
            visited[k] = true;
            len++;
            k = seq[k] - 1;
        }
        sum += ops[len];
    }

    cout << "Case #" << cn << ": " << sum << endl;

    return 1;
}

int main(){
    cout << setiosflags(ios::fixed) << setprecision(8);
    int cases = 1 << 30;
    if(INMODE == 0) cin >> cases;
    if(INMODE == 1) cases = 1;
    for(int cn = 1; cn <= cases; ++cn)
        if(!solve(cn) && INMODE == 2) break;
    return 0;
}
