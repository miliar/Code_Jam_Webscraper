#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

#define BIG
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#ifdef BIG
ifstream in("D-large.in") ;
ofstream out("D-large.out") ;
#endif

#ifndef BIG
ifstream in("D-small.in") ;
ofstream out("D-small.out") ;
#endif

#define MAXN 1005

typedef long double LD ;

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        int n ;
        in >> n ;
        int correct = 0, cur ;
        for (int i = 1 ; i <= n ; i ++) {
            in >> cur ;
            if (cur == i) correct ++ ;
        }
        out << "Case #" << test << ": " << (n - correct) << endl ;
    }
    in.close() ;
    out.close() ;
    
    return 0;
}
