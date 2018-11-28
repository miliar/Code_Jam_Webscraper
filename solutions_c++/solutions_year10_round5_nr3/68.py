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

#define SIZE 4000100

int tab[SIZE];
set<pii> zb;

void zmien(int poz, int nw) {
    zb.erase(MP(tab[poz], poz));
    tab[poz] = nw;
    zb.insert(MP(tab[poz], poz));
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        int D;
        LL wyn = 0;
        REP(a, SIZE)
            tab[a] = 0;
        scanf("%d", &D);
        REP(a, D) {
            int poz, ile;
            scanf("%d%d", &poz, &ile);
            poz += 2000000;
            tab[poz] = ile;
            zb.insert(MP(ile, poz));
        }
        for (;;) {
            int p = zb.rbegin()->second;
            int i = tab[p];
            if (i<=1)
                break;
            zmien(p, i%2);
            wyn += i/2;
            zmien(p-1, tab[p-1]+i/2);
            zmien(p+1, tab[p+1]+i/2);
        }
        printf("Case #%d: %Ld\n", tt+1, wyn);
    }
}


