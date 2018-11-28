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

int d[4][2] = {
    -1, 0,
    0, -1,
    0, 1,
    1, 0
};

const int infty = 2147000000;

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d:\n", test);
        int H, W;
        int p[20000];
        int level[200][200];
        cin >>H >>W;
        REP(i, H) {
            REP(j, W) {
                cin >> level[i][j];
                p[i*W+j] = i*W+j;
            }
        }
        REP(i, H) {
            REP(j, W) {
                int min_alt = infty;
                int pi, pj;
                REP(k, 4) {
                    int qi = i+d[k][0];
                    int qj = j+d[k][1];
                    if (0 <= qi && qi < H && 0 <= qj && qj < W) {
                        if (min_alt > level[qi][qj]) {
                            min_alt = level[qi][qj];
                            pi = qi; pj = qj;
                        }
                    }
                }
                if (min_alt < infty && min_alt < level[i][j]) {
                    int ca = p[i*W+j]; int cb = p[pi*W+pj];
                    while (p[ca] != ca) ca = p[ca];
                    while (p[cb] != cb) cb = p[cb];
                    if (ca > cb) swap(ca, cb);
                    p[cb] = ca;
                }
            }
        }
        set<int> tops;
        map<int, char> cvt;
        REP(i, H) {
            REP(j, W) {
                int ca = p[i*W+j];
                while (p[ca] != ca) ca = p[ca];
                p[i*W+j] = ca;
                tops.insert(ca);
            }
        }
        int cnt = 0;
        FORE(it, tops) {
            cvt[*it] = 'a' + cnt;
            cnt++;
        }
        REP(i, H) {
            REP(j, W) {
                printf("%c", cvt[p[i*W+j]]);
                printf( (j+1 == W) ? "\n" : " ");
            }
        }
    }

}
