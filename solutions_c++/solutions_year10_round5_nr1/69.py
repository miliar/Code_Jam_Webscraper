#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(a, b) __typeof(b) a = (b)
#define FOREACH(a, b) for(INIT(a, (b).begin()); a!=(b).end(); ++a)
 
#define PB push_back
#define MP make_pair
 
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;
 
#define INF 1000000000
 
template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

void NWD(int A, int B, LL &xp, LL &yp) {
    if (B==0) {
        xp = 1;
        yp = 0;
        return;
    }
    LL x, y;
    NWD(B, A%B, x, y);
    xp = y;
    yp = x-A/B*xp;
}


int odwr(int A, int P) {
    LL x,y;
    NWD(A, P, x, y);
    x %= P;
    while (x<0)
        x += P;
    return x;
}

int primes[1000000];
int ilep = 0;
int tab[1000001];

int K, inp[20];
int D;
int top;

int main() {
    FOR(p, 2, 1000000)
        if (!tab[p]) {
            primes[ilep++] = p;
            for (int p2 = p*2; p2<=1000000; p2 += p)
                tab[p2] = 1;
        }

    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", tt+1);
        scanf("%d%d", &D, &K);
        REP(a, K)
            scanf("%d", &inp[a]);
        if (K==1 || (K==2 && inp[0]!=inp[1]))
            printf("I don't know.\n");
        else
        if (inp[0]==inp[1])
            printf("%d\n", inp[0]);
        else {
            int next = -1;
            top = 1;
            REP(a, D)
                top *= 10;
            REP(xx, ilep) {
                int P = primes[xx];
                if (P>top)
                    break;
                REP(a, K)
                    if (inp[a]>=P)
                        goto zle;
                {
                int A = (inp[1]-inp[2]+P)*(LL)odwr((inp[0]-inp[1]+P)%P, P)%P;
                int B = (inp[1]-A*(LL)inp[0]+P*(LL)P)%P;
                int w;
                FOR(n, 3, K) {
                    w = (A*(LL)inp[n-1]+B)%P;
                    if (n<K && w!=inp[n])
                        goto zle;
                }
                if (next>=0 && next!=w)
                    goto niewiem;
                next = w;
                }
                zle:;
            }
            printf("%d\n", next);
            continue;
            niewiem:
            printf("I don't know.\n");
        }
    }
}



