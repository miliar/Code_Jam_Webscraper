#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())


struct node {
    bool internal;
    node *left;
    node *right;
    int value; // leaves
    bool changeable;
    bool is_and;

    int changes[2]; // # of changes to make it desired
};

const int infty = 2100000000;

int M, V;

struct node D[100000];

void solve() {
    scanf("%d %d", &M, &V);
    for (int i = 0; i < (M-1)/2; i++) {
        int is_and, change;
        scanf("%d %d", &is_and, &change);

        D[i].internal = true;
        D[i].left = &D[i*2+1];
        D[i].right = &D[i*2+2];
        D[i].is_and = (is_and) == 1;
        D[i].changeable = (change) == 1;
    }
    for (int i = (M-1)/2; i < M; i++) {
        int value;
        D[i].internal = false;
        scanf("%d", &value);
        D[i].changes[value] = 0;
        D[i].changes[1-value] = infty;
    }
    for (int i = (M-1)/2 - 1; i >= 0; i--) {
        node *l = D[i].left;
        node *r = D[i].right;
        D[i].changes[0] = infty;
        D[i].changes[1] = infty;
        for (int des = 0; des < 2; des++) {
            //
            //  to make the desired
            //

            //
            //  1. and case
            //

            REP(lf, 2) {
                REP(rf, 2) {
                    if (l->changes[lf] >= infty) continue;
                    if (r->changes[rf] >= infty) continue;
                    
                    //printf("%d %d %d\n", lf, rf, (lf & rf));

                    if ( (lf & rf) == des ) {
                        //printf("!!%d\n", D[i].is_and);
                        int cand = l->changes[lf] + r->changes[rf];
                        if (!D[i].is_and) {
                            if (!D[i].changeable) continue;
                            cand++;
                        }
                        D[i].changes[des] = min(D[i].changes[des], cand);
                    }
                }
            }
            

            //
            //  2. or case
            //
            REP(lf, 2) {
                REP(rf, 2) {
                    if (l->changes[lf] >= infty) continue;
                    if (r->changes[rf] >= infty) continue;

                    if ( (lf | rf) == des ) {
                        int cand = l->changes[lf] + r->changes[rf];
                        if (D[i].is_and) {
                            if (!D[i].changeable) continue;
                            cand++;
                        }
                        D[i].changes[des] = min(D[i].changes[des], cand);
                    }
                }
            }
            //printf("%d %d %d\n", i, des, D[i].changes[des]);
        }
    }
    if (D[0].changes[V] == infty) {
        printf("IMPOSSIBLE\n");
    }
    else {
        printf("%d\n", D[0].changes[V]);
    }
}

int main(int argc, char *argv[]) {
    int Tests;
    freopen(argv[1], "r", stdin);
    scanf("%d", &Tests);
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        solve();
    }
}


