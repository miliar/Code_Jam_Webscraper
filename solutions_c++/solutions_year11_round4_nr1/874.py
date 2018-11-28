#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <iomanip>
#include <cmath>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

#define BIG
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define FOR(i, s, n) for (int i = (s) ; i < (n) ; i ++)

#define eps 1e-13
#define le(a, b) ((a) < (b) + eps)

#ifdef BIG
ifstream in("A-large.in") ;
ofstream out("A-large.out") ;
#endif

#ifndef BIG
ifstream in("A-small.in") ;
ofstream out("A-small.out") ;
#endif

typedef long long i64 ;
typedef long double d64 ;
typedef pair<int, int> pint ;
typedef pair<d64, d64> pdouble ;

int N ;
d64 X, B, E, S, R, t, total, w ;
vector<pdouble> v ;

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        in >> X >> S >> R >> t >> N ;
        v.clear() ;
        total = 0 ;
        REP(i, N) { in >> B >> E >> w ; v.push_back(pdouble(w, E - B)) ; total += E - B ; }
        v.push_back(pdouble(0.0, X - total)) ;
        sort(v.begin(), v.end()) ;
        double res = 0.0 ;
        for (int i = 0 ; i < v.size() ; i ++) {
            if (t > eps) {
                double pt = v [i].second / (R + v [i].first) ;
                if (le(pt, t)) {
                    res += pt ; t -= pt ;
                }
                else {
                    res += t + (v [i].second - (R + v [i].first) * t) / (S + v [i].first) ;
                    t = 0.0 ;
                }
            }
            else {
                res += v [i].second / (S + v [i].first) ;
            }
        }
        out << "Case #" << test << ": " << fixed << setprecision(10) << res << endl ;
    }
    in.close() ;
    out.close() ;

    return 0;
}
