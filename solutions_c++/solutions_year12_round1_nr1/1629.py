#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 1

int main()
{

#if SMALL
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
#else
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

    int T, A, B;
    double p[10], ans, prob[10], exp[10];
    int stroke[10][10];
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d", &A, &B);
        REP(i,A) scanf("%lf", &p[i]);
        memset(stroke, 0, sizeof(stroke));
        ans = 100000;

        REP(mask,1<<A) {
            prob[mask] = 1;
            REP(j,A) {
                if (mask & (1<<j)) prob[mask] *= 1 - p[A-1-j];
                else prob[mask] *= p[A-1-j];
            }
        }
        REP(i,A+1) {
            REP(mask,1<<A) {
                stroke[i][mask] += 2*i;
                bool wrong = false;
                REP(j,A) {
                    if (j >= i && (mask & (1 << j))) {
                        wrong = true;
                        break;
                    }
                }
                if (wrong) stroke[i][mask] += B + 1;
                stroke[i][mask] += B - A + 1;
            }
        }
        REP(mask,1<<A) stroke[A+1][mask] = B + 2;
        REP(i,A+2) {
            exp[i] = 0;
            REP(mask,1<<A) exp[i] += stroke[i][mask] * prob[mask];
            ans = min(ans, exp[i]);
        }
        /*
        REP(mask, 1<<A) printf("%.6lf\t", prob[mask]);
        printf("\n");
        REP(i,A+2) {
            REP(mask,1<<A) printf("%d\t", stroke[i][mask]);
            printf("%.6lf\n", exp[i]);
        }
        */
        printf("Case #%d: %.6lf\n", tc, ans);
    }
    return 0;
}
