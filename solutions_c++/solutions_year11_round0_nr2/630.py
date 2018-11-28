#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <map>

using namespace std;

#define BIG
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#ifdef BIG
ifstream in("B-large.in") ;
ofstream out("B-large.out") ;
#endif

#ifndef BIG
ifstream in("B-small.in") ;
ofstream out("B-small.out") ;
#endif

#define MAXN 1005

typedef long double LD ;

map<string, char> b2c ;
map<string, int> op ;

int main() {
    int numTests ;
    in >> numTests ;
    for (int test = 1 ; test <= numTests ; test ++) {
        int numBasic, numOpposed, n ;
        string s, start ;
        
        b2c.clear() ;
        op.clear() ;
        in >> numBasic ;
        for (int i = 0 ; i < numBasic ; i ++) {
            in >> s ;
            b2c [string(1, s [0]) + string(1, s [1])] = s [2] ;
            b2c [string(1, s [1]) + string(1, s [0])] = s [2] ;
        }
        
        in >> numOpposed ;
        for (int i = 0 ; i < numOpposed ; i ++) {
            in >> s ;
            op [s] = 1 ; op [string(1, s [1]) + string(1, s [0])] = 1 ;
        }
        
        in >> n >> start ;
        string res = string(1, start [0]) ;
        for (int i = 1 ; i < start.size() ; i ++) {
            res += start [i] ;
            if (res.size() >= 2) {
                int lng = res.size() ;
                string last = string(1, res [lng - 2]) + string(1, res [lng - 1]) ;
                if (b2c [last]) {
                    res [lng - 2] = b2c [last] ;
                    res.resize(lng - 1) ;
                }
            }
            for (int j = 0 ; j < res.size() ; j ++)
                for (int k = j + 1 ; k < res.size() ; k ++)
                    if (op [string(1, res [j]) + string(1, res [k])] == 1) { res = "" ; break ; }
        }
        string ret = "[" ;
        if (res.size() > 0) {
            ret += string(1, res [0]) ;
            for (int i = 1 ; i < res.size() ; i ++) ret += ", " + string(1, res [i]) ;
        }
        ret += "]" ;
        out << "Case #" << test << ": " << ret << endl ;
    }
    in.close() ;
    out.close() ;
    
    return 0;
}
