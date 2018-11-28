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
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
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

LL N;
int res;

bool ma_dz[1000001];

LL potegi[200000], ile;

int main() {
    FOR(x, 2, 1000000) {
        if (ma_dz[x])
            continue;
        for (int y = 2*x; y<=1000000; y += x)
            ma_dz[y] = 1;
        LL w = x*(LL)x;
        while (w<=1000000*(LL)1000000) {
            potegi[ile++] = w;
            w *= x;
        }
    }
//    fprintf(stderr, "%d\n", ile);
    sort(potegi, potegi+ile);
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%Ld", &N);
        res = 1+(upper_bound(potegi, potegi+ile, N)-potegi);
        if (N==1) 
            res = 0;
        printf("Case #%d: %d\n", (tt+1), res);
    }
}


