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
#include <map>
#include <cassert>

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
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

int P;
ll mustsee[4096];
ll cost[4096][12];
ll D[4096][12][12];

ll infty = 2147483647;

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;

    FOR(test, 1, Tests+1) {
        cin >> P;
        for (int i = 0; i < 1 << P; i++) {
            int v;
            cin >> v;
            mustsee[i] = P - v;
        }
        for (int i = 1; i <= P; i++) {
            for (int j = 0; j < 1<<(P-i); j++) {
                cin >> cost[i][j];
            }
        }

        for (int i = 0; i <= P; i++) {
            for (int j = 0; j < (1<<(P-i)); j++) {
                for (int k = 0; k <= P; k++) {
                    if (i == 0) {
                        if ((mustsee[j] - k) <= 0) {
                            D[j][i][k] = 0;
                        }
                        else {
                            D[j][i][k] = infty;
                        }
                    }
                    else {
                        D[j][i][k] = D[j*2][i-1][k] + D[j*2+1][i-1][k];
                        D[j][i][k] = min(D[j][i][k], D[j*2][i-1][k+1] + cost[i][j] + D[j*2+1][i-1][k+1]);
                    }
                }
            }
        }


        printf("Case #%d: %lld\n", test, D[0][P][0]);
    }
    return 0;

}

