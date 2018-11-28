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

#define FIN "test.in"
#define FOUT "test.out"

#define MAX_S 100
#define MAX_Q 1000

int a[MAX_Q + 10][MAX_S + 10];
vector<string> servers;
vector<int> queries;
map<string, int> msi;

int go() {
    int S = SIZE(servers);
    int Q = SIZE(queries);
    if (Q <= 1) return 0;
    REP(i, S) a[0][i] = 0;
    FOR(i, 1, Q) {
        int q = queries[i-1];
        REP(j, S) {
            if (q == j) {
                a[i][j] = MAX_Q;
            } else {
                a[i][j] = a[i-1][j];
                REP(k, S) a[i][j] = min(a[i][j], a[i-1][k] + 1);
            }
        }
    }
    int res = MAX_Q;
    REP(i, S) res = min(res, a[Q][i]);
    return res;
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int tests;
    cin >> tests;

    REP(ttt, tests) {
        memset(a, 0, sizeof(a));
        servers.clear();
        queries.clear();
        msi.clear();
        int S, Q;
        string tmp;
        cin >> S; getline(cin, tmp);
        REP(i, S) {
            getline(cin, tmp);
            servers.PB(tmp);
            msi[servers[i]] = i;
        }
        cin >> Q; getline(cin, tmp);
        REP(i, Q) {
            getline(cin, tmp);
            queries.PB(msi[tmp]);
        }
        cout << "Case #" << (ttt + 1) << ": " << go() << endl;
    }
    return 0;
}
