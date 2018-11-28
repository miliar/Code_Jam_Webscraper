#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <cstdlib>  
#include <string>  
#include <vector>  
#include <cstdio>  
#include <cctype>  
#include <queue>  
#include <cmath>  
#include <list>  
#include <set>  
#include <map>  
using namespace std;

// obscure code contest go

#define _KITTEN(a,b) a##b
#define _CAT(a,b) _KITTEN(a,b)

#define FO(i,a,b) for (int i = (a), _CAT(i,__end)=(b); i < _CAT(i,__end); ++i)
#define FE(i,a,b) for (int i = (a), _CAT(i,__end)=(b); i <= _CAT(i,__end); ++i)
#define FZ(i,n) FO(i,0,n)
#define FI(i,n) FE(i,1,n)

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  

#define FV(i,vec) FZ(i,SZ(vec))
#define FS(i,a,vec) FO(i,a,SZ(vec))

typedef long long lng;

int     rdi() { int x;                      scanf( "%d",    &x ); return x; }
lng     rdl() { lng x;                      scanf( "%lld",  &x ); return x; }
double  rdf() { double x;                   scanf( "%lf",   &x ); return x; }
string  rdw() { static char wbuf[100005];   scanf( "%s", wbuf ); return wbuf; }

#define RDI(N) int N = rdi()
#define RDW(s) scanf( "%s", s )

// wanted
// FSTR - iterate chars until strlen?
// binary printer

int R, C;
char pic[50][50+1];

bool solve() {
    FZ(r,R) {
        FZ(c,C) {
            if (pic[r][c] == '#') {
                if (r == R-1 || pic[r+1][c] != '#') return false;
                if (c == C-1 || pic[r][c+1] != '#') return false;
                if (pic[r+1][c+1] != '#') return false;
                pic[r][c] = '/'; pic[r][c+1] = '\\';
                pic[r+1][c] = '\\'; pic[r+1][c+1] = '/';
            }
        }
    }
    return true;
}

void run(int casenum) {
    printf("Case #%d:\n", casenum);
    R = rdi(); C = rdi();
    FZ(i,R) RDW(pic[i]);
    if (solve()) {
        FZ(r,R) {
            FZ(c,C) printf("%c", pic[r][c]);
            printf("\n");
        }
    } else {
        printf("Impossible\n");
    }
}

int main() {
    FE(i,1,rdi()) run(i);
}
