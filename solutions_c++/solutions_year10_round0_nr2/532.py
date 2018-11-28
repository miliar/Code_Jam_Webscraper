#include <string>
#include <cstring>
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
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////


LL nwd(LL a, LL b) {
    LL d = 1;
    while (a && b) {
        if (!(a&1) && !(b&1))
            a >>= 1,
            b >>= 1,
            d <<= 1;
        else
        if (!(a&1))
            a >>= 1;
        else
        if (!(b&1))
            b >>= 1;
        else
        if (a>b)
            a -= b;
        else
            b -= a;
    }
    return (a|b)*d;
}

LL N, NWD, cur, first;

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        NWD = 0;
        scanf("%Ld", &N);
        scanf("%Ld", &first);
        REP(a, N-1) {
            scanf("%Ld", &cur);
            NWD = nwd(abs(first-cur), NWD);
//            printf("%Ld ---> %Ld ---> %Ld\n", cur, abs(first-cur), NWD);
        }
        printf("Case #%d: %Ld\n", tt+1, (NWD-cur%NWD)%NWD);
    }
}


