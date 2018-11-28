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

//#define BIG
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
ofstream out("B-large.out") ;
#endif

#ifndef BIG
ifstream in("B-small.in") ;
ofstream out("B-small.out") ;
#endif

#define MAXR 1024
#define MAXC 1024

typedef long long i64 ;
typedef long double d64 ;
typedef vector<int> vi ;


#define LBIT(x) ((x) & -(x))

typedef long long TC ;

int nr, nc ;
TC D, v [MAXR] [MAXR], table [3] [2 * MAXR + 1] [2 * MAXR + 1] ;
string sheet [MAXR] ;

void update(int t, int x, int y, TC value) {
    x ++ ; y ++ ;
    for ( ; x < MAXR ; x += LBIT(x))
        for ( int iy = y ; iy < MAXR ; iy += LBIT(iy))
            table [t] [x] [iy] += value ;
}

TC query(int t, int x, int y) {
    x ++ ; y ++ ;
    TC ret = 0;
    for ( ; x > 0; x -= LBIT(x))
        for (int iy = y ; iy > 0 ; iy -= LBIT(iy))
            ret += table [t] [x][iy] ;
    return ret ;
}

TC query(int t, int sr, int sc, int fr, int fc) {
    return query(t, fr, fc) - query(t, sr - 1, fc) - query(t, fr, sc - 1)
            + query(t, sr - 1, sc - 1) ;
}

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        in >> nr >> nc >> D ;
        REP(ir, nr) in >> sheet [ir] ;
        REP(ir, nr) REP(ic, nc) v [ir] [ic] = D + (int) (sheet [ir] [ic] - '0') ;
        memset(table, 0, sizeof(table)) ;
        REP(ir, nr) REP(ic, nc) update(0, ir, ic, v [ir] [ic] + 0) ;
        REP(ir, nr) REP(ic, nc) update(1, ir, ic, ir * (v [ir] [ic] + 0)) ;
        REP(ir, nr) REP(ic, nc) update(2, ir, ic, ic * (v [ir] [ic] + 0)) ;
        
        int K = MIN(nr, nc) ;
        bool found = false ;
        for ( ; K >= 3 && !found ; K --) {
            for (int sr = 0 ; sr + K - 1 < nr && !found ; sr ++) {
                for (int sc = 0 ; sc + K - 1 < nc && !found ; sc ++) {
                    int fr = sr + K - 1, fc = sc + K - 1 ;
                    double mr = 0.5 * (sr + fr), mc = 0.5 * (sc + fc) ;
                    TC mass = query(0, sr, sc, fr, fc) ;
                    TC massR = query(1, sr, sc, fr, fc) ;
                    TC massC = query(2, sr, sc, fr, fc) ;
                    for (int dr = 0 ; dr <= K - 1 ; dr += K - 1)
                        for (int dc = 0 ; dc <= K - 1 ; dc += K - 1) {
                            int pr = sr + dr, pc = sc + dc ;
                            mass -= v [pr] [pc] ;
                            massR -= pr * v [pr] [pc] ;
                            massC -= pc * v [pr] [pc] ;
                        }
                    
                    double xr = 1.0 * massR / mass, xc = 1.0 * massC / mass ;
                    if (eq(mr, xr) && eq(mc, xc)) {
//                        out << sr << " " << sc << " " << K << endl ;
//                        out << mass << " " << massR << " " << massC << endl ;
                        found = true ;
                    }
                }
            }
            if (found) break ;
        }
        out << "Case #" << test << ": " ;
        if (K < 3) out << "IMPOSSIBLE" << endl ;
        else out << K << endl ;
        
    }
    
    in.close() ;
    out.close() ;
    
    return 0;
}

/*

void init (int sz)
}
for (size = 1; size < sz; size <<= 1)
;
{
int sum (int x1, int y1, int x2, int y2) {
    int res, ix1, ix2, iy1, iy2;
    res = 0;
    for(iy2 = y2+1; iy2 > y1; iy2 -= LOW_BIT(iy2)) {
        for (ix2 = x2+1; ix2 > x1; ix2 -= LOW_BIT(ix2))
            res += table[ix2-1][iy2-1];
        for (ix1 = x1; ix1 > ix2; ix1 -= LOW_BIT(ix1))
            res -= table[ix1-1][iy2-1];
    }

    for(iy1 = y1; iy1 > iy2; iy1 -= LOW_BIT(iy1)) {
        for (ix2 = x2+1; ix2 > x1; ix2 -= LOW_BIT(ix2))
            res -= table[ix2-1][iy1-1];
        for (ix1 = x1; ix1 > ix2; ix1 -= LOW_BIT(ix1))
            res += table[ix1-1][iy1-1];
    }
    return res ;
}

void update (int x, int y, int amount) {
    int ix;
    x++; y++;
    for(; y <= size; y += LOW_BIT(y)) {
        for(ix = x; ix <= size; ix += LOW_BIT(ix))
            table[ix-1][y-1] += amount;
}

void update(int t, int r, int c, int value) {
	int tmpC ;
	while (r <= MAXR) {
		tmpC = c ;
		while (tmpC <= MAXC){
			table [t] [r] [tmpC] += value ;
			tmpC += (tmpC & -tmpC) ;
		}
		r += (r & -r) ;
	}
}
int query( int x1, int y1, int x2, int y2 ) {
    return sum( x2, y2 ) -
           sum( x1 - 1, y2 ) - sum( x2, y1 - 1 ) +
           sum( x1 - 1, y1 - 1 );
}

*/
