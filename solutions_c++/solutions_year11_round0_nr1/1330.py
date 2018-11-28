/*
 * Author: ZaviOr
 * Created Time:  2011/5/7 13:48:12
 * File Name: A.cpp
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

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t < T) {
        printf("Case #%d: ", ++t);
        int n;
        cin >> n;
        int ca = 0, cb = 0, pa = 1, pb = 1, ans = 0;
        REP(i, n) {
            char c;
            int p;
            cin >> c >> p;
            if (c == 'O') {
                ca += max(abs(pa - p) - cb, 0) + 1;
                ans += max(abs(pa - p) - cb, 0) + 1;
                pa = p;
                cb = 0;
            } else {
                cb += max(abs(pb - p) - ca, 0) + 1;
                ans += max(abs(pb - p) - ca, 0) + 1;
                pb = p;
                ca = 0;
            }
            //printf("%c %d ans = %d ca = %d cb = %d\n", c, p, ans, ca, cb);
        }
        cout << ans << endl;
    }
    return 0;
}

