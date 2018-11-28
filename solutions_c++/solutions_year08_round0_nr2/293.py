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

#define FAIL "FAIL"

string adj_time(string t, int dt) {
    int hh, mm;
    hh = 10 * (t[0] - '0') + (t[1] - '0');
    mm = 10 * (t[3] - '0') + (t[4] - '0');
    mm += dt;
    if (mm >= 60) {
        hh++;
        mm -= 60;
    }
    if (hh >= 24) return FAIL;
    string res = t;
    res[0] = '0' + hh / 10;
    res[1] = '0' + hh % 10;
    res[3] = '0' + mm / 10;
    res[4] = '0' + mm % 10;
    return res;
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int tests;
    vector<pair<string, string> > vpss;

    cin >> tests;
    FOR(ttt, 1, tests) {
        int na, nb, T;
        cin >> T >> na >> nb;
        vpss.clear();
        string tmp1, tmp2;
        REP(i, na) {
            cin >> tmp1 >> tmp2;
            vpss.PB(make_pair(tmp1 + 'a', tmp2 + 'b'));
        }
        REP(i, nb) {
            cin >> tmp1 >> tmp2;
            vpss.PB(make_pair(tmp1 + 'b', tmp2 + 'a'));
        }
        sort(ALL(vpss));
        int n = na + nb;
        vector<bool> covered(n, false);
        int trains[2];
        trains[0] = trains[1] = 0;
        REP(i, n) if (!covered[i]) {
            trains[vpss[i].first[5] - 'a']++;
            covered[i] = true;
            string cur_time = adj_time(vpss[i].second, T);
            FOR(j, i + 1, n - 1) {
                if ((!covered[j]) && (cur_time[5] == vpss[j].first[5]) && (vpss[j].first >= cur_time)) {
                    covered[j] = true;
                    cur_time = adj_time(vpss[j].second, T);
                }
            }
        }
        cout << "Case #" << ttt << ": " << trains[0] << ' ' << trains[1] << endl;
    }

    return 0;
}
