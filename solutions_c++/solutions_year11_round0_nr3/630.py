#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

#define BIG
#define MAXN 100005
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#ifdef BIG
ifstream in("C-large.in") ;
ofstream out("C-large.out") ;
#endif

#ifndef BIG
ifstream in("C-small.in") ;
ofstream out("C-small.out") ;
#endif

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        int n, sum = 0, xorSum = 0, minNumber = 1000000000 ;
        in >> n ;
        for (int i = 0 ; i < n ; i ++) {
            int cur ;
            in >> cur ;
            sum += cur ; xorSum ^= cur ;
            minNumber = MIN(minNumber, cur) ;
        }
        out << "Case #" << test << ": " ;
        if (xorSum != 0) out << "NO" << endl ;
        else out << (sum - minNumber) << endl ;
    }
    in.close() ;
    out.close() ;
    
    return 0;
}
