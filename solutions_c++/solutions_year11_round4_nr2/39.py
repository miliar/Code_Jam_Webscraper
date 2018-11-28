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

int N, len, S, R, cz_b;
double czas;

pair<int, pii> kor[1000]; //(pr, pocz, kon)


char tab[501][501];

int odchx[501][501];
int odchy[501][501];

int odch_w[501][501];
int odch_k[501][501];
int suma_w[501][501];
int suma_k[501][501];

int best, xs, ys;

void find_odd(bool parz) {
    int s,l,p;
    if (parz) {
        s = 2;
        l = 0;
        p = 1;
        REP(x, xs) REP(y, ys) {
            odch_w[x][y] = tab[x][y]-tab[x+1][y];
            odch_k[x][y] = tab[x][y]-tab[x][y+1];
            suma_w[x][y] = tab[x][y]+tab[x+1][y];
            suma_k[x][y] = tab[x][y]+tab[x][y+1];
        }
        REP(x, xs-1) REP(y, ys-1) {
            odchx[x][y] = odch_w[x][y]+odch_w[x][y+1];
            odchy[x][y] = odch_k[x][y]+odch_k[x+1][y];
        }
    }
    else {
        s = 1;
        l = 0, p = 0; // od srodka do boku
        REP(x, xs) REP(y, ys) {
            odchx[x][y] = odchy[x][y] = odch_k[x][y] = odch_w[x][y] = 0;
            suma_w[x][y] = suma_k[x][y] = tab[x][y];
        }
    }
    while (s<=xs && s<=ys) {
        s += 2;
        ++l; ++p;
        FOR(x, l, xs-1-p) REP(y, ys)
            suma_w[x][y] += tab[x-l][y]+tab[x+p][y];
        REP(x, xs) FOR(y, l, ys-1-p)
            suma_k[x][y] += tab[x][y-l]+tab[x][y+p];
        FOR(x, l, xs-1-p) FOR(y, l, ys-1-p) {
            odchx[x][y] += suma_k[x-l][y]-suma_k[x+p][y]+odch_w[x][y-l]+odch_w[x][y+p];
            odchy[x][y] += suma_w[x][y-l]-suma_w[x][y+p]+odch_k[x-l][y]+odch_k[x+p][y];
            int ox = odchx[x][y]-tab[x-l][y-l]-tab[x-l][y+p]+tab[x+p][y-l]+tab[x+p][y+p];
            int oy = odchy[x][y]-tab[x-l][y-l]+tab[x-l][y+p]-tab[x+p][y-l]+tab[x+p][y+p];
            if (!ox && !oy)
                best = s;
        }
        FOR(x, l, xs-1-p) REP(y, ys)
            odch_w[x][y] += tab[x-l][y]-tab[x+p][y];
        REP(x, xs) FOR(y, l, ys-1-p)
            odch_k[x][y] += tab[x][y-l]-tab[x][y+p];
    }
}


int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%*d", &xs, &ys);
        REP(x, xs)
            scanf("%s", tab[x]);
        best = 0;
        printf("Case #%d: ", (tt+1));
        find_odd(false);
        find_odd(true);
        if (best<3)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", best);
        fprintf(stderr, "%d\n", tt+1);
    }
}


