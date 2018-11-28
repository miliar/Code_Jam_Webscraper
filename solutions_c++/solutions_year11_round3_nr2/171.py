/*
 * Author: ZaviOr
 * Created Time:  2011/5/22 17:59:41
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define FORIT(I,V) for (typeof(V.begin()) I = V.begin(); I != V.end(); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
typedef long long LL;

vector<pair<LL, int> > a;

void show(const pair<LL, int> &x) {
    cout << x.first << " " << x.second << endl;
}

int main() {
    freopen("B.out", "w", stdout);
    int T, ncase = 0, l, n, c;
    LL t;
    scanf("%d", &T);
    while (ncase++ < T) {
        scanf("%d%I64d%d%d", &l, &t, &n, &c);
        a.clear();
        REP(i, c) {
            int v;
            scanf("%d", &v);
            a.PB(MP(LL(v), n / c + (((n % c) > i) ? 1 : 0)));
            //show(a[i]);
        }
        LL ans = 0;
        REP(i, n) {
            if (ans + a[i % c].first * 2 >= t) {
                a.PB(MP(a[i % c].first - (t - ans) / 2, 1));
                ans = t;
                a[i % c].second--;
                //show(*(a.rbegin()));
                break;
            } else {
                ans += a[i % c].first * 2;
                a[i % c].second--;
            }
        }
        sort(ALL(a));
        for (int i = SZ(a) - 1; i >= 0; --i) {
            //show(a[i]);
            ans += ((LL)a[i].first) * a[i].second * 2;
            ans -= ((LL)a[i].first) * min(l, a[i].second);
            l -= min(l, a[i].second);
        }
        printf("Case #%d: %I64d\n", ncase, ans);
    }
    return 0;
}

