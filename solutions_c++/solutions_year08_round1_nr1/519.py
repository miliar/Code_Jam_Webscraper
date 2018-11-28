/*
ID: ram3ai1
LANG: C++
TASK: heritage
*/

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
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
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBG(x) cout << #x << " = " << x << endl;
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int T, n, t;
    cin >> T;
    vector<long long> ap, an, bn, bp, ar, br;
    REP(zzz, T)  {
        ap.clear();
        bp.clear();
        an.clear();
        bn.clear();
        cin >> n;
        REP(i, n) {
            cin >> t;
            if (t < 0) an.PB(t); else ap.PB(t);
        }
        REP(j, n) {
            cin >> t;
            if (t < 0) bn.PB(t); else bp.PB(t);
        }
        long long sc = 0;
        sort(ALL(an));
        sort(ALL(bn));
        sort(ALL(bp));
        sort(ALL(ap));
        int san, sbn, sbp, sap;
        san = SIZE(an);
        sap = SIZE(ap);
        sbn = SIZE(bn);
        sbp = SIZE(bp);
        // an - bp
        REP(i, min(san, sbp)) {
            sc += an[i] * bp[sbp - i - 1];
        }
        // bn - ap
        REP(i, min(sbn, sap)) {
            sc += bn[i] * ap[sap - i - 1];
        }
        ar.clear();
        br.clear();
        //DBG(sc); DBG(san); DBG(sap); DBG(sbn); DBG(sbp);
            if (san > sbp) {
                FOR(i, sbp, san - 1) ar.PB(-an[i]);
            } else {
                REP(i, sbp - san) br.PB(bp[i]);
            }
            if (sbn > sap) {
                FOR(i, sap, sbn - 1) br.PB(-bn[i]);
            } else {
                REP(i, sap - sbn) ar.PB(ap[i]);
            }
            sort(ALL(ar));
            sort(ALL(br));
            REP(i, SIZE(ar)) sc += ar[i] * br[SIZE(ar) - i - 1];

        cout << "Case #" << (zzz + 1) << ": " << sc << endl;
    }

    return 0;
}
