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

int x[10000];

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int tests;
    cin >> tests;
    int A, n, m;
    FOR(ttt, 1, tests) {
        cin >> n >> m >> A;
        memset(x, 0, sizeof(x));
        FOR(i, 1, n) FOR(j, 1, m) x[i*j] = 1;
        x[0] = 1;
        int x1, y1, x2, y2;
        bool found = false;
        FORD(z, n*m, A) if (x[z] && x[z-A]) {
            //DBG(z); DBG(z - A);
            found = true;
            FORD(i, n, 1) if ((z % i) == 0) {
                if (z / i <= m) {
                    x1 = i;
                    y2 = z / i;
                }
                break;
            }
            if (z == A) {
                x2 = 1;
                y1 = 0;
            }
            else FORD(i, n, 1) if (((z-A) % i) == 0) {
                if ((z-A) / i <= m) {
                    x2 = i;
                    y1 = (z-A) / i;
                }
                break;
            }
            break;
        }
        if (!found)
            cout << "Case #" << ttt << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << ttt << ": 0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
    }

    return 0;
}
