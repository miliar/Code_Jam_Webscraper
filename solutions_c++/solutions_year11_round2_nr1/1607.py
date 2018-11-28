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
    int n;
    scanf("%d", &n);

    double WP[n];
    double OWPS[n];
    double OOWPS[n];
    int MATCH[n][n];
    int wins[n];
    int losses[n];
    int matches[n];
    rep(i,0,n) WP[i] = 0;
    rep(i,0,n) OWPS[i] = 0;
    rep(i,0,n) OOWPS[i] = 0;
    clr(MATCH);
    clr(wins);
    clr(losses);
    clr(matches);

    rep(i,0,n) rep(j,0,n) {
        char in;
        scanf(" %c", &in);
        if(in == '1') {
            MATCH[i][j] = 1;
            wins[i]++;
            matches[i]++;
        }
        else if(in == '0') {
            MATCH[i][j] = -1;
            losses[i]++;
            matches[i]++;
        }
    }

    rep(i,0,n) {
        WP[i] = (0.0 + wins[i]) / matches[i];
        rep(j,0,n) {
            if(MATCH[i][j]) {
                int win = MATCH[j][i] == 1 ? 1 : 0;
                OWPS[i] += (0.0 + wins[j] - win) / (matches[j] - 1);
            }
        }
        OWPS[i] /= matches[i];
    }

    rep(i,0,n) {
        rep(j,0,n) {
            if(MATCH[i][j]) {
                OOWPS[i] += OWPS[j];
            }
        }
        OOWPS[i] /= matches[i];
    }

    printf("Case #%d:\n", cn);
    rep(i,0,n) {
        printf("%.10f\n", 0.25 * WP[i] + 0.5 * OWPS[i] + 0.25 * OOWPS[i]);
    }

    return 1;
}

int main(){
    cout << setiosflags(ios::fixed) << setprecision(10);
    int cases = 1 << 30;
    if(INMODE == 0) cin >> cases;
    if(INMODE == 1) cases = 1;
    for(int cn = 1; cn <= cases; ++cn)
        if(!solve(cn) && INMODE == 2) break;
    return 0;
}
