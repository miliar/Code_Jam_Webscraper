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
#define se second.first
#define th second.second
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

vector< pair< double, pair< double, double > > > A;

void do_case(int cn) {
    double X, S, R, t;
    cin >> X >> S >> R >> t;
    int N;
    cin >> N;
    A.clear();
    A.resize(N);
    REP(i,N) cin >> A[i].se >> A[i].th >> A[i].fi;
    sort(ALL(A));
    double rem = X;
    REP(i,N) rem -= A[i].th - A[i].se;
    double res = 0;
    if(t - (rem / R) > 1e-9) {
        res += rem/R;
        t -= rem/R;
    } else {
        res += t;
        res += (rem - (R*t)) / S;
        t = 0;
    }
    REP(i,N) {
        double rs = A[i].fi+R, ss = A[i].fi+S, di = A[i].th-A[i].se;
        if(t - (di / rs) > 1e-9) {
            res += di/rs;
            t -= di/rs;
        } else {
            res += t;
            res += (di - (rs*t)) / ss;
            t = 0;
        }
    }
    cout << "Case #" << cn << ": " << fixed << setprecision(9) << res << endl;
}

#define fname "A-large"

int main() {
    freopen(fname ".in", "r", stdin);
    freopen(fname ".out", "w", stdout);
    int T;
    cin >> T;
    REP1(it,T) do_case(it);
    return 0;
}
