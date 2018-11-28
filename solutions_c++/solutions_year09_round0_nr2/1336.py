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
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;

#define INF 1000000000
#define PB push_back
 
//////////////////////////////////////////

int T, YS, XS;

char nr;

int tab[100][100];
char wyn[100][100];

char start(int x, int y) {
    if (wyn[x][y]) return wyn[x][y];
    int yd[4] = {-1, 0, 0, 1};
    int xd[4] = {0, -1, 1, 0};
    int b = -1, bv = tab[x][y];
    REP(d, 4) {
        int nx = x+xd[d], ny = y+yd[d];
        if (nx<0 || ny<0 || nx>=XS || ny>=YS)
            continue;
        if (tab[nx][ny]<bv) {
            b = d;
            bv = tab[nx][ny];
        }
    }
    if (b<0)
        return wyn[x][y] = nr++;
    return wyn[x][y] = start(x+xd[b], y+yd[b]);
}

int main() {
    scanf("%d",&T);
    REP(t, T) {
        scanf("%d%d", &YS, &XS);
        REP(y, YS) REP(x, XS) {
            scanf("%d", &tab[x][y]);
            wyn[x][y] = 0;
        }
        nr = 'a';
        REP(y, YS) REP(x, XS)
            start(x, y);
        printf("Case #%d:\n", t+1);
        REP(y, YS) REP(x, XS)
            printf("%c%c", wyn[x][y], x==XS-1 ? '\n' : ' ');
    }
}