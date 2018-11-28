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

struct TSP {
    int a, b, c; 
    int t, s, p; 
    bool operator <(const TSP& rhs) const { return t < rhs.t || t==rhs.t && s < rhs.s || s==rhs.s && p < rhs.p; }
};
std::set<TSP> tsps;

const int db = 0;
int N, S, nS, P;
int ti[100];
TSP tsis[100][2];
int ppp[100][2];
int ps[100];

int rec(int i, int ns) {
    if (db) {
        printf("rec(i=%d,ns=%d): ", i, ns);
        FZ(k,N) printf("%d ", ps[k]);
        printf("");
        printf("\n");
    }
    if (ns == S) {
        int rv = 0;
        FZ(j,N) if (ps[j] >= P) ++rv;
        return rv;
    }
    if (S-ns <= N-i) {
        int rv = 0;
        FO(j,i,N) {
            ps[j] = ppp[j][1];
            int can = rec(j+1, ns+1);
            if (can > rv) rv = can;
            ps[j] = ppp[j][0];
        }
        return rv;
    }
    return 0;
}

void run(int casenum) {
    printf("Case #%d: ", casenum);
    
    FZ(i,100) FZ(j,2) ppp[i][j] = -1;
    N = rdi();
    S = rdi();
    P = rdi();
    nS = 0;
    FZ(i,N) { 
        ti[i] = rdi();

        int hs = 0;
        FZ(j,4) tsis[i][j].s = -1;
        //if (db) printf("ti=%d : ", ti[i]);
        int c = 0;
        for (auto it = tsps.begin(); it != tsps.end(); ++it) {
            if (it->t == ti[i]) {
                ppp[i][it->s] = it->p;
                if (it->s) hs = 1;
                tsis[i][c] = *it;
                ++c;
                if (c > 2) abort();
                //if (db) printf("(s=%d p=%d %d-%d-%d) ", it->s, it->p, it->a, it->b, it->c);
            }
        }
        if (hs) ++nS;
        //if (db) printf("\n");
        if (db) printf("ppp[%d] = %d %d\n", i, ppp[i][0], ppp[i][1]);
    }

    if (nS < S) printf("0");
    else {
        FZ(i,N) ps[i] = ppp[i][0];
        printf("%d", rec(0, 0));
    }

    printf("\n");
}

int main() {
    FE(a,0,10) FE(b,0,10) FE(c,0,10) {
        if (abs(a-b)>2 || abs(b-c)>2 || abs(a-c)>2) continue;
        TSP v = { a, b, c, a+b+c, abs(a-b)==2 || abs(b-c)==2 || abs(a-c)==2, std::max(c, std::max(a,b)) };
        tsps.insert(v);
    }

    FE(i,1,rdi()) run(i);
}
