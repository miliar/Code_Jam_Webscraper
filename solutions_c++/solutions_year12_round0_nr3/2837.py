#include <algorithm>  
#include <iostream>  
#include <stdint.h>  
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

int N;
int tps[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000 };

void run(int casenum) {
    printf("Case #%d:", casenum);

    int A = rdi();
    int B = rdi();
    std::set<uint64_t> myass;
    int rv = 0;

    FE(n,A,B) {
        int r = int(ceil(log10(double(n+1))));
        FZ(p,r-1) {
            int a1 = tps[p+1];
            int a2 = tps[r-p-1];
            int m = (n%a1)*a2 + n/a1;
            if (m <= n) continue;
            uint64_t k = ((uint64_t)n << 32) | m;
            if (myass.find(k) == myass.end() && m >= A && m <= B) {
                //printf("n=%d m=%d\n", n, m);
                ++rv;
                myass.insert(k);
            }
        }
    }
/*    for n in range(A, B+1):
        r = int(math.ceil(math.log(n+1,10)))
        if len(set(str(n))) == 1:
            continue
        if time.time() - t > 1:
            t = time.time()
            print(n)
        for p in range(r-1):
            a1 = 10**(p+1)
            a2 = 10**(r-p-1)
            m = (n % a1)*a2 + n//a1
            if m <= n:
                continue
            if ((n,m) not in boo) and (m >= A and m <= B):
                rv += 1
                #print((n,m))
                boo.add((n,m))
    print("Case #%d:" % (i+1), rv)
*/

    printf(" %d\n", rv);
}

int main() {
    FE(i,1,rdi()) run(i);
}
