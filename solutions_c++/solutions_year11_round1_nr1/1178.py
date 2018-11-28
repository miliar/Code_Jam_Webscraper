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

typedef long long i64 ;

i64 mcd(i64 a, i64 b) { if (b == 0) return a ; else return mcd(b, a % b) ; }

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        i64 n, pd, pg ;
        out << "Case #" << test << ": " ;
        in >> n >> pd >> pg ;
        if (pd < 100 && pg == 100) { out << "Broken" << endl ; continue ; }
        if (pd == 100 && pg == 100) { out << "Possible" << endl ; continue ; }
        if (pd == 0) { out << "Possible" << endl ; continue ; }
        if (pd > 0 && pg == 0) { out << "Broken" << endl ; continue ; }
        
        i64 k = mcd(pd, 100) ;
        if ((100 / k) <= n) out << "Possible" << endl ;
        else out << "Broken" << endl ;
    }

    in.close() ;
    out.close() ;

    return 0;
}
