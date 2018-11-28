#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBG(x) cout << #x << " = " << (x) << endl
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl

#define PI 3.14159265358979
#define EPS 1e-8

#define FIN "test.in"
#define FOUT "test.out"

#define MAXC 1000000

int a[MAXC + 10];
bool gate[MAXC + 10];
bool agate[MAXC + 10];
bool change[MAXC + 10];

int calc(int x) {
    if (!gate[x]) return a[x];
    if (agate[x]) a[x] = calc(2*x)*calc(2*x+1);
    else {
        if (calc(2*x) == 1) a[x] = 1;
        else a[x] = calc(2*x + 1);
    }
    return a[x];
}

void norm(int& l, int& r) {
    if (l < 0) l = r;
    if (r < 0) r = l;
}

int calc_mv(int i, int v) {
    //DBG(i);
    int l, r;
    if (a[i] == v) return 0;
    if (!gate[i]) {
        if (a[i] != v) return -1;
        else return 0;
    } else {
        if (!agate[i]) {
            if (v == 1) {
                l = calc_mv(2*i, 1);
                r = calc_mv(2*i + 1, 1);
                if ((l == -1) && (r == -1)) return -1;
                norm(l, r);
                return min(l, r);
            } else {
                if (change[i]) {
                    if ((a[2*i] == 0) || (a[2*i + 1] == 0)) return 1;
                    l = calc_mv(2*i, 0);
                    r = calc_mv(2*i + 1, 0);
                    if ((l == -1) && (r == -1)) return -1;
                    norm(l, r);
                    //printf("i=%d, l=%d, r=%d\n", i, l, r);
                    return 1 + min(l, r);
                } else {
                    if (a[2*i] == 0) return calc_mv(2*i+1, 0);
                    if (a[2*i+1] == 0) return calc_mv(2*i, 0);
                    l = calc_mv(2*i, 0);
                    r = calc_mv(2*i + 1, 0);
                    if ((l == -1) || (r == -1)) return -1;
                    return l + r;
                }
            }
        } else {
            if (v == 0) {
                l = calc_mv(2*i, 0);
                r = calc_mv(2*i + 1, 0);
                if ((l == -1) && (r == -1)) return -1;
                norm(l, r);
                return min(l, r);
            } else {
                if (change[i]) {
                    if ((a[2*i] == 1) || (a[2*i + 1] == 1)) return 1;
                    l = calc_mv(2*i, 1);
                    r = calc_mv(2*i + 1, 1);
                    if ((l == -1) && (r == -1)) return -1;
                    norm(l, r);
                    return 1 + min(l, r);
                } else {
                    if (a[2*i] == 1) return calc_mv(2*i+1, 1);
                    if (a[2*i+1] == 1) return calc_mv(2*i, 1);
                    l = calc_mv(2*i, 1);
                    r = calc_mv(2*i + 1, 1);
                    if ((l == -1) || (r == -1)) return -1;
                    return l + r;
                }
            }
        }
    }
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int tests;
    cin >> tests;
    int M, V;
    FOR(ttt, 1, tests) {
        cin >> M >> V;
        FOR(i, 1, M) {
            a[i] = -1;
            gate[i] = false;
            agate[i] = false;
            change[i] = false;
        }
        FOR(i, 1, (M-1)/2) {
            int G, C;
            cin >> G >> C;
            gate[i] = true;
            if (G) agate[i] = true;
            if (C) change[i] = true;
        }
        FOR(i, (M-1)/2 + 1, M) {
            cin >> a[i];
        }
        //FOR(i, 1, 9) cout << gate[i]; cout << endl;
        calc(1);
        //FOR(i, 1, 9) cout << a[i]; cout << endl;
        int res = calc_mv(1, V);
        if (res == -1)
            cout << "Case #" << ttt << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << ttt << ": " << res << endl;
    }

    return 0;
}
