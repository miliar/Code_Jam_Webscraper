/*
 * Author: ZaviOr
 * Created Time:  2011/5/22 18:37:53
 * File Name: C.cpp
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

LL v[10001];

int main() {
    freopen("c.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t++ < T) {
        int n;
        LL l, h;
        cin >> n >> l >> h;
        REP(i, n) {
            cin >> v[i];
        }
        bool ans = false;
        for (LL i = l; i <= h; ++i) {
            bool flag = true;
            REP(j, n) {
                if (v[j] % i != 0 && i % v[j] != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans = true;
                printf("Case #%d: %I64d\n", t, i);
                break;
            }
        }
        if (!ans) {
            printf("Case #%d: NO\n", t);
        }
    }
    return 0;
}

