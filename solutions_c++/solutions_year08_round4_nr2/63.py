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

typedef long long ll;


ll N, M, A;

void eval() {
    ll x[3], y[3];
    x[0] = 0;
    y[0] = 0;
    for (x[1] = x[0]; x[1] <= N; x[1]++) {
        for (x[2] = x[1]; x[2] <= N; x[2]++) {
            if (x[0] == x[1] && x[1] == x[2]) continue;
            for (y[1] = -M; y[1] <= M; y[1]++) {
                for (y[2] = -M; y[2] <= M; y[2]++) {
                    int ymin = min(y[0], min(y[1], y[2]));
                    int ymax = max(y[0], max(y[1], y[2]));
                    if (ymax - ymin > M) continue;
                    ll result = x[1] * y[2] - x[2] * y[1];
                    if (result < 0) result = -result;
                    if (result == A) {
                        REP(i, 3) {
                            y[i] -= ymin;
                        }
                        REP(i, 3) {
                            printf(" %lld %lld", x[i], y[i]);
                        }
                        printf("\n");
                        return;
                    }

                }
            }
        }
    }
    printf(" IMPOSSIBLE\n");
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d:", test);
        cin >> N >> M >> A;
        eval();
    }
}
