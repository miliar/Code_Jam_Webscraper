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

int R, K, N, R0;
int tab[1000];
int zysk[1000];
int ileg[1000];

int p1, p2;
LL z1, z2;

void go() {
        z1 += zysk[p1];
        p1 = (p1+ileg[p1])%N;
        z2 += zysk[p2];
        p2 = (p2+ileg[p2])%N;
        z2 += zysk[p2];
        p2 = (p2+ileg[p2])%N;
        --R;
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d", &R, &K, &N);
        REP(a, N)
            scanf("%d", &tab[a]);
        REP(s, N) {
            if (s && ileg[s-1]) {
                ileg[s] = ileg[s-1]-1;
                zysk[s] = zysk[s-1]-tab[s-1];
            }
            else
                ileg[s] = zysk[s] = 0;
            while (ileg[s]<N && zysk[s]+tab[(s+ileg[s])%N]<=K) {
                zysk[s] += tab[(s+ileg[s])%N];
                ++ileg[s];
            }
        }
        p1 = p2 = 0;
        z1 = z2 = 0;
        R0 = R;
        go();
        while (R && p1!=p2)
            go();
        int dl_c = R0-R;
        int ile_c = R/dl_c;
        z1 += (z2-z1)*ile_c;
        R -= dl_c*ile_c;
        while (R)
            go();
        printf("Case #%d: %Ld\n", tt+1, z1);
    }
}


