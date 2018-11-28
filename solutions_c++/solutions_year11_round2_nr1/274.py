#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;

#define BIG
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define FOR(i, s, n) for (int i = (s) ; i < (n) ; i ++)

#ifdef BIG
ifstream in("A-large.in") ;
ofstream out("A-large.out") ;
#endif

#ifndef BIG
ifstream in("A-small.in") ;
ofstream out("A-small.out") ;
#endif

#define MAXN 105
#define WP(nwin, nplayed) ((nplayed) > 0 ? 1.0 * (nwin) / (nplayed) : 0.0)
typedef long long i64 ;

string score [MAXN] ;
int n, win [MAXN], played [MAXN], NOP [MAXN] ;
double RPI [MAXN], OWP [MAXN], OOWP [MAXN] ;

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        in >> n ;
        REP(i, n) in >> score [i] ;
        REP(i, n) {
            played [i] = 0 ; win [i] = 0 ;
            REP(j, n)
                if (score [i] [j] != '.') {
                    played [i] ++ ;
                    if (score [i] [j] == '1') win [i] ++ ;
                }
        }
        REP(i, n) {
            RPI [i] = 0.25 * WP(win [i], played [i]) ;
            OWP [i] = 0.0 ;
            NOP [i] = 0 ;
            REP(j, n) if (j != i) {
                if (score [j] [i] != '.') {
                    NOP [i] ++ ;
                    if (score [j] [i] == '1') OWP [i] += WP(win [j] - 1, played [j] - 1) ;
                    else OWP [i] += WP(win [j], played [j] - 1) ;
                }
            }
            OWP [i] = (NOP [i] == 0) ? 0.0 : OWP [i] / NOP [i] ;
            RPI [i] += 0.50 * OWP [i] ;
        }
        REP(i, n) {
            OOWP [i] = 0.0 ;
            REP(j, n)
                if (j != i && score [j] [i] != '.')
                    OOWP [i] += (NOP [i] == 0) ? 0.0 : OWP [j] / NOP [i] ;
            RPI [i] += 0.25 * OOWP [i] ;
        }
        out << "Case #" << test << ": " << endl ;
        REP(i, n) out << fixed << setprecision(12) << RPI [i] << endl ;
    }
    in.close() ;
    out.close() ;

    return 0;
}
