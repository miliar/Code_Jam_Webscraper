#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

int ile_zm[2][10000];
int gates[10000][2];

#define INF 1000000

int main() {
    int z;
    scanf("%d", &z);
    FOR(zz, 1, z) {
        int n, v;
        scanf("%d%d", &n, &v);
        int gnum = (n-1)/2, lnum = (n+1)/2;
        REP(i, gnum)
            scanf("%d %d", &gates[i][0], &gates[i][1]);
        REP(i, lnum) {
            int lvalue;
            scanf("%d", &lvalue);
            ile_zm[lvalue][gnum+i] = 0;
            ile_zm[lvalue^1][gnum+i] = INF;
        }
        FORD(i, gnum-1, 0) {
            ile_zm[0][i] = ile_zm[1][i] = INF;
            if (gates[i][0] == 1) { //AND GATE
                ile_zm[1][i] <?= ile_zm[1][2*i+1] + ile_zm[1][2*i+2];
                ile_zm[0][i] <?= (ile_zm[0][2*i+1] + ile_zm[1][2*i+2])<?(ile_zm[1][2*i+1] + ile_zm[0][2*i+2])<?
                    (ile_zm[0][2*i+1] + ile_zm[0][2*i+2]);
            } else { // OR GATE
                ile_zm[0][i] <?= ile_zm[0][2*i+1] + ile_zm[0][2*i+2];
                ile_zm[1][i] <?= (ile_zm[0][2*i+1] + ile_zm[1][2*i+2])<?(ile_zm[1][2*i+1] + ile_zm[0][2*i+2])<?
                    (ile_zm[1][2*i+1] + ile_zm[1][2*i+2]);
            }
            if (gates[i][1] == 1) { // changeable
                if (gates[i][0] == 0) { //changed to AND GATE
                    ile_zm[1][i] <?= ile_zm[1][2*i+1] + ile_zm[1][2*i+2] + 1;
                    ile_zm[0][i] <?= 1+ ((ile_zm[0][2*i+1] + ile_zm[1][2*i+2])<?(ile_zm[1][2*i+1] + ile_zm[0][2*i+2])<?
                        (ile_zm[0][2*i+1] + ile_zm[0][2*i+2]));
                } else { //changed to OR GATE
                    ile_zm[0][i] <?= ile_zm[0][2*i+1] + ile_zm[0][2*i+2] + 1;
                    ile_zm[1][i] <?= ((ile_zm[0][2*i+1] + ile_zm[1][2*i+2])<?(ile_zm[1][2*i+1] + ile_zm[0][2*i+2])<?
                        (ile_zm[1][2*i+1] + ile_zm[1][2*i+2]))+1;
                }
            }
        }
        //REP(i, n) printf("%d: %d %d\n", i, ile_zm[0][i], ile_zm[1][i]);
        if (ile_zm[v][0] == INF)
            printf("Case #%d: IMPOSSIBLE\n", zz);
        else
            printf("Case #%d: %d\n", zz, ile_zm[v][0]);
    }
    return 0;
}
