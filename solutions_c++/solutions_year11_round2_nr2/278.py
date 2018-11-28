#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <iomanip>

using namespace std;

#define BIG
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define FOR(i, s, n) for (int i = (s) ; i < (n) ; i ++)

#define eps 1e-9
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps)
#define gr(a, b) ((a) > (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)

#ifdef BIG
ifstream in("B-large.in") ;
ofstream out("B-largeb.out") ;
#endif

#ifndef BIG
ifstream in("B-small.in") ;
ofstream out("B-small.out") ;
#endif


typedef long long i64 ;
typedef long double d64 ;
typedef vector<int> vi ;

#define MAXC 205
i64 c, v [MAXC] ;
d64 T, minD, p [MAXC] ;

bool check(d64 T) {
    d64 minX = -1e20, nextX ;
    REP(i, c) {
        if (gr(p [i] - T - minD, minX)) {
            nextX = p [i] - T + (v [i] - 1) * minD ;
            if (gr(nextX - p [i], T)) return false ;
            minX = nextX ;
        }
        else {
            nextX = minX + minD + (v [i] - 1) * minD ;
            if (gr(nextX - p [i], T)) return false ;
            minX = nextX ;
        }
    }
    return true ;
}

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        in >> c >> minD ;
        cout << "Case #" << test << ": " << c << " " << minD << endl  ;
        REP(i, c) in >> p [i] >> v [i] ;
        d64 lowT = 0.0, highT = 1e18 ;
        for (int step = 0 ; step < 1000 ; step ++) {
            T = 0.5 * (lowT + highT) ;
//            out << lowT << " " << T << " " << highT << " " << (highT - lowT) << endl ;
            if (check(T)) highT = T ;
            else lowT = T ;
        }
        out << "Case #" << test << ": " << fixed << setprecision(10) << T << endl ;
        
    }
    
    in.close() ;
    out.close() ;
    cin >> numTests ;
    
    return 0;
}
