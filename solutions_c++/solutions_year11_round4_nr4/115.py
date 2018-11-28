#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <utility>
#include <complex>
#include <list>
#include <sstream>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <iomanip>
using namespace std;


template<class T>inline T iabs(const T& v) {return v<0 ? -v : v;}
template<class T>inline T strTo(string s){istringstream is(s);T v;is>>v;return v;}
template<class T>inline string toStr(const T& v){ostringstream os;os<<v;return os.str();}
template<class T>inline int cMin(T& a, const T& b){return b<a?a=b,1:0;}
template<class T>inline int cMax(T& a, const T& b){return a<b?a=b,1:0;}
template<class T>inline int cBit(T n){return n?cBit(n&(n-1))+1:0;}
template<class T>inline int cntbit(T n) {int c=0;for(;n; n&=n-1)++c;return c;}


#define DEBUG(a)     printf("%s = %s\n", #a, toStr(a).c_str())

#define two(i)       (1ULL<<(i))
#define two64(i)     (1LL<<(i))
#define contain(s,i) (((s)>>(i))&1)
#define testBit(s,i) (((s)>>(i))&1)
#define setBit(s, i) (s |= two(i))
#define unSetBit(s,i) (s &= ~two(i))
#define MP(a,b)      make_pair(a,b)
#define CLR(arr,v)   memset(arr, v, sizeof(arr))
#define FOR(i,s,e)   for(int i(s),__(e); i<=__; ++i)
#define FORD(i,s,e)  for(int i(s),__(e); i>=__; ++i)
#define REP(i,n)     for(int i(0),__(n); i< __; ++i)
#define REPD(i,n)    for(int i((n)-1);   i>= 0; --i)

typedef int                 i32;
typedef unsigned int        u32;
typedef long long           i64;
typedef unsigned long long  u64;
typedef pair<int,int>       PII;
typedef vector<int>         VI;
typedef vector<string>      VS;

const int NN  = 416;
const int MM = 13;
int  N, E, BitLen;
int  adj[NN][NN], deg[NN];
u64  AdjMask[NN];
int  dist[NN],  Maskdeg[NN];
u64  Mask[NN][NN];
set<u64>  tMask[NN];
typedef set<u64>::iterator iter_t;

int  cntBit(int A[]) {
    int  cnt=0; REP(i, BitLen) cnt += cntbit(A[i]);
    return cnt;
}

void Add(int dst[], int src[]) {
    REP(i, BitLen) dst[i] |= src[i];
}

int  Q[1<<20], Qs, Qe;

int  Ans1, Ans2;

void  solve() {
    Qs = Qe = 0;
    CLR(dist, 0x3f);
    REP(i, N) tMask[i].clear();
    dist[0] = 0;
    Q[Qe++] = 0;
    tMask[0].insert(0ULL);
    while(Qs != Qe) {
        int  u = Q[Qs++];
        //printf("u = %d\n", u);
        REP(i, deg[u]) {
            int  v = adj[u][i];
            if(dist[v] < dist[u] + 1) continue;
            if(dist[v] == dist[u] + 1) {
                //int *p=Mask[v][Maskdeg[v]];
                for(iter_t it = tMask[u].begin(); it!=tMask[u].end(); ++it) {
                    tMask[v].insert(*it | AdjMask[u]);
                }
                continue;
            }
            dist[v] = dist[u] + 1;
            tMask[v].clear();
            for(iter_t it = tMask[u].begin(); it!=tMask[u].end(); ++it) {
                tMask[v].insert(*it | AdjMask[u]);
            }
            Q[Qe++] = v;
        }
    }
    Ans1 = dist[1] - 1;
    Ans2 = 0;
    for(iter_t it = tMask[1].begin(); it!=tMask[1].end(); ++it) {
        int  t = cntbit(*it) - Ans1;
        if(t > Ans2) Ans2 = t;
    }
}

int main(int argc, char* argv[]) {
    int  testcase;
    freopen("D-small-attempt0.in" , "r", stdin);
    freopen("output.out" , "w", stdout);
    scanf("%d", &testcase);
    FOR(it, 1, testcase) {
        scanf("%d%d", &N, &E);
        CLR(deg, 0);
        CLR(AdjMask, 0);
        BitLen = N/32 + ((N&31) ? 1 : 0);
        REP(i, E) {
            int  u, v;
            scanf("%d,%d", &u, &v);
            adj[u][deg[u]++] = v;
            AdjMask[u] |= two(v);
            adj[v][deg[v]++] = u;
            AdjMask[v] |= two(u);
        }
        REP(i, N) AdjMask[i] |= two(i);
        
        solve();
        
        printf("Case #%d: %d %d\n", it, Ans1, Ans2 - 1);
    }
    return 0;
}

