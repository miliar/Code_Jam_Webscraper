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
ifstream in("A-large.in") ;
ofstream out("A-large.out") ;
#endif

#ifndef BIG
ifstream in("A-small.in") ;
ofstream out("A-small.out") ;
#endif

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        int n, lastO = 0, lastB = 0, posO = 1, posB = 1, T = 0, moves ;
        in >> n ;
        for (int j = 0 ; j < n ; j ++) {
            string s ; int button ;
            in >> s >> button ;
            if (s == "O") {
                moves = ABS(posO - button) + 1 ;
                if (lastO + moves <= T) {
                    T ++ ;
                    lastO = T ;
                }
                else {
                    T = lastO + moves ;
                    lastO = T ;
                }
                posO = button ;
            } else {
                moves = ABS(posB - button) + 1 ;
                if (lastB + moves <= T) {
                    T ++ ;
                    lastB = T ;
                }
                else {
                    T = lastB + moves ;
                    lastB = T ;
                }
                posB = button ;
            }
        }
        
        out << "Case #" << test << ": " << T << endl ;
    }
    in.close() ;
    out.close() ;
    
    return 0;
}
