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

int N;
LL L;
int dl[100];

#define X 10000

LL koniec[X+1];

#define DUZO 1000000000*(LL)1000000000*2

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%Ld%d", &L, &N);
        REP(a, N)
            scanf("%d", &dl[a]);
        sort(dl, dl+N);
        REP(a, X+1)
            koniec[a] = (L-a)%dl[N-1] ? DUZO : (L-a)/dl[N-1];
        FORD(k, X, 0)
            REP(a, N)
                if (k+dl[a]<=X)
                    koniec[k] = min(koniec[k], koniec[k+dl[a]]+1);
        printf("Case #%d: ", tt+1);
        if (koniec[0]==DUZO)
            printf("IMPOSSIBLE\n");
        else
            printf("%Ld\n", koniec[0]);
    }
}
